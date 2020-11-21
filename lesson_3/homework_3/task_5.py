import string

result = 0
flag = True

while flag is True:
    numbers = (input("Enter integer number separated with space: ")).split(" ")
    for number in numbers:
        for symbol in string.punctuation:
            if symbol in number:
                flag = False
        if flag:
            result += int(number)
    print(f"Result is: {result}")


