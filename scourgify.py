import csv
import sys


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    try:
        with open(sys.argv[1], "r", newline="") as infile:
            reader = csv.DictReader(infile)

            with open(sys.argv[2], "w", newline="") as outfile:
                fieldnames = ["first", "last", "house"]
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)

                writer.writeheader()

                for row in reader:
                    last, first = row["name"].split(", ")
                    writer.writerow({
                        "first": first,
                        "last": last,
                        "house": row["house"]
                    })

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


if __name__ == "__main__":
    main()
