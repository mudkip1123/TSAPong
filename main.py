import pyglet
from pyglet.window import key

import playerShip
import asteroid

win = pyglet.window.Window(width=800, height=600)
ball = playerShip.Ship(x=400, y=300, scale=10)
rocks = asteroid.buildAsteroidField(3)
keys = key.KeyStateHandler()
win.push_handlers(keys)

score = 0
lives = 3
score_text = pyglet.text.Label(text='', x=0, y=590)


def update(dt):
	global rocks, score
	ball.update(dt)
	for i in rocks:
		i.update(dt)

	for shot in ball.rounds:
		for rock in rocks:
			if rock is not None and shot.collide(rock):
				ball.rounds.remove(shot)
				c, b = rock.die()
				rocks.append(b)
				rocks.append(c)
				rocks.remove(rock)
				score += 10
				break

	rocks = [i for i in rocks if i is not None]
	for rock in rocks:
		if ball.collide(rock):
			pass
	score_text.text = str(score)


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
	score_text.draw()

	for i in range(lives):
		playerShip.Ship(scale=5, rotation=180, x=790 - (i * 20), y=590).draw()
	for i in rocks:
		i.draw()

pyglet.clock.schedule_interval(update, 1. / 120.)
pyglet.app.run()