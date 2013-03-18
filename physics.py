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


def addAcceleration(dx, dy, rotation, force):
	dx += math.cos(math.radians(rotation)) * force
	dy += math.sin(math.radians(rotation)) * force
	return dx, dy