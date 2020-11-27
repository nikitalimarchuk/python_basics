from itertools import cycle


counter = 0

for number in cycle((1, 2, 3, 4, 5)):
    if counter == 50:
        break
    print(number)
    counter += 1
