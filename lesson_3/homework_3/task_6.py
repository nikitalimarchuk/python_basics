def my_func(word: str) -> str:
    """Converts provided word in lowercase into the word with first letter
    in upper case

    :param word: word for conversation
    :return: word after conversation with first letter in uppercase"""

    return f"{word[0].upper()}{word[1: len(word)]}"


if __name__ == '__main__':
    words = input("Enter words separated by space: ").split(' ')
    print(" ".join([my_func(word) for word in words]))

