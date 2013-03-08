import pyglet


class PhysicalBall(pyglet.sprite.Sprite):
	def __init__(self, *args, **kwargs):
		super(PhysicalBall, self).__init__(*args, **kwargs)
		self.vX = 0.0
		self.vY = 0.0

	def update(self, dt):
		self.x += self.vX * dt
		self.y += self.vY * dt
		self.wraparound(dt)

	def wraparound(self, dt):
		x, y, vx, vy = self.x, self.y, self.vX, self.vY

		if x < 0 and vx < 0:
			self.vX *= -1
		if x > 800 and vx > 0:
			self.vX *= -1
		if y > 600 and vy > 0:
			self.vY *= -1
		if y < 0 and vy < 0:
			self.vY *= -1