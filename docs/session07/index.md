# Session 07
> A grid to move on.

> Currently the movement of Cliq is based on pixels. In order to implement a splix.io grid movement shoud be based on square increments (e.g. move up 1 square, move left 2 squares, move down 1 square etc...). Two things need to happen to accomplish this type of grid movement. First, the screen must be on a grid system. Second, when a move instruction is given the closest row,col combination needs to be chosen.

## Constructing a Grid
> To construct the grid a square size that fits evenly in the screen dimensions needs to be selected. Then a 2D array needs to be built to represent rows and columns of the grid. Each cell (a row,col square in the grid) needs to be initialized with `is_highlighted=False`. Whenever a player consumes a free cell, `is_highlighted` will be flipped to `True`. When rendering the screen highlighted cells will be displayed.

### Creating a square from scratch
1. Open a new [codeskulptor](http://www.codeskulptor.org).
2. Search in the docs for `draw_polygon`.
3. Remove button, hello message text from skulptor.
4. Construct a C shape to complete a square.
![square](https://drive.google.com/uc?export=download&id=0B3SFnARVIcGLTW1JVHNJczdudmM)

### Creating a square anywhere

### Creating a 2D grid of sqaures

## Picking the closest row,col on the grid
