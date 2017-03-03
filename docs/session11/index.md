# Session 11
> Snake tail on the grid

## Outline
1. Construct a square object which can draw itself.
2. 

#### Square class stub
```python
class Square:
	def __init__(self, x, y, size=GLOBAL_DEFAULT_SQUARE_SIZE):
		self.x = x
		self.y = y
		self.size = size
		
	def draw_me(self, canvas):
		pass
```

> The square should store its `(x,y)` coordinate and size. It should know how to convert the topleft point into a square on the canvas. If we take a minute and compose `SquareGrid` with a list of `Square`'s we can then use the `Square` class for the snake tail as well.

> Here is the `init_grid` function from the `SquareGrid` class
```python
    def init_grid(self, width, height):
        num_rows = self.NUM_ROWS
        num_cols = self.NUM_COLS
        grid_elements = []
        
        for x in range(num_rows):
            for y in range(num_cols):
                grid_elements.append((x+BASE_SHIFT_X,y+BASE_SHIFT_Y))
        return grid_elements
```

> The `tuple` that is saved in the `grid_elements` list is the data that we want to save in a our new `Square` class.
```python
(x+BASE_SHIFT_X,y+BASE_SHIFT_Y)
```


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

> Notice that it is doing two things. 1) looping over `body_segments`. 2) Printing `squares`. We want to push the printing responsibility to the `Square` object so the grid can focus on just looping over the list of `grid_elements`.

> Make the body of the four loop into the `draw_me` of the `Square` class.
```python
            x = pos[0] * size
            y = pos[1] * size
            canvas.draw_polygon(
                rect_coords(size, size, (x,y)),
                1, 'Green', 'Orange'
            )
```

> This chunk of code depends on `pos` and `size`. `pos` is the `(x, y)` data on the `Square` object. `size` is also data on the `Square` object.
