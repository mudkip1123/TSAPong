import pyglet

import load
import ballPhysics

win = pyglet.window.Window(width=800, height=600)

ball = ballPhysics.PhysicalBall(img=load.ball_sprite, x=300, y=300)

def update(dt):
	ball.update(dt)


@win.event
def on_draw():
	win.clear()
	ball.draw()

pyglet.clock.schedule_interval(update, 1. / 120.)
pyglet.app.run()