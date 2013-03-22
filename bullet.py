import physics
import lineObject


class Bullet(lineObject.Thing):
	def __init__(self, lifetime=400, **kwargs):
		super(Bullet, self).__init__(pointsX=[0, 1, -1], pointsY=[1, -1, -1], **kwargs)
		self.lifetime = lifetime
		self.vel = physics.addAcceleration(self.vel, self.rotation, 100)

	def update(self, dt):
		self.rotation += 10
		self.lifetime -= 1
		super(Bullet, self).update(dt)
		self.wraparound()

	def draw(self, scale=3):
		super(Bullet, self).draw(3)

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