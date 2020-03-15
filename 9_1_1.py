with open("write.txt", "w") as file:
    i = 0
    while i < 5:
        file.write(input() + "\n")
        i += 1

