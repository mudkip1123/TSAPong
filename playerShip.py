import pyglet

import physics
import bullet


class Ship:
	def __init__(self, x=0, y=0, rotation=0, dx=0, dy=0):
		self.x, self.y = x, y
		self.rotation = rotation
		self.vel = physics.vector2(x=dx, y=dy)
		self.pointsX = [2, -2, -1, -2]
		self.pointsY = [0, -2, 0, 2]
		self.rounds = []

		self.burning = False
		self.shooting = False
		self.braking = False

		self.shotTimer = 30

	def update(self, dt):
		# Counters
		self.shotTimer -= 1

		#Update key things
		if self.burning:
			self.burn()
		if self.shooting and self.shotTimer <= 0:
			self.shoot()

		#Update shots
		for i in self.rounds:
			i.update(dt)

		#update self
		self.x += self.vel.x * dt
		self.y += self.vel.y * dt
		self.wraparound(dt)

	def burn(self):
		self.vel = physics.addAcceleration(self.vel, self.rotation, 3)

	def shoot(self):
		self.rounds.append(bullet.Bullet(self.x, self.y, self.vel, self.rotation))
		self.shotTimer = 30

	def draw(self):
		for i in self.rounds:
			i.draw()

		pointsX = [i * 10 for i in self.pointsX]
		pointsY = [i * 10 for i in self.pointsY]

		coords = physics.revolve(pointsX, pointsY, self.rotation, self.x, self.y)

		pyglet.graphics.draw(4, pyglet.gl.GL_LINE_LOOP, ('v2f', coords))

	def wraparound(self, dt):
		x, y, vx, vy = self.x, self.y, self.vel.x, self.vel.y

		if x < 0 and vx < 0:
			self.vel.x *= -1
		if x > 800 and vx > 0:
			self.vel.x *= -1
		if y > 600 and vy > 0:
			self.vel.y *= -1
		if y < 0 and vy < 0:
			self.vel.y *= -1