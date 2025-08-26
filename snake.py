import curses
import random
import time


"""Simple terminal-based snake game.

Use the arrow keys to move the snake and collect food. Press 'q' to quit.
"""


WINDOW_TIMEOUT = 100  # milliseconds


def create_food(snake, sh, sw):
    """Create a new piece of food not overlapping the snake."""
    while True:
        nf = [random.randint(1, sh - 2), random.randint(1, sw - 2)]
        if nf not in snake:
            return nf


def main(stdscr):
    curses.curs_set(0)
    sh, sw = stdscr.getmaxyx()
    window = curses.newwin(sh, sw, 0, 0)
    window.keypad(True)
    window.timeout(WINDOW_TIMEOUT)

    snk_x = sw // 4
    snk_y = sh // 2
    snake = [[snk_y, snk_x], [snk_y, snk_x - 1], [snk_y, snk_x - 2]]

    food = create_food(snake, sh, sw)
    window.addch(food[0], food[1], curses.ACS_PI)

    key = curses.KEY_RIGHT
    score = 0

    while True:
        next_key = window.getch()
        if next_key == ord("q"):
            break
        key = key if next_key == -1 else next_key

        head_y, head_x = snake[0]
        if (
            head_y in [0, sh - 1]
            or head_x in [0, sw - 1]
            or [head_y, head_x] in snake[1:]
        ):
            msg = f"Game Over! Score: {score}"
            window.addstr(sh // 2, sw // 2 - len(msg) // 2, msg)
            window.refresh()
            time.sleep(2)
            break

        new_head = [head_y, head_x]
        if key == curses.KEY_DOWN:
            new_head[0] += 1
        elif key == curses.KEY_UP:
            new_head[0] -= 1
        elif key == curses.KEY_LEFT:
            new_head[1] -= 1
        elif key == curses.KEY_RIGHT:
            new_head[1] += 1

        snake.insert(0, new_head)

        if snake[0] == food:
            score += 1
            food = create_food(snake, sh, sw)
            window.addch(food[0], food[1], curses.ACS_PI)
        else:
            tail = snake.pop()
            window.addch(tail[0], tail[1], " ")

        window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)


if __name__ == "__main__":
    curses.wrapper(main)
