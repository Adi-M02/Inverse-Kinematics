import pyglet
from pyglet.window import mouse

window = pyglet.window.Window()
@window.event
def on_mouse_press(x, y, button, modifiers):
    print(x,y)
@window.event
def on_draw():
    window.clear()
#run
pyglet.app.run()