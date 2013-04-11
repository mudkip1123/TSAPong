import pyglet
from pyglet.window import key

import playerShip
import asteroid

win = pyglet.window.Window(width=800, height=600)
ball = playerShip.Ship(x=400, y=300)
a = asteroid.buildAsteroidField()
keys = key.KeyStateHandler()
win.push_handlers(keys)
score = 0


def update(dt):
	global a, score
	ball.update(dt)
	for i in a:
		i.update(dt)

	for shot in ball.rounds:
		for asteroid in a:
			if asteroid is not None and shot.collide(asteroid):
				ball.rounds.remove(shot)
				c, b = asteroid.die()
				a.append(b)
				a.append(c)
				a.remove(asteroid)
				score += 10
				break

	a = [i for i in a if i is not None]
	for asteroid in a:
		if ball.collide(asteroid):
			pass



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

pyglet.clock.schedule_interval(update, 1. / 120.)
pyglet.app.run()