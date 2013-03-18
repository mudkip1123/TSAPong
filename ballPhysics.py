import pyglet


class PhysicalBall(pyglet.sprite.Sprite):
	def __init__(self, *args, **kwargs):
		super(PhysicalBall, self).__init__(*args, **kwargs)
		self.rotation = 0
		self.vX = 0.0
		self.vY = 0.0

	def update(self, dt):
		self.x += self.vX * dt
		self.y += self.vY * dt
		self.wraparound(dt)

	def draw(self):
		pointsX = [i * 10 + self.x for i in [0, 2, 0, -2]]
		pointsY = [i * 10 + self.y for i in [3, -1, 0, -1]]
		coords = [None] * (len(pointsX) + len(pointsY))
		coords[::2] = pointsX
		coords[1::2] = pointsY
		pyglet.graphics.draw(4, pyglet.gl.GL_LINE_LOOP,
			('v2f', coords))

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