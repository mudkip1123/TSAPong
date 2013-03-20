import pyglet

import physics


class Ship:
	def __init__(self, x=0, y=0, rotation=0, dx=0, dy=0):
		self.x = x
		self.y = y
		self.rotation = rotation
		self.dx = dx
		self.dy = dy
		self.pointsX = [0, 2, 0, -2]
		self.pointsY = [2, -2, -1, -2]

	def update(self, dt):
		self.x += self.dx * dt
		self.y += self.dy * dt
		self.wraparound(dt)

	def pedal(self):
		self.dx, self.dy = physics.addAcceleration(self.dx, self.dy, self.rotation + 90, 10)

	def draw(self):
		pointsX = [i * 10 for i in self.pointsX]
		pointsY = [i * 10 for i in self.pointsY]

		coords = physics.revolve(pointsX, pointsY, self.rotation, self.x, self.y)

		pyglet.graphics.draw(4, pyglet.gl.GL_LINE_LOOP, ('v2f', coords))

	def wraparound(self, dt):
		x, y, vx, vy = self.x, self.y, self.dx, self.dy

		if x < 0 and vx < 0:
			self.dx *= -1
		if x > 800 and vx > 0:
			self.dx *= -1
		if y > 600 and vy > 0:
			self.dy *= -1
		if y < 0 and vy < 0:
			self.dy *= -1