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

	def draw(self, scale=3):
		super(Bullet, self).draw(scale)
