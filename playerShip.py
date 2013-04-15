import math

import physics
import bullet
import lineObject
import load


class Ship(lineObject.Thing):
	def __init__(self, **kwargs):
		super(Ship, self).__init__(pointsX=[1.5, -1.5, -1, -1.5], pointsY=[0, -1, 0, 1], **kwargs)
		self.rounds = []

		self.burning = False
		self.shooting = False
		self.braking = False

		self.shotDelay = 10
		self.shotTimer = self.shotDelay
		self.turnSpeed = 6
		self.enginePower = 10

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
			if i.lifetime <= 0:
				self.rounds.remove(i)

		#Update self
		self.vel *= .983
		super(Ship, self).update(dt)
		self.wraparound()

	def burn(self):
		self.vel = physics.addAcceleration(self.vel, self.rotation, self.enginePower)

	def shoot(self):
		bx = self.x + 20 * math.cos(math.radians(self.rotation))
		by = self.y + 20 * math.sin(math.radians(self.rotation))
		self.rounds.append(bullet.Bullet(x=bx, y=by, vel=self.vel, rotation=self.rotation))
		self.shotTimer = self.shotDelay
		# load.shot_sound.play()

	def draw(self):
		for i in self.rounds:
			i.draw()
		super(Ship, self).draw()

	def wraparound(self):
		x, y, vx, vy = self.x, self.y, self.vel.x, self.vel.y

		if x < 0 and vx < 0:
			self.vel.x *= -1
		if x > 800 and vx > 0:
			self.vel.x *= -1
		if y > 600 and vy > 0:
			self.vel.y *= -1
		if y < 0 and vy < 0:
			self.vel.y *= -1

	def reset(self):
		self.x = 400
		self.y = 300
		self.rotation = 0
		self.vel = physics.vector2(x=0, y=0)
		self.rounds = []