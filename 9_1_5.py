fileName = input()
s = input()
sentence = []
with open(fileName, 'r+') as file:
    print("===Before the deletion")
    line = file.readline()
    while line != "":
        print(line, end="")
        sentence += [line]
        line = file.readline()

    for i in range(0,len(sentence)):
        sentence[i] = sentence[i].replace(s, "")

    file.seek(0, 0)
    file.truncate()
    for i in range(0, len(sentence)):
        file.write(sentence[i])
    file.seek(0, 0)

    print("===After the deletion")
    line = file.readline()
    while line != "":
        print(line, end="")
        line = file.readline()