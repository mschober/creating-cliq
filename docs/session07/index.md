# Session 07
> A grid to move on.

> Currently the movement of Cliq is based on pixels. In order to implement a splix.io grid movement shoud be based on square increments (e.g. move up 1 square, move left 2 squares, move down 1 square etc...). Two things need to happen to accomplish this type of grid movement. First, the screen must be on a grid system. Second, when a move instruction is given the closest row,col combination needs to be chosen.

## Constructing a Grid
> To construct the grid a square size that fits evenly in the screen dimensions needs to be selected. Then a 2D array needs to be built to represent rows and columns of the grid. Each cell (a row,col square in the grid) needs to be initialized with `is_highlighted=False`. Whenever a player consumes a free cell, `is_highlighted` will be flipped to `True`. When rendering the screen highlighted cells will be displayed.

### Creating a square from scratch
1. Open a new [codeskulptor](http://www.codeskulptor.org).
2. Search in the docs for `draw_polygon`.
3. Remove click me button, hello message text, and click function from skulptor.
4. Construct a backwards C shape to complete a square.
  - Identify the top left point (hint: [0,0])
  - Identify the rest of the points around the C based on that start point

![square](https://drive.google.com/uc?export=download&id=0B3SFnARVIcGLRDhkNWdYUHpmNjA)

### Creating a square anywhere
1. Add an import at the top to include the `random` module.
2. Recall that `random.randint(0,5)` would produce a random number between 0 and 5.
3. Given a square size of **50**.
   - How many squares will fit across?
   - How many squares will fit down?
4. Suppose you want to randomely choose a square to build in the 3rd row.
   - Instead of counting in pixels we'll count in integers based on which row,col we are in.
   - At the last minute when it is time to render the square we'll convert to pixel locations.
   - So what are the coordinates of the random square?
       - Y is easy => 2 (don't forget we are 0-based indexing!)
       - X is tougher => random from 0 to 9
         - Example square coordinates for start point: (3, 2)
         - [(3,2), (4,2), (4,3), (3,3)]
   - This doesn't explain how to actually paint the square though.
       - Loop over the points in the square
       - For each x and each y multiple by the size
         - [(150,100), (200,100), (200,150), (150,150)]
   - Here is some code that will get you started on the random_x square.

```python
class Square:
    def __init__(self, size, points):
        self.size = size
        self.points = self.to_pixels(points)
        
    def to_pixels(self, points):
        pass
    
    def draw(self, canvas):
        pass
        
rand_x = random.randint(0,9)
rando_square = Square(50,
    [
        (rand_x,2), (rand_x+1,2), (rand_x+1,3), (rand_x,3)
    ]
)

frame.set_draw_handler(rando_square.draw)
```
  
  * Is it hard to accomplish a random_x,random_y now?
 
## Picking the closest row,col on the grid
> Splix snakes follow a discrete path on the grid. Meaning you can't have a snake splitting the row or the column. When the direction is changed it has to be row or by column. 

### Animate the sqaure based on directional keys
> A small step towards using the grid is to move the square around the board using keys.

```python
import simplegui, time
import random
class Square:
    def __init__(self, size, points):
        self.size = size
        self.pixels = self.to_pixels(points)
        
    def to_pixels(self, points):
        pixels = []
        for point in points:
            npt = (
                point[0] * self.size, 
                point[1] * self.size)
            pixels.append(npt)
        return pixels
    
                   
    
    def draw(self, canvas):
        canvas.draw_polygon(self.pixels, 1, 'Blue', 'Green'
        )
    
grid = {}
x = random.randint(0,9)
y = random.randint(0,9)



def draw(canvas):
    for square in grid.values():
        square.draw(canvas)

KEY_TO_DIRECTION_MAP = {
    37: "left",
    38: "up",
    39: "right",
    40: "down"
}
        
DIRECTION_TO_KEY_MAP = {
    "left": 37,
    "up": 38,
    "right": 39,
    "down": 40
}
def move(key):
    global x
    global y
    def update_square(x,y):
        grid[str(x) + "-" + str(y)] = Square(50,
            [
                (x,y), (x+1,y), (x+1,y+1), (x,y+1)
            ]
        )
        print len(grid)
    if key == DIRECTION_TO_KEY_MAP["left"]:
        x = x -1
        y = y
        update_square(x,y)
    if key == DIRECTION_TO_KEY_MAP["up"]:
        x = x
        y = y - 1
        update_square(x,y)
    if key == DIRECTION_TO_KEY_MAP["right"]:
        x = x + 1
        y = y
        update_square(x,y)
    if key == DIRECTION_TO_KEY_MAP["down"]:
        x = x
        y = y + 1
        update_square(x,y)
    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 500, 500)
frame.set_draw_handler(draw)
frame.set_keydown_handler(move)

# Start the frame animation
frame.start()
```
