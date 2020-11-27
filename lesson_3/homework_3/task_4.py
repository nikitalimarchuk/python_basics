def my_fun_1(x, y):
    if not isinstance(x, float) or x <=0:
        raise ValueError("X is more then 0 and not float")
    if not isinstance(y, int) or y >= 0:
        raise ValueError("Y is less then 0 and not int")

    return x ** y


def my_fun_2(x, y):
    if not isinstance(x, float) or x <= 0:
        raise ValueError("X is more then 0 and not float")
    if not isinstance(y, int) or y >= 0:
        raise ValueError("Y is less then 0 and not int")

    result = x

    for _ in range(abs(y) + 1):
        result /= x

    return result


if __name__ == '__main__':
    print(my_fun_1(2.0, -2))
    print(my_fun_2(2.0, -2))
