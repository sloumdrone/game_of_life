# game_of_life
This is a basic implementation of Conway's Game of Life. The `alt` folder contains an earlier procedural version. 
I didn't like the structure of the procedural version (too much arg passing or global variable usage), so updated
to the class based version in the main folder of the repo.

## controls

|  key  | effect |
|-------|--------|
| Q / q |  quit  |
| W / w |  toggle edge wrap on/off (default off) |
|   Up  |  speed up |
|  Down |  slow down |
| R / r |  new random seed |


## dependencies

On most systems this implementation should be available with just the Python3 standard library. It is possible
that some systems may need additional support for the `curses` library (I'm looking at you Windows). I can
vouch for it running fine on x86 Debian based GNU/Linux machines.

If you have trouble getting it to run, or the program cannot find Python3, simply call it with Python3
explicitly: `python3 ./life`. If that solves the issue, update the shebang in the `life` file. If you do
not know the path to your python3 implementation, try: `which python3`.
