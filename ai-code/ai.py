import random


def generate_equation() -> str:
    """
    Generates a random equation.
    """
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    num3 = random.randint(1, 9)

    operator1 = random.choice(["+", "-", "*"])
    operator2 = random.choice(["+", "-", "*"])

    return str(num1) + operator1 + str(num2) + operator2 + str(num3)


def solve_equation(equation: str) -> int:
    """
    Solves the equation.
    """
    return str(int(eval(equation)))


def read_line():
    for line in open('in', 'rb', 0):
        yield line.decode().strip()


def input():
    return next(read_line())


role = input()
if role == 'giver':
    # We provide an equation first.
    equation = generate_equation()
    print(equation)
    for i in range(500):
        equation = input()
        print(solve_equation(equation))
        equation = generate_equation()
        print(equation)
elif role == 'solver':
    # We solve first
    equation = input()
    print(solve_equation(equation))
    for i in range(500):
        equation = generate_equation()
        print(equation)
        equation = input()
        print(solve_equation(equation))
