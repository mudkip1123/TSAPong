import pyglet

import load

win = pyglet.window.Window()

ball = pyglet.sprite.Sprite(img=load.ball_sprite)
ball.x = 300


def update(dt):
	ball.x += 1


@win.event
def on_draw():
	win.clear()
	ball.draw()

pyglet.clock.schedule_interval(update, 1 / 120.)
pyglet.app.run()