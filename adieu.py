from inflect import engine

p = engine()
names = []

try:
    while True:
        names.append(input("Name: "))
except EOFError:
    print()
    print("Adieu, adieu, to", p.join(names))
