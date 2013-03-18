import pyglet

import load
import ballPhysics
import objectFollower

win = pyglet.window.Window(width=800, height=600)
b = pyglet.graphics.Batch()

ball = ballPhysics.PhysicalBall(img=load.ball_sprite, batch=b)
ball.x = 300
ball.y = 300
foll = objectFollower.Follower(img=load.block_sprite, batch=b, target=ball, speed=80.0)
foll.vY = 10.0


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
	b.draw()
	ball.draw()

pyglet.clock.schedule_interval(update, 1. / 120.)
pyglet.app.run()