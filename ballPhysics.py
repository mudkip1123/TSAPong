import pyglet


class PhysicalBall(pyglet.sprite.Sprite):
	def __init__(self, *args, **kwargs):
		super(PhysicalBall, self).__init__(*args, **kwargs)
		self.vX = 0.0
		self.vY = 0.0

	def update(self, dt):
		self.x += self.vX * dt
		self.y += self.vY * dt