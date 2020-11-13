elements = input("Enter integer numbers splitted by space: ")
elements = elements.split(" ")
length = len(elements)
reversed_pairs = []

for i in range(0, length, 2):
    pair = elements[i: i + 2]
    pair.reverse()
    reversed_pairs.extend(pair)

print(reversed_pairs)
