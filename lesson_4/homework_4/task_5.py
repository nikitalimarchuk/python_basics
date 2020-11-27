from functools import reduce

# super_list = (item for item in range(1, 5)) # 24
sequence_generator = (item for item in range(100, 1001))
print(reduce(lambda first, next: first * next, sequence_generator))
