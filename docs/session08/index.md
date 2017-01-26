# Session 08
> Snake on the grid.

> We've played around with many concepts that will fit together to make splix.io happen. Assigning velocity to a shape, keeping track of its previous positions, let the player control the direction with keydown handlers. Soon it will be time to take a step back and start designing how the final game will be constructed. But first we need to formalize the efforts on using the grid to build a homebase, as well as enforce of the snake on a grid instead of for any pixel. Lets begin by getting a fresh copy of last weeks code.

## Reviewing last week
> Take a look at where we left off last week. Using the existing velocity snake we added a grid to the board. If you didn't get a chance to complete the entire grid or randomize it, you can see the working code as well. Navigate to last weeks code, select all and copy, paste into a new [codeskulptor](http://www.codeskulptor.org/).

#### [Last Weeks Code](from_last_week.md)

### Stopping the snake
> The constantly moving snake will be distracting while we work on creating a homebase square.

> Comment the following lines

```python
# cliq = Character()            
```

```python
    if ticker == 3:
    #    cliq.save_me()    
        ticker = 0
    # cliq.draw_me(canvas)    # draw circle
```

```python
# frame.set_keydown_handler(cliq.move) #for move circle******
```
> Then run the program and there should be just a grid on the screen and no errors.
* A diff of the code is [here](https://github.com/bellcodo/creating-cliq/commit/68eb14b7d80d20be96aa9ae07f1fb2a08d0aac59)

> The grid initialization from last week is difficult to understand, lets simplify it as our first change.

```python
    def init_grid(self, width, height):
        grid_elements = []
        for pos in range(random.randint(0,99)):
            grid_elements.append(
                tuple(
                    map(lambda x: x * 50, (random.randint(0,9), random.randint(0,9)))
                )
            )
        return grid_elements
```

### Might look like this
![random grid](https://drive.google.com/uc?export=download&id=0B3SFnARVIcGLUTdfeGpHUWt0SFU)

> Instead of using maps and lambdas, lets just loop for all the rows and all the columns. To do so create an outer loop of x and an inner loop for y.

```python
    def init_grid(self, width, height):
        grid_elements = []
        for x in range(10):
            for y in range(10):
                grid_elements.append((x,y))
        return grid_elements
```

### Might look like this
![random grid](https://drive.google.com/uc?export=download&id=0B3SFnARVIcGLZjRodENhQ0JqWjQ)

#### Adding a base object
> Create the base object template.

```python
class HomeBase:
    
    def __init__(self):
        self.base_map = self.init_base((0,0), 10)
    
    def init_base(self, start_pos, size):
        pass
    
    def draw_me(self, canvas):
        pass
```

* Create a base

```python
base = HomeBase()
```

* Draw the base in the global draw method

```python
base.draw_me(canvas)
```

* Create a square class and add points to the map
```python
class Square:
    
    DEFAULT_SIZE = 15
    def __init__(self, top_left_point):
        (x,y) = top_left_point
        self.points = rect_coords(
            self.DEFAULT_SIZE,
            self.DEFAULT_SIZE,
            (x,y)
        )
                
class HomeBase:
    
    def __init__(self):
        self.base_map = self.init_base((0,0), 10)
    
    def init_base(self, start_pos, size):
        base_map = {}
        for x in range(size):
            for y in range(size):
                element_key = self.create_key((x,y))
                base_map[element_key] = Square((x,y))
        return base_map
    
    def create_key(self, top_left_point):
        (x,y) = top_left_point
        return "%s-%s" % (x,y)
    
    def draw_me(self, canvas):
        points = self.base_map["0-0"].points
        canvas.draw_polygon(
            points,
            3,
            "Red",
            "Blue"
        )
```

> If you are super on top of it, you'll notice that `rect_coords` handles giving you back the 4 points in the square, but each iteration through the loop we are only increment the x and y by 1 instead of by the size of the square. This will result in squares printing on top of eachother. To solve this problem the squares top left point needs to be shifted by the size of the square before calculating the rectangular coordinates. This can be done in the square class.

### Shifting squares in the base
> 
