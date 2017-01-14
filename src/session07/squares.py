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

class Snake:
    def __init__(self, square):
        self.head = square
        self.snake_map = {}
        self.add(square)
    
    def add(self, square):
        point = square.point
        pos_key = "%s-%s" % (point[0], point[1])
        self.snake_map[pos_key] = square
        self.head = square
        
    def move_left(self):
        x = self.head.point[0] - 1
        y = self.head.point[1]
        new_square = Square((x,y), self.head.size)
        self.add(new_square)
      
home_square = Square((5, 5), 50)
the_snake = Snake(home_square)
  
def move(key):
    x = home_square.point[0]
    y = home_square.point[1]
    if keymap["left"] == key:
        the_snake.move_left()
    elif keymap["right"] == key:
        print "right"
    elif keymap["up"] == key:
        print "up"
    elif keymap["down"] == key:
        print "down"
    else :
        print "unused"

def draw(canvas):
    for square in the_snake.snake_map.values():
        square.draw(canvas)

    
frame = simplegui.create_frame("Home", 500, 500)
frame.set_draw_handler(draw)
frame.set_keydown_handler(move)
frame.start()

