def is_valid(s):

    if len(s) < 2 or len(s) > 6:
        return False


    if not s[:2].isalpha():
        return False

    number_started = False

    for char in s[2:]:
        if char.isdigit():
            if not number_started:

                if char == "0":
                    return False
                number_started = True
        else:
            if number_started:
                
                return False
            if not char.isalpha():
                return False

    return True


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
