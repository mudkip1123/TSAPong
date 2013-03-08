import pyglet

win = pyglet.window.Window()


def update(dt):
	pass

@win.event
def on_draw():
	win.clear()

pyglet.clock.schedule_interval(update, 1 / 120.)
pyglet.app.run()