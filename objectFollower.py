import pyglet

import math


class Follower(pyglet.sprite.Sprite):
	def __init__(self, target, speed, *args, **kwargs):
		super(Follower, self).__init__(*args, **kwargs)

		self.target = target
		self.vX = 0.0
		self.vY = 0.0
		self.speed = speed

	def update(self, dt):
		dx = self.target.x - self.x
		dy = self.target.y - self.y
		mag = math.sqrt(dx ** 2 + dy ** 2)

		self.x += dx / mag * self.speed * dt
		self.y += dy / mag * self.speed * dt