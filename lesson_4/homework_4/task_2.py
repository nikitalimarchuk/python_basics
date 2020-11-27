def my_gen():
    previous = 300
    for number in [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]:
        if number > previous:
            yield number
        previous = number

gen = my_gen()
items = []

for item in gen:
    items.append(item)

print(items)