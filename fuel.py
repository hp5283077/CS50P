def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)

    if x < 0 or y < 0:
        raise ValueError

    if y == 0:
        raise ZeroDivisionError

    if x > y:
        raise ValueError

    return round((x / y) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    return f"{percentage}%"


def main():
    while True:
        try:
            fraction = input("Fraction: ")
            print(gauge(convert(fraction)))
            break
        except (ValueError, ZeroDivisionError):
            pass


if __name__ == "__main__":
    main()
