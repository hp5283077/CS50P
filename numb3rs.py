import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^([1-9]\d{0,2}|0)\.([1-9]\d{0,2}|0)\.([1-9]\d{0,2}|0)\.([1-9]\d{0,2}|0)$"

    if not re.fullmatch(pattern, ip):
        return False

    parts = ip.split(".")

    for part in parts:
        if int(part) > 255:
            return False

    return True


if __name__ == "__main__":
    main()
