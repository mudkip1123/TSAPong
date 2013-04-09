import pyglet

import physics


class Thing(object):
	def __init__(self, pointsX=None, pointsY=None, **kwargs):
		self.pointsX = pointsX
		self.pointsY = pointsY
		self.vel = kwargs.get("vel", physics.vector2(x=0, y=0))
		self.x = kwargs.get("x", 0)
		self.y = kwargs.get("y", 0)
		self.rotation = kwargs.get("rotation", 0)
		self.scale = kwargs.get('scale',1)

	def coord_shift(self):
		pointsX = [i * self.scale for i in self.pointsX]
		pointsY = [i * self.scale for i in self.pointsY]
		coords = physics.revolve(pointsX, pointsY, self.rotation, self.x, self.y)
		return coords

	def draw(self):
		coords = self.coord_shift()
		pyglet.graphics.draw(len(coords) / 2, pyglet.gl.GL_LINE_LOOP, ('v2f', coords))

	def update(self, dt):
		self.x += self.vel.x * dt
		self.y += self.vel.y * dt
		self.wraparound()

	def wraparound(self):
		if self.x > 800:
			self.x = 0
		if self.x < 0:
			self.x = 800
		if self.y > 600:
			self.y = 0
		if self.y < 0:
			self.y = 600
		self.x = max(min(self.x, 800), 0)
		self.y = max(min(self.y, 600), 0)

	def segments(self):
		coords = self.coord_shift()
		p = [(i[j], i[j + 1]) for i in [coords] for j in range(0, len(i) - 1, 2)]
		# print p
		points = [physics.point(k[0], k[1]) for k in p]
		s = []

		for i in range(len(points) - 1):
			s.append(physics.segment(points[i], points[i + 1]))

		return s
