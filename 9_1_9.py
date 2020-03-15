import pickle
with open("phone.txt", "wb+") as file:
    i = 0
    while i < 5:
        line = input()
        pickle.dump(line+"\n", file)
        i += 1
    file.seek(0, 0)
    while True:
        try:
            print(pickle.load(file),end="")
        except EOFError:
            break