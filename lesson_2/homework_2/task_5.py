rating = [10, 9, 8, 4, 3, 2, 1]

while True:
    print(rating)
    number = int(input("Enter integer number: "))

    if number in rating:
        index = rating.index(number)
        rating.insert(index + 1, number)
    else:
        rating.append(number)
        rating.sort(reverse=True)
