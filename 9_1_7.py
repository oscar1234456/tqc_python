c_line = 0
c_word = 0
c_char = 0
with open("read3.txt", "r") as file:
    line = file.readline()
    while line != "":
        c_line += 1
        print(line, end="")

        word = line.strip("\n").split(" ")
        c_word += len(word)

        for i in range(0,len(word)):
            c_char += len(word[i])
        line = file.readline()
print()
print("%d line(s)" % c_line)
print("%d word(s)" % c_word)
print("%d character(s)" % c_char)
