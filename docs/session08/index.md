# Session 08
> Snake on the grid.

> Now that grid movement has been established we need to consider how to construct a snake on the grid. You can think of a snake as a list of points in order. Every time the snake head moves the previous head needs to be added to the body. Every time the print loop runs, print ever segment in the body and print the head. 

## Reviewing last week
> Take a look at where we left off last week. Using the existing velocity snake we added a grid to the board. If you didn't get a chance to complete the entire grid or randomize it, you can see the working code as well. Navigate to last weeks code, select all and copy, paste into a new [codeskulptor](http://www.codeskulptor.org/).

#### [Last Weeks Code](from_last_week.md)

### Remove the grid and stop the snake
> Now that we can create squares on the screen we want to clear it up again and create a blank canvas. 

> Comment the following lines

```python
# cliq = Character()            
# grid = SquareGrid() 
```

```python
    if ticker == 3:
    #    cliq.save_me()    
        ticker = 0
    # cliq.draw_me(canvas)    # draw circle
    # grid.draw_me(canvas)    # draw grid
```

```python
    if ticker == 3:
    #    cliq.save_me()    
        ticker = 0
    # cliq.draw_me(canvas)    # draw circle
    # grid.draw_me(canvas)    # draw grid
```

```python
# frame.set_keydown_handler(cliq.move) #for move circle******
```
> Then run the program and there should be nothing on the screen and no errors.

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
