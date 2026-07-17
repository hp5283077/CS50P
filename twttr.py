def shorten(word):
    result = ""
    for letter in word:
        if letter.lower() not in "aeiou":
            result += letter
    return result


def main():
    text = input("Input: ")
    print("Output:", shorten(text))


if __name__ == "__main__":
    main()
