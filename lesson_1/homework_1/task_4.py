number = 0

while number <= 0:
    number = int(input("Enter integer positive number: "))

number_string = str(number)
index = 0
length = len(number_string)
max = 0
min = 0

while index < length:
    current_number = int(number_string[index])
    if current_number > max:
        max = current_number
    if min == 0:
        min =current_number
    if current_number < min:
        min = current_number
    index += 1

print(f"Min: {min}")
print(f"Max: {max}")

