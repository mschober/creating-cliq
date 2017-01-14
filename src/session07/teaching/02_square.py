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
    
