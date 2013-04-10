import random
import math

import lineObject
import physics


class Asteroid(lineObject.Thing):
	def __init__(self, **kwargs):
		self.size = kwargs.get('size', 4)
		self.radius = self.size * 10
		pointsX, pointsY = self.generate()

		super(Asteroid, self).__init__(pointsX=pointsX, pointsY=pointsY, **kwargs)

	def generate(self, verticies=15):
		pointsX = []
		pointsY = []
		for i in range(verticies):
			rad = random.randint(self.radius - self.radius // 5, self.radius + self.radius // 5)
			part = math.radians(360 / verticies * i)
			pointsX.append(math.cos(part) * rad)
			pointsY.append(math.sin(part) * rad)
		return pointsX, pointsY

	def update(self, dt):
		self.rotation += .3
		super(Asteroid, self).update(dt)

	def die(self):
		if self.size == 1:
			return None, None
		cv1 = self.vel.rotate(45) * 1.5
		cv2 = self.vel.rotate(-45) * 1.5
		child1 = Asteroid(size=self.size / 2, vel=cv1, x=self.x, y=self.y)
		child2 = Asteroid(size=self.size / 2, vel=cv2, x=self.x, y=self.y)
		return child1, child2


def buildAsteroidField():
	asteroids = []
	for i in range(10):
		asteroid = Asteroid(radius=40)
		asteroid.x = random.randint(0, 800)
		asteroid.y = random.randint(0, 600)
		asteroid.vel = physics.vector2(x=random.randint(-50, 50), y=random.randint(-50, 50))
		asteroids.append(asteroid)
	return asteroids