from time import sleep
from random import randint
import colorama
from colorama import ansi, Style


from utils import load_sample

ALIVE_SYMBOL = Style.BRIGHT + '#'
DEAD_SYMBOL = ' '


def get_dead_state(width, height):
    return [[0 for _ in range(width)] for _ in range(height)]


def get_random_state(width, height):
    state = get_dead_state(width, height)
    for y in range(height):
        for x in range(width):
            state[y][x] = randint(0, 1)
    return state


def print_board_state(state):
    height, width = len(state), len(state[0])

    output_str = []
    for y in range(height):
        current_row = [ALIVE_SYMBOL if state[y][x] == 1 else DEAD_SYMBOL for x in range(width)]
        output_str.append(''.join(current_row))
    output_str = '\n'.join(output_str)
    print(output_str)


def get_next_state(current_state):
    height, width = len(current_state), len(current_state[0])
    next_state = get_dead_state(width, height)

    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]

    for y in range(height):
        for x in range(width):
            alive_neighbors = 0
            for direction in range(len(dy)):
                new_x = x + dx[direction]
                new_y = y + dy[direction]
                if new_x < 0 or new_x >= width:
                    continue
                if new_y < 0 or new_y >= height:
                    continue
                if current_state[new_y][new_x] == 1:
                    alive_neighbors += 1
            next_state[y][x] = 0
            if current_state[y][x] == 1:
                if alive_neighbors <= 1:
                    next_state[y][x] = 0
                elif alive_neighbors <= 3:
                    next_state[y][x] = 1
                else:
                    next_state[y][x] = 0
            elif alive_neighbors == 3:
                next_state[y][x] = 1
    return next_state


if __name__ == "__main__":
    colorama.init()

    # initial_state = load_sample('toad.txt')
    initial_state = get_random_state(150, 40)

    current_state = initial_state

    # Clear the screen before printing anything
    print(ansi.clear_screen())
    try:
        while True:
            print(ansi.Cursor.POS(1, 1))
            print_board_state(current_state)
            current_state = get_next_state(current_state)
            sleep(0.05)
    except KeyboardInterrupt as e:
        print(ansi.clear_screen())
