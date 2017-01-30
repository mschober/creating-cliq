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
