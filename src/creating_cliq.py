import simplegui

class Circle:
    def __init__(self):
        self.center_point = (100,100)
        self.radius = 10

class ShapeAttribute:
    pass

class Cliq:
    def __init__(self):
        self.circle_shape = Circle()
        self.shape_attributes = ShapeAttribute()

cliq = Cliq()

def draw(canvas):
    pass

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 500, 500)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
