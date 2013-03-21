import pyglet

import physics


class Bullet:
	def __init__(self, x, y, vel, rotation, lifetime=1000):
		self.x, self.y = x, y
		self.rotation = rotation
		self.lifetime = lifetime
		self.pointsX = [0, 1, -1]
		self.pointsY = [1, -1, -1]
		self.vel = physics.addAcceleration(vel, self.rotation, 100)

	def update(self, dt):
		self.rotation += 10
		self.lifetime -= 1
		self.x += self.vel.x * dt
		self.y += self.vel.y * dt
		self.wraparound()

	def draw(self):
		pointsX = [i * 3 for i in self.pointsX]
		pointsY = [i * 3 for i in self.pointsY]

		coords = physics.revolve(pointsX, pointsY, self.rotation, self.x, self.y)

		pyglet.graphics.draw(3, pyglet.gl.GL_LINE_LOOP, ('v2f', coords))

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