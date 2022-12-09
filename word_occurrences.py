"""Program to count the occurrences of words in a string"""


def main():
    """Get user input and count the occurrences of words."""
    sentence = input("Text: ")
    words = sentence.split()
    occurrences = {}
    for word in words:
        occurrences[word] = occurrences.get(word, 0) + 1

    words = list(occurrences.keys())
    words.sort()
    length = max(len(word) for word in words)
    for word in words:
        print(f"{word:<{length}} : {occurrences[word]}")


if __name__ == '__main__':
    main()
