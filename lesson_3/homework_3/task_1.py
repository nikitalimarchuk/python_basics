numbers = input("Enter 2 integer numbers separated with space: ")
numbers = [int(number) for number in numbers.split(" ")]


def divide_first_on_second(number_1: int, number_2: int) -> float:
    """Divides first number on second and return result in float type

    :param number_1: dividend integer number
    :param number_2: divider integer number. By default if 0 will return 0
    :return: result of dividing is float number"""

    if number_2:
        return number_1 / number_2
    else:
        return 0.0


if __name__ == '__main__':
    print(divide_first_on_second(*numbers))