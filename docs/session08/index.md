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

### Might look like this: random grid
![random grid](https://drive.google.com/uc?export=download&id=0B3SFnARVIcGLUTdfeGpHUWt0SFU)

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

> Instead of using maps and lambdas, lets just loop for all the rows and all the columns. To do so create an outer loop of x and an inner loop for y.

```python
    def init_grid(self, width, height):
        grid_elements = []
        for x in range(10):
            for y in range(10):
                grid_elements.append((x,y))
        return grid_elements
```

### Might look like this: grid printed on top of itself
![grid printed on top of itself](https://drive.google.com/uc?export=download&id=0B3SFnARVIcGLZjRodENhQ0JqWjQ)

* Diff of the code [here](https://github.com/bellcodo/creating-cliq/commit/2160b0e0dc10cd7f235df5440894907c32aab626)

> The intention of the above loops is not to shift the square by 1 pixel each time through the loop, but instead shift it by an entire square each time through the loop. The easiest way to shift by 1 square instead of 1 pixel is to multiple x and y by the size of the square.

```python
    def init_grid(self, width, height):
        grid_elements = []
        for x in range(10):
            for y in range(10):
                grid_elements.append((x*50,y*50))
        return grid_elements
```

### Might look like this: paint the screen with squares
![paint the screen with squares](https://drive.google.com/uc?export=download&id=0B3SFnARVIcGLNjA5cU1oODk1SlE)

* Diff of the code [here](https://github.com/bellcodo/creating-cliq/commit/a6eed59a14511f28c654411bb9905fbee4ffbf9a)

> Let me diverge for a moment and comment on [code smells](https://martinfowler.com/bliki/CodeSmell.html) (and examples [here](https://sourcemaking.com/refactoring)). When you see something that doesn't quite sit right in your tummy, or is commonly an issue later it usually indicates a code smell. Code smells are early warning signs that you should do some [refactoring](http://wiki.c2.com/?WhatIsRefactoring) to clean them up. We identified a code smell above with the overly complex loops for the grid. Then we refactored to a simplier solution. Another code smell are the "magic numbers". Where are we getting 10 and 50 from? These number should be moved to constatns and passed in where necessary. Lets do another refactor to move them out of the code. This way we are not confused in the future with what they mean, and they can be easily changed everywhere.

### Refactoring to constants
> We'll do this in three steps. First, create local vairables in the method. Second, get the values for the local variables from class constants. Third, assign the class constants from global constants.

1. Create local vairables.

```python
    def init_grid(self, width, height):
        num_rows = 10
        num_cols = 10
        grid_elements = []
        
        size = 50
        
        for x in range(num_rows):
            for y in range(num_cols):
                grid_elements.append((x*size,y*size))
        return grid_elements
```

2. Local variables from class constants.
3. Class constants from global constants.


### Might look like this: paint the screen with squares
![paint the screen with squares](https://drive.google.com/uc?export=download&id=0B3SFnARVIcGLTDZ0OW9zNHc1bnM)

* Diff of the code [here](https://github.com/bellcodo/creating-cliq/commit/a6eed59a14511f28c654411bb9905fbee4ffbf9a)

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
