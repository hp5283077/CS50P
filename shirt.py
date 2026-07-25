import sys
from os.path import splitext
from PIL import Image, ImageOps


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_ext = splitext(sys.argv[1])[1].lower()
    output_ext = splitext(sys.argv[2])[1].lower()

    valid = [".jpg", ".jpeg", ".png"]

    if input_ext not in valid or output_ext not in valid:
        sys.exit("Invalid output")

    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    try:
        shirt = Image.open("shirt.png")
        image = Image.open(sys.argv[1])

        image = ImageOps.fit(image, shirt.size)
        image.paste(shirt, (0, 0), shirt)

        image.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
