import pyglet

import physics


class Thing:
	def __init__(self, pointsX=None, pointsY=None, **kwargs):
		self.pointsX = pointsX
		self.pointsY = pointsY
		self.vel = kwargs.get("vel", physics.vector2(x=0, y=0))
		self.x = kwargs.get("x", 0)
		self.y = kwargs.get("y", 0)
		self.rotation = kwargs.get("rotation", 0)

	def draw(self, scale):
		pointsX = [i * scale for i in self.pointsX]
		pointsY = [i * scale for i in self.pointsY]
		coords = physics.revolve(pointsX, pointsY, self.rotation, self.x, self.y)
		pyglet.graphics.draw(len(pointsX), pyglet.gl.GL_LINE_LOOP, ('v2f', coords))

	def update(self, dt):
		self.x += self.vel.x * dt
		self.y += self.vel.y * dt