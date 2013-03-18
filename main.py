import pyglet
from pyglet.window import key

import ballPhysics
import objectFollower

win = pyglet.window.Window(width=800, height=600)
ball = ballPhysics.PhysicalBall(x=300, y=300)
foll = objectFollower.Follower(target=ball, speed=80.0)
keys = key.KeyStateHandler()
win.push_handlers(keys)


def update(dt):
	ball.update(dt)
	foll.update(dt)


def keyupdate():
	if keys[key.A]:
		ball.rotation += 5
	if keys[key.D]:
		ball.rotation -= 5
	if keys[key.W]:
		ball.pedal()
	if keys[key.S]:
		ball.dx *= .95
		ball.dy *= .95


@win.event
def on_mouse_motion(x, y, dx, dy):
	ball.x = x
	ball.y = y


@win.event
def on_draw():
	win.clear()
	keyupdate()
	ball.draw()
	foll.draw()

pyglet.clock.schedule_interval(update, 1. / 120.)
pyglet.app.run()