class SquareGrid:

    def __init__(self):
        self.grid_elements = self.init_grid(
            WINDOW_WIDTH,
            WINDOW_HEIGHT
        )
        
    def init_grid(self, width, height):
        grid_elements = []
        for pos in range(random.randint(0,99)):
            grid_elements.append(
                tuple(
                    map(lambda x: x * 50, (random.randint(0,9), random.randint(0,9)))
                )
            )
        return grid_elements
    
    def draw_me(self, canvas):
        size = 50
        for pos in self.grid_elements:
            x = pos[0]
            y = pos[1]
            canvas.draw_polygon(
                [
                    (x, y),
                    ((x+size), y),
                    ((x+size), (y+size)),
                    (x, (y+size))
                ], 1, 'Green', 'Orange'
            )

