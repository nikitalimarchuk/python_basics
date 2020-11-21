text = input("Enter some several words separated with space symbol: ")
words = text.split(" ")

for line_number in range(1, len(words) + 1):
    print(f"{line_number}. {words[line_number - 1][:11]}")