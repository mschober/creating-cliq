# Session09

# Reintroducing `Character` as a snake
> Now that we have a shiny new base, its time to starting snaking out into the world and collecting new squares. Lets leave velocities out for now so that we can figure out the game logic to leave the base, return to the base, identify when self collisions happen, and backfill the captured squares. Once all of this if figured out...we can turn velocities back on and start capturing!

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

