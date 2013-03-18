import pyglet

win = pyglet.window.Window(width=800, height=600)
b = pyglet.graphics.Batch()


def update(dt):
	pass


class point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.p = [x, y]

	def __iter__(self):
		return self.p.__iter__()


class segment:
	def __init__(self, x1, y1, x2, y2):
		self.p1 = point(x1, y1)
		self.p2 = point(x2, y2)
		self.points = self.p1.p + self.p2.p

	def __iter__(self):
		return self.points.__iter__()

stat = segment(100., 300., 400., 80.)


def ccw(A, B, C):
	return (C.y - A.y) * (B.x - A.x) > (B.y - A.y) * (C.x - A.x)


# Return true if line segments AB and CD intersect
def intersect(A, B, C, D):
	return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)


@win.event
def on_draw():
	win.clear()
	dyn = segment(10., 10., win._mouse_x, win._mouse_y)
	
	pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
		('v2f', tuple(stat)))
	pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
		('v2f', tuple(dyn)))
	print intersect(dyn.p1, dyn.p2, stat.p1, stat.p2)


pyglet.clock.schedule_interval(update, 1. / 120.)
pyglet.app.run()