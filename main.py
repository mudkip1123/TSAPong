import pyglet

import ballPhysics
import objectFollower

win = pyglet.window.Window(width=800, height=600)
b = pyglet.graphics.Batch()

ball = ballPhysics.PhysicalBall(x=300, y=300)
foll = objectFollower.Follower(target=ball, speed=80.0)


def update(dt):
	ball.update(dt)
	foll.update(dt)


@win.event
def on_key_press(symbol, modifier):
	pass


@win.event
def on_mouse_motion(x, y, dx, dy):
	ball.x = x
	ball.y = y


@win.event
def on_draw():
	win.clear()
	ball.draw()
	foll.draw()

pyglet.clock.schedule_interval(update, 1. / 120.)
pyglet.app.run()