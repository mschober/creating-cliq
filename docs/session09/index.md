# Session09

# Reintroducing `Character` as a snake
> Now that we have a shiny new base, its time to starting snaking out into the world and collecting new squares. Lets leave velocities out for now so that we can figure out the game logic to leave the base, return to the base, identify when self collisions happen, and backfill the captured squares. Once all of this if figured out...we can turn velocities back on and start capturing!

Code from [Session08](https://raw.githubusercontent.com/bellcodo/creating-cliq/master/src/session08/2_splix.io.py)

### Putting snake in the cage
> First order of business is to draw the snake head in the top-center square of the base. For this to happen the initial position needs to be shifted to that square, and the draw function needs to be re-enabled for the head. Lets begin by renaming `cliq` to `snake`.

A refresher on the state from last week

### Might look like this: clean grid
![clean grid](https://drive.google.com/uc?export=download&id=0B3SFnARVIcGLZ0FRemJYdWVfMHM)

* Diff of the code (after rename) [here](https://github.com/bellcodo/creating-cliq/commit/5538da81e5edf9ea2ec82fdc2dac694fcc04c698)

> Now that we've chosen a nice sensible name for our snake, its time to draw her again. For this we'll start by turning the draw methods back on, but to comment out the velocity drawing cliq just rename that method and create a new draw method with `pass` for the body.

```python
    def draw_me(self, canvas):
        pass
    
    def draw_me_2 (self, canvas):
```

* Diff of code [here](https://github.com/bellcodo/creating-cliq/commit/541c2e748126912b1a1f8039a7b91c27caa4516a)

> We need to do a little cleanup here. If you look through the code you'll see several copies of this block.

```python
            canvas.draw_circle(
                segment,
                self.circle_shape.radius /2,
                self.shape_attributes.line_width,
                self.shape_attributes.fill_color,
                self.shape_attributes.fill_color    
            )
```

> Refactor this into a new method on `snake` and reuse it in all its current places in the `draw_me_2` function. Note that you'll need to pass in a few parameters to make this work. Can you figure out what the parameters are? Here is what I came up with.

```python
    def draw_circle(self, canvas, center):
        canvas.draw_circle(
                center,
                self.circle_shape.radius /2,
                self.shape_attributes.line_width,
                self.shape_attributes.fill_color,
                self.shape_attributes.fill_color    
            )
```

> Now that the circle method is exposed in the class lets call it in the `draw_me` method.

```python
    def draw_me(self, canvas):
        self.draw_circle(canvas, self.circle_shape.center_point)
```

### Might look like this: tiny dot
![tiny dot](https://drive.google.com/uc?export=download&id=0B3SFnARVIcGLZWdTTWMzRmNpa1U)

* Diff of code [here](https://github.com/bellcodo/creating-cliq/commit/6e9f771de6acb341129c47d2daccd0a759ab3d42)

> To shift the dot over to the base, move it by square sizes to the beginning of the base. This is done by changing the circle center point by `(5*SIZE_OF_SQUARE,5*SIZE_OF_SQAURE)`.

### Might look like this: snake in cage
![snake in cage](https://drive.google.com/uc?export=download&id=0B3SFnARVIcGLaUpDemZ3TWswNUE)

* Diff of code [here](https://github.com/bellcodo/creating-cliq/commit/5da02a41a598d84b520ba706c501240f86d27bdf)

> There are `5`s floating around all about now, so lets create some constants to keep track of what the `5`s are for.

```python
IN_SQUARES = GLOBAL_DEFAULT_SQUARE_SIZE
BASE_SHIFT_X = 5
BASE_SHIFT_Y = 5
```

> Need to update the base drawing function.

```python
        for x in range(num_rows):
            for y in range(num_cols):
                grid_elements.append((x+BASE_SHIFT_X,y+BASE_SHIFT_Y))
        return grid_elements
```

> And finally updating the circle class.

```python
class Circle:
    
    START_POINT_X = BASE_SHIFT_X*IN_SQUARES
    START_POINT_Y = BASE_SHIFT_Y*IN_SQUARES
    
    def __init__ (self):
        x = self.START_POINT_X
        y = self.START_POINT_Y
        
        self.radius = 3
        self.center_point = (x,y)
```

* Diff of code [here](https://github.com/bellcodo/creating-cliq/commit/127e0d7006688a67df01256e8c3cfeda90f94536)

> The snake head should be the same size as the squares and snapped to the same grid. To begin lets refactor the radius constant into a class constant and global constant.

* New global constant
     - `GLOBAL_CIRCLE_RADIUS = 3`
* New class constant
     - `    RADIUS = GLOBAL_CIRCLE_RADIUS`
* Updated radius in `Circle` class
     - `        self.radius = self.RADIUS`

* Diff of code [here](https://github.com/bellcodo/creating-cliq/commit/fc12c88bfbb473de5c6557ff7d97ccc20d95f6b2)
> Uh-oh look closely at the above diff. There is an important additional change that was meant to come in the next change. The last edit removes the divide by `2` in the radius. Back when we were drawing `cliq` the body was decided to be half the size of the head. That divide by `2` was legacy from refactoring the draw method. We'll need to divide by `2` for the head to match the squares though because radius should be 1/2 the diameter. Lets do the division when creating the global constant instead of in the draw method.

* `GLOBAL_CIRCLE_RADIUS = GLOBAL_DEFAULT_SQUARE_SIZE / 2`

### Might look like this: big dot
![big dot](https://drive.google.com/uc?export=download&id=0B3SFnARVIcGLNHBBZFBKNHJpams)

* Diff of code [here](https://github.com/bellcodo/creating-cliq/commit/e6fbbf0a63978e291782f3709daed90d14dc8f17)

> To move the snake head into the grid its `center_point` needs to move half the width and half the height of the square.

```python
class Circle:
    
    START_POINT_X = BASE_SHIFT_X*IN_SQUARES + IN_SQUARES/2
    START_POINT_Y = BASE_SHIFT_Y*IN_SQUARES + IN_SQUARES/2
```

> And by refactoring we get

```python
class Circle:
    
    START_POINT_X = IN_SQUARES*(BASE_SHIFT_X + .5)
    START_POINT_Y = IN_SQUARES*(BASE_SHIFT_Y + .5)
```

### Might look like this: snake in grid
![snake in grid](https://drive.google.com/uc?export=download&id=0B3SFnARVIcGLQ1ZCcTZqcl9BWEE)

Diff of code [here](https://github.com/bellcodo/creating-cliq/commit/15a7c9b5db61006537fe402fa976d87ccd7363a0)

> With diligent refactoring and use of constants shifting the snake over to a nice starting position becomes super easy. Just add 4 sqaures to the initial `x` position of the head.

```python
    def __init__ (self):
        x = self.START_POINT_X + 4*IN_SQUARES
        y = self.START_POINT_Y
```

### Might look like this: snake in grid
![snake in grid](https://drive.google.com/uc?export=download&id=0B3SFnARVIcGLUmZDM3dMb1pOTmM)

Diff of code [here](https://github.com/bellcodo/creating-cliq/commit/33a844cf8a561b8ab1df4b612d32870c1e4bf75b)

> What happens if you try and increase the number of starting squares in the base? Lets double it and see. Change the constants to always be square and doulbed to `20`. Then run it and see what happens.

```python
GLOBAL_NUM_ROWS = 20
GLOBAL_NUM_COLS = GLOBAL_NUM_ROWS
```

### Might look like this: scaling didnt work
![scaling didnt work](https://drive.google.com/uc?export=download&id=0B3SFnARVIcGLM1BoWlBYTnNCS00)

> The snake head is in the wrong column now, and the base is shifted to the far lower corner. The snake start position is easy to fix so lets handle that first. 
* Find the middle of the base with division.
* Convert it to squares.

```python
class Circle:
    
    START_POINT_X = IN_SQUARES*(BASE_SHIFT_X + .5)
    START_POINT_Y = IN_SQUARES*(BASE_SHIFT_Y + .5)
    RADIUS = GLOBAL_CIRCLE_RADIUS
    
    def __init__ (self):
        start_in_middle_of_base = (GLOBAL_NUM_COLS / 2) - 1
        x = self.START_POINT_X + start_in_middle_of_base*IN_SQUARES
        y = self.START_POINT_Y
```

### Might look like this: fixed snake starting position
![fixed snake starting position](https://drive.google.com/uc?export=download&id=0B3SFnARVIcGLSnhjb3dtUk9PNXc)

> Since everything is going to be square it helps to just have the height always match the width.
```python
WINDOW_WIDTH = 500
WINDOW_HEIGHT = WINDOW_WIDTH
GLOBAL_DEFAULT_SQUARE_SIZE = 25
IN_SQUARES = GLOBAL_DEFAULT_SQUARE_SIZE
BASE_SHIFT_X = 5
BASE_SHIFT_Y = BASE_SHIFT_X
GLOBAL_CIRCLE_RADIUS = GLOBAL_DEFAULT_SQUARE_SIZE / 2
GLOBAL_NUM_ROWS = 20
GLOBAL_NUM_COLS = GLOBAL_NUM_ROWS
```

> The next part is difficult. We need to think for a minute about how to define the `x` & `y` shift in terms of the window width and base width. Create a new global constant that is the number of squares across.

```python
GLOBAL_SQUARES_ACROSS = WINDOW_WIDTH / GLOBAL_DEFAULT_SQUARE_SIZE
```

> To shift the base the proper distance in the `x` direction image cutting the base base columns out of the middle of the screen.

### Might look like this: shifting the base
![shifting the base](https://drive.google.com/uc?export=download&id=0B3SFnARVIcGLaWpWS09TZUliMk0)

* Diff of code [here](https://github.com/bellcodo/creating-cliq/commit/ea30b830a1a53f4df96d7e6edb19f2a9b8313ccd)

> After removing the middle of the base there are two pieces left over. You only want to shift the width of one of the pieces. Mathmatically this would be

```
(1/2) * (WINDOW_WIDTH_IN_SQUARES - BASE_WIDTH_IN_SQUARES)
```

> And in python we can create a constant for this as

```python
BASE_SHIFT_X = (GLOBAL_SQUARES_ACROSS - GLOBAL_NUM_ROWS) /2
BASE_SHIFT_Y = BASE_SHIFT_X
```

> We get the `y` direction for free because of choosing a square for the starting base. Try changing the window size and base size. The new constants should keep everything working.
