import math


def ccw(A, B, C):
	return (C.y - A.y) * (B.x - A.x) > (B.y - A.y) * (C.x - A.x)


# Return true if line segments AB and CD intersect
def intersect(A, B, C, D):
	return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)


def revolve(lo):
	coords = []
	for i in range(len(lo.pointsX)):
		x = lo.pointsX[i]
		y = lo.pointsY[i]
		theta = math.radians(lo.rotation)
		coords.append(x * math.cos(theta) - y * math.sin(theta) + lo.dx)
		coords.append(x * math.sin(theta) + y * math.cos(theta) + lo.dy)
	return coords


def addAcceleration(velocity, rotation, force):
	new_vx = velocity.x + math.cos(math.radians(rotation)) * force
	new_vy = velocity.y + math.sin(math.radians(rotation)) * force
	return vector2(x=new_vx, y=new_vy)


def distance(x1, y1, x2, y2):
	return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


class vector2:
	def __init__(self, **kwargs):
		self.x = kwargs.get('x')
		self.y = kwargs.get('y')

	def magnitude(self):
		return math.sqrt(self.x ** 2 + self.y ** 2)

	def normalized(self):
		return vector2(x=self.x / self.magnitude(), y=self.y / self.magnitude())

	def __iter__(self):
		return [self.x, self.y].__iter__()

	def __mul__(self, other):
		return vector2(x=self.x * other, y=self.y * other)
