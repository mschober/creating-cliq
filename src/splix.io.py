import simplegui

SIZE = 25
SNAKE_COLOR = ("Gold", "Purple")
WINDOW = (500,500)
LEFT = "LEFT"
UP = "UP"
RIGHT = "RIGHT"
DOWN = "DOWN"

KEYMAP = {
    LEFT: 37,
    RIGHT: 39,
    DOWN: 40,
    UP: 38
}

def square_coords_from_grid(size, grid_spot):
    x = grid_spot[0]
    y = grid_spot[1]
    points = [(x,y), (x+1,y), (x+1,y+1), (x,y+1)]
    scaled_points = map(lambda point:
                        (point[0]*size,point[1]*size), 
                        points)
    print scaled_points
    return scaled_points

class Square(object):
    def __init__(self, point, size, color=SNAKE_COLOR):
        self.size = size
        self.point = point
        self.points = square_coords_from_grid(size, point)
        self.color = color
    
    def draw(self, canvas):
        canvas.draw_polygon(
        self.points, 3, self.color[0], self.color[1]
    )

    def set_color(self, color):
        self.color = color
    
class Snake:
    def __init__(self, square):
        self.head = square
        self.snake_body = {}
        self.poly_points = []
    
    def add_to_body(self):
        point = self.head.point
        pos_key = "%s-%s" % (point[0], point[1])
        self.snake_body[pos_key] = self.head
        self.poly_points.append(map(lambda x: x*SIZE, point))        
        
    def update(self, new_point):
        x = self.head.point[0] + new_point[0]
        y = self.head.point[1] + new_point[1]
        self.head.point = (x,y)
        
    def move_left(self):
        self.add_to_body()
        self.update((-1,0))
        self.head = Square(self.head.point, self.head.size)
        
    def move_right(self):
        self.add_to_body()
        self.update((1,0))
        self.head = Square(self.head.point, self.head.size)
    
    def move_up(self):
        self.add_to_body()
        self.update((0,-1))
        self.head = Square(self.head.point, self.head.size)
        
    def move_down(self):
        self.add_to_body()
        self.update((0,1))
        self.head = Square(self.head.point, self.head.size)

    def draw(self, canvas):
        self.head.draw(canvas)
        for square in self.snake_body.values():
            square.draw(canvas)
        if self.poly_points:            
            canvas.draw_polygon(self.poly_points, 3, "Red")
        
        
    def get_position_key(self):
        pos_key = "%s-%s" % (self.head.point[0], self.head.point[1])
        return pos_key

class HomeBase:
    
    def __init__(self, start_pos, size):
        self.start_pos = start_pos
        self.home_base_map = {}
        self.fill_home_base(size)
    #(0,0)          (9,0)            (19,0)
    
    
    
   #            (4,4)            (14,4)
    
    
   #            (4,14)           (14,14)
    
    
    #(0,19)         (9,19)           (19,19)
    def add(self, square):
        point = square.point
        pos_key = "%s-%s" % (point[0], point[1])
        self.home_base_map[pos_key] = square
        
    def fill_home_base(self, size):
        sp = self.start_pos
        tl_x = (3 * sp[0])/4
        tl_y = (3 * sp[1])/4
        for x in range(size):
            for y in range(size):
                square = Square((x + tl_x, y + tl_y), SIZE)
                self.add(square)

    def draw(self, canvas):
        for square in self.home_base_map.values():
            square.draw(canvas)

home_base = HomeBase((10,10), 5)
home_square = Square((9, 7), SIZE)
the_snake = Snake(home_square)
  
def move(key):
    global the_snake
    the_snake.head.set_color(("Green", "Blue"))
    if KEYMAP[LEFT] == key:
        the_snake.move_left()
    elif KEYMAP[RIGHT] == key:
        the_snake.move_right()
    elif KEYMAP[UP] == key:
        the_snake.move_up()
    elif KEYMAP[DOWN] == key:
        the_snake.move_down()
    else :
        print "unused"
        
    position = the_snake.get_position_key()
    snake_keys = the_snake.snake_body.keys();
    if position in home_base.home_base_map.keys():
        print "The snake is in the base, creating a new snake"
        the_snake = Snake(the_snake.head)
    if position in the_snake.snake_body:
        print "found that snake!"
        
def draw(canvas):
    the_snake.draw(canvas)
    home_base.draw(canvas)
    
frame = simplegui.create_frame("Home", *WINDOW)
frame.set_draw_handler(draw)
frame.set_keydown_handler(move)
frame.start()
