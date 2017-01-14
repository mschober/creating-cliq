import simplegui

# abstract the points based on the size

keymap = {
    "left": 37,
    "right": 39,
    "down": 40,
    "up": 38
}
        
class Square(object):
    def __init__(self, point, size):
        self.size = size
        self.point = point
        self.points = self.square_coords_from_grid(size, point)
    
    def square_coords_from_grid(self, size, grid_spot):
        x = grid_spot[0]
        y = grid_spot[1]
        points = [(x,y), (x+1,y), (x+1,y+1), (x,y+1)]
        scaled_points = map(lambda point:
                            (point[0]*size,point[1]*size), 
                        points)
        print scaled_points
        return scaled_points
    
    def draw(self, canvas):
        canvas.draw_polygon(
        self.points, 3, "Blue", "Green"  
    )
        
home_square = Square((0, 0), 50)

the_snake = {
    str(home_square.point[0]) + "-" + str(home_square.point[1]): home_square    
}

def draw(canvas):
    for square in the_snake.values():
        square.draw(canvas)

    
frame = simplegui.create_frame("Home", 500, 500)
frame.set_draw_handler(draw)
frame.set_keydown_handler(move)
frame.start()

