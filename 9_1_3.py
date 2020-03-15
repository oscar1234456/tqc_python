with open("data.txt", "a+") as file:
    i = 0
    while i < 5:
        file.write(("\n" if i == 0 else "")+input() + ("\n" if i != 4 else ""))
        i += 1
    file.seek(2, 0)
    print(file.read(), end="")