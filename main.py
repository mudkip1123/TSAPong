import pyglet
from pyglet.window import key

import playerShip
import asteroid

win = pyglet.window.Window(width=800, height=600)
ball = playerShip.Ship(x=300, y=300)
a = asteroid.buildAsteroidField(ball)
#foll = objectFollower.Follower(target=ball, speed=80.0)
keys = key.KeyStateHandler()
win.push_handlers(keys)


def update(dt):
	ball.update(dt)
	for i in a:
		i.update(dt)
	#foll.update(dt)


def keyupdate():
	if keys[key.A]:
		ball.rotation += ball.turnSpeed
	if keys[key.D]:
		ball.rotation -= ball.turnSpeed
	if keys[key.S]:
		ball.vel *= .95
	ball.burning = keys[key.W]
	ball.shooting = keys[key.SPACE]


@win.event
def on_mouse_motion(x, y, dx, dy):
	ball.x = x
	ball.y = y


@win.event
def on_draw():
	win.clear()
	keyupdate()
	ball.draw()
	for i in a:
		i.draw()
	#foll.draw()

pyglet.clock.schedule_interval(update, 1. / 120.)
pyglet.app.run()