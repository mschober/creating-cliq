# Session 11
> Snake tail on the grid

#### Square class stub
```python
class Square:
	def __init__(self, x,y):
		self.x = x
		self.y = y
		
	def draw_me(self, canvas):
		pass
```

> The square should store its `(x,y)` coordinate and know how to convert the topleft point into a square on the canvas. We already accomplished this in the `SquareGrid` class. Initially we can cp/pst the code from that class, but we'll want to refactor the `SquareGrid` class to use `Square` objects.

> This is the `draw_me` from `SquareGrid`
```python
    def draw_me(self, canvas):
        size = self.SQUARE_PIXEL_SIZE
        for pos in self.grid_elements:
            x = pos[0] * size
            y = pos[1] * size
            canvas.draw_polygon(
                rect_coords(size, size, (x,y)),
                1, 'Green', 'Orange'
            )
```

> Notice that it is doing two things. 1) looping over `body_segments`. 2) Printing `squares`. Grab the printing squares piece and see if you can make it work down in the `draw_me` method of the `Square` class.
