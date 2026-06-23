months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    try:
        date = input("Date: ").strip()

        if "/" in date:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)

            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year:04}-{month:02}-{day:02}")
                break

        else:
            month, day, year = date.split()

            if not day.endswith(","):
                continue

            day = int(day.rstrip(","))

            if month in months and 1 <= day <= 31:
                month_num = months.index(month) + 1
                year = int(year)
                print(f"{year:04}-{month_num:02}-{day:02}")
                break

    except (ValueError, IndexError):
        pass
