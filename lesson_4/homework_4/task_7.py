from typing import Generator


def factorial(n: int) -> Generator:
    result = 1
    for i in range(1, n + 1):
        result *= i
        yield result


if __name__ == '__main__':
    for result in factorial(3):
        print(result)