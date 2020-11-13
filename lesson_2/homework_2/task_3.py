month = int(input("Enter number of month: "))
months = {
             "Winter": (1, 2, 3),
             "Spring": (4, 5, 6),
             "Summer": (7, 8, 9),
             "Autumn": (10, 11, 12)
}

for name, numbers in months.items():
    if month in numbers:
        print(f"It is {name} now")
        break
