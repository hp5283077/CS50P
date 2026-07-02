import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get(
        "https://api.coincap.io/v2/assets/bitcoin"
    )

    data = response.json()

    price = float(data["data"]["priceUsd"])

    total = n * price

    print(f"${total:,.4f}")

except requests.RequestException:
    sys.exit()
