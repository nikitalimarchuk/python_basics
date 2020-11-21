def my_func(number_1: int, number_2: int, number_3: int) -> int:
    """summarize 2 most bigger elements from provided in input arguments

    :param number_1: integer number for summarizing
    :param number_2: integer number for summarizing
    :param number_3: integer number for summarizing
    :return: result of summarizing 2 from 3 input arguments"""

    arguments = [number_1, number_2, number_3]

    if any(not isinstance(item, int)for item in arguments):
        raise ValueError

    max_1 = max(arguments)
    arguments.remove(max_1)
    max_2 = max(arguments)

    return max_1 + max_2

if __name__ == '__main__':
    print(my_func(1, 2, 3))