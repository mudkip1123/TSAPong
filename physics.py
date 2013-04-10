import math


def ccw(A, B, C):
	return (C.y - A.y) * (B.x - A.x) > (B.y - A.y) * (C.x - A.x)


# Return true if line segments AB and CD intersect
def intersect(A, B, C, D):
	return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)


def revolve(pointsX, pointsY, rotation, dx=0, dy=0):
	coords = []
	for i in range(len(pointsX)):
		x = pointsX[i]
		y = pointsY[i]
		theta = math.radians(rotation)
		coords.append(x * math.cos(theta) - y * math.sin(theta) + dx)
		coords.append(x * math.sin(theta) + y * math.cos(theta) + dy)
	return coords


def addAcceleration(velocity, rotation, force):
	new_vx = velocity.x + math.cos(math.radians(rotation)) * force
	new_vy = velocity.y + math.sin(math.radians(rotation)) * force
	return vector2(x=new_vx, y=new_vy)


def distance(x1, y1, x2, y2):
	return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


class point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def pt(self):
		return [self.x, self.y]


class segment:
	def __init__(self, *args):
		if len(args) == 2:
			self.p1 = args[0]
			self.p2 = args[1]
		elif len(args) == 4:
			self.p1 = point(args[0], args[1])
			self.p2 = point(args[2], args[3])

	def inter(self, other):
		return intersect(self.p1, self.p2, other.p1, other.p2)

	def points(self):
		return [self.p1.x, self.p1.y, self.p2.x, self.p2.y]


class vector2:
	def __init__(self, **kwargs):
		self.x = kwargs.get('x')
		self.y = kwargs.get('y')

	def magnitude(self):
		return math.sqrt(self.x ** 2 + self.y ** 2)

	def normalized(self):
		return vector2(x=self.x / self.magnitude(), y=self.y / self.magnitude())

	def rotate(self, degrees):
		radians = math.radians(degrees)
		nx = math.cos(math.acos(self.normalized().x) + radians) * self.magnitude()
		ny = math.sin(math.asin(self.normalized().y) + radians) * self.magnitude()
		return vector2(x=nx, y=ny)

	def __iter__(self):
		return [self.x, self.y].__iter__()

	def __mul__(self, other):
		return vector2(x=self.x * other, y=self.y * other)
