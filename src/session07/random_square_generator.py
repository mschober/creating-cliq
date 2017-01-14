import simplegui, random

class Square:
    def __init__(self, size, points):
        self.size = size
        self.pixels = self.to_pixels(points)
        print self.pixels

    def to_points(self, pixels):
        pass
    
    def to_pixels(self, points):
        pixels = []
        for point in points:
            pixels.append(
                (point[0] * self.size, point[1] * self.size)
            )
        return pixels
    
    def draw(self, canvas):
        canvas.draw_polygon(self.pixels, 5, "Orange", "Aqua")

rand_x = random.randint(0,9)
rand_y = random.randint(0,9)
rando_square = Square(50,
    [
        (rand_x,rand_y), (rand_x+1,rand_y), (rand_x+1,rand_y+1), (rand_x,rand_y+1)
    ]
)

frame = simplegui.create_frame("Home", 500, 500)
frame.set_draw_handler(rando_square.draw)
frame.start()
