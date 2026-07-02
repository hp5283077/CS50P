import emoji # pyright: ignore[reportMissingImports]

text = input("Input: ")
print(emoji.emojize(text, language="alias"))
