from datetime import date
import inflect
import sys


p = inflect.engine()


def main():
    try:
        birth = input("Date of Birth: ")
        year, month, day = map(int, birth.split("-"))
        birthday = date(year, month, day)
    except ValueError:
        sys.exit("Invalid date")

    print(minutes_alive(birthday))


def minutes_alive(birthday):
    today = date.today()
    minutes = int((today - birthday).total_seconds() // 60)
    words = p.number_to_words(minutes, andword="")
    return f"{words.capitalize()} minutes"


if __name__ == "__main__":
    main()
