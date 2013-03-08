import pyglet

pyglet.resource.path = ['res']
pyglet.resource.reindex()


def center_anchor(image):
	image.anchor_x = image.width / 2
	image.anchor_y = image.height / 2

ball_sprite = pyglet.resource.image("ballBlue.png")
paddle_sprite = pyglet.resource.image("paddleBlu.png")
block_sprite = pyglet.resource.image("element_red_rectangle.png")

center_anchor(ball_sprite)
center_anchor(paddle_sprite)
center_anchor(block_sprite)
