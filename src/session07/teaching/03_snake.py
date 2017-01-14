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
        
    def move_right(self):
        x = self.head.point[0] + 1
        y = self.head.point[1]
        new_square = Square((x,y), self.head.size)
        self.add(new_square)
    
    def move_up(self):
        x = self.head.point[0]
        y = self.head.point[1] -1
        new_square = Square((x,y), self.head.size)
        self.add(new_square)
    
    def move_down(self):
        x = self.head.point[0]
        y = self.head.point[1] +1
        new_square = Square((x,y), self.head.size)
        self.add(new_square)
