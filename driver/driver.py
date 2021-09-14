from models import *
from io import TextIOWrapper
import os

game = Game(GameInitiator.PLAYER_1, Player(
    Language.PYTHON), Player(Language.PYTHON))


def is_valid(equation: str):
    if not equation.replace(' ', '').replace('+', '').replace('-', '').replace('*', '').replace('/', '').isdigit():  # noqa
        return False
    try:
        eval(equation)
        return True
    except Exception:
        return False


def get_line_from_player1():
    for line in open('/fifos/player1/out', 'rb', 0):
        yield line.decode().strip()


def get_line_from_player2(fifo: str):
    for line in open(fifo, 'rb', 0):
        yield line.decode().strip()


def get_line_from(fifo: str):
    return next(get_line_from_player1(fifo))


def write_line_to(fifo: str, line: str):
    os.write(os.open(fifo, os.O_WRONLY), line.encode() + b'\n')


def play_turn(giver_input: str,
              giver_output: TextIOWrapper,
              solver_input: str,
              solver_output: TextIOWrapper,
              score):
    giver_score, solver_score = score
    equation = get_line_from(giver_output)
    print('Got equation', equation)
    if not is_valid(equation):
        giver_score -= 1
        equation = '1'
    expected_answer = eval(equation)
    print('Expecting answer', expected_answer)
    write_line_to(solver_input, equation)
    answer = get_line_from(solver_output)
    print('Got answer', answer)
    if int(answer) == int(expected_answer):
        solver_score += 1
    else:
        giver_score += 1
        solver_score -= 1
    return (giver_score, solver_score)


print(os.listdir('/'))
print(os.listdir('/fifos'))
print(os.listdir('/fifos/player1'))

player1_input = '/fifos/player1/in'
player1_output = '/fifos/player1/out'
player2_input = '/fifos/player2/in'
player2_output = '/fifos/player2/out'

scores = 0, 0

write_line_to(player1_input, 'giver')
print('Role sent to player 1')
write_line_to(player2_input, 'solver')
print('Role sent to player 2')
print()

for i in range(500):
    print(scores)
    print()
    print('Player 1 gives:')
    (player1_score, player2_score) = play_turn(
        player1_input, player1_output, player2_input, player2_output, scores
    )
    scores = player1_score, player2_score
    print()
    print(scores)
    print()
    print('Player 2 gives:')
    (player2_score, player1_score) = play_turn(
        player2_input, player2_output, player1_input, player1_output, scores
    )
    scores = player1_score, player2_score

    print()

print(scores)
