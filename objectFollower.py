import pyglet

import physics

import math


class Follower():
	def __init__(self, target, speed, *args, **kwargs):
		self.x = 0
		self.y = 0
		self.rotation = 0
		self.target = target
		self.vX = 0.0
		self.vY = 0.0
		self.speed = speed

		self.pointsX = [-4, 4, 4, -4]
		self.pointsY = [-2, -2, 2, 2]

	def draw(self):
		pointsX = [i * 10 for i in self.pointsX]
		pointsY = [i * 10 for i in self.pointsY]

		coords = physics.revolve(pointsX, pointsY, self.rotation, self.x, self.y)

		pyglet.graphics.draw(4, pyglet.gl.GL_LINE_LOOP, ('v2f', coords))

	def update(self, dt):
		self.rotation += 1
		dx = self.target.x - self.x
		dy = self.target.y - self.y
		mag = math.sqrt(dx ** 2 + dy ** 2)

		self.x += dx / mag * self.speed * dt
		self.y += dy / mag * self.speed * dt