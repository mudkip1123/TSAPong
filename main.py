import pyglet
from pyglet.window import key

import playerShip
import asteroid

win = pyglet.window.Window(width=800, height=600)
ball = playerShip.Ship(x=400, y=300, scale=10)
rocks = asteroid.buildAsteroidField(1)
keys = key.KeyStateHandler()
win.push_handlers(keys)

respawncounter = -1
level = 1
score = 0
lives = 3
score_text = pyglet.text.Label(text='', x=0, y=585)


def resetgame():
	global level, lives, score, respawncounter, rocks
	level = 1
	lives = 3
	score = 0
	ball.x = 10000
	respawncounter = 120
	rocks = []


def update(dt):
	global rocks, score, lives, level, respawncounter
	if respawncounter > 0:
		respawncounter -= 1
	elif respawncounter == 0:
		ball.reset()
		respawncounter = -1
	else:
		ball.update(dt)

	if lives == 0:
		resetgame()
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
			lives -= 1
			ball.x = 10000
			respawncounter = 60
	if not rocks:
		rocks = asteroid.buildAsteroidField(level)
		level += 1
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
def on_draw():
	win.clear()
	keyupdate()
	if respawncounter <= 0:
		ball.draw()
	score_text.draw()

	for i in range(lives):
		playerShip.Ship(scale=5, rotation=180, x=790 - (i * 20), y=590).draw()
	for i in rocks:
		i.draw()

pyglet.clock.schedule_interval(update, 1. / 120.)
pyglet.app.run()