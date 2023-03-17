# SnakeGame

This is a simple implementation of the classic Snake Game using Pygame. The game features a snake that moves around the screen and eats randomly placed food, growing in length with each food eaten. The objective is to make the snake as long as possible without hitting the walls or running into its own body.

## How to Play

- Use the arrow keys to move the snake around the screen.
- The goal is to eat as many red apples as possible without running into the walls or the snake's own body.
- Every time you eat an apple, the snake gets longer and the game gets faster.
- The game ends when the snake hits the wall or its own body.

## Installation and Usage

1. Clone the repository to your local machine:

```bash
git clone https://github.com/aabasiyanik/SnakeGame.git
```
2. Navigate to the directory containing the game files:

```bash
cd SnakeGame
```
3. Install the required dependencies:
```bash
pip install pygame
```
## Customization

You can customize the game by modifying the following variables in the `snake.py` file:

```python
WIDTH = 600
HEIGHT = 600
CELL_SIZE = 20

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
```

- `WIDTH` and `HEIGHT` represent the dimensions of the game screen.
- `CELL_SIZE` represents the size of each block on the screen.
- `WHITE`, `GREEN`, and `RED` represent the colors used in the game.

You can modify these values to create your own custom version of the game.

## Credits
This game was made by **Ahmed Abasiyanik**. Feel free to use it, modify it, and share it with others!
