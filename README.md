# Free Python Games

**Free Python Games** is an Apache2 licensed collection of free Python games intended for education and fun. The games are written in simple Python code, making them easy to experiment with and customize. Simplified versions of classic arcade games are included, promoting learning through fun.

## Quickstart

### Installation
To install **Free Python Games**, use `pip`:
```bash
$ python3 -m pip install freegames
```
| Game    | Description                                                                                      | Changes Made                                        | Commands to Run                    |
|---------|--------------------------------------------------------------------------------------------------|-----------------------------------------------------|------------------------------------|
| Paint   | Draw lines and shapes. Click to start and end shapes, select colors with keys.                   | Added PURPLE, circle, rectangle, and triangle tools | `python3 paint.py`                 |
| Snake   | Navigate, eat food to grow, avoid self and walls.                                                | Random food, color changes each run                 | `python3 snake.py`                 |
| Pacman  | Navigate maze, eat food, avoid ghosts.                                                           | Smarter ghosts, modified maze, faster ghosts        | `python3 pacman.py`                |
| Cannon  | Fire cannonballs to pop balloons before they cross the screen.                                   | Faster cannon, infinite run                         | `python3 cannon.py`                |
| Memory  | Match number pairs to clear tiles.                                                               | Added tap counter, tap detection, letters in data   | `python3 memory.py`                |

## Additional Libraries

Some games may require additional libraries to enhance functionality, such as `random` and `turtle` for random movements and drawing capabilities:

```python
from random import *
from turtle import *
from freegames import floor, vector, choice

