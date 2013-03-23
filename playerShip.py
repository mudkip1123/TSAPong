import physics
import bullet
import lineObject


class Ship(lineObject.Thing):
	def __init__(self, **kwargs):
		super(Ship, self).__init__(pointsX=[2, -2, -1, -2], pointsY=[0, -2, 0, 2], **kwargs)
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
			if i.lifetime <= 0:
				self.rounds.remove(i)

		#Update self
		self.vel *= .99
		super(Ship, self).update(dt)
		self.wraparound()

	def burn(self):
		self.vel = physics.addAcceleration(self.vel, self.rotation, 3)

	def shoot(self):
		self.rounds.append(bullet.Bullet(x=self.x, y=self.y, vel=self.vel, rotation=self.rotation))
		self.shotTimer = 30

	def draw(self, scale=10):
		for i in self.rounds:
			i.draw()
		super(Ship, self).draw(scale)

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