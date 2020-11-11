number = input("Enter integer number: ")
amount_of_duplication = int(input("Enter number of duplication: "))
numbers = []

for _ in range(1, amount_of_duplication + 1):
    numbers.append(number * _)

result = sum([int(number) for number in numbers])
print(f"{' + '.join(numbers)} = {result}")
