# with open("te.txt","w") as infile:
#     infile.write("I am Apple!\n")
# with open("te.txt","a") as infile:
#     infile.write("I am Apple2!")
#
# with open("te.txt", "r") as outfile:
#     line = outfile.readline()
#     while line != "":
#         print(line,end="")
#         line = outfile.readline()

# with open("te.txt","w+") as file:
#     file.write("I love apple!\n")
#     file.write("I love apple2!")
#     file.seek(0,0)
#     line = file.read()
# print(line, end="")

import pickle
with open("te2.txt","wb") as file:
    pickle.dump(123,file)
    pickle.dump([1,2,3],file)
    pickle.dump({1,2,30},file)

with open("te2.txt","rb") as file:
    eof_end = False
    while not eof_end:
        try:
            print(pickle.load(file),end="")
        except EOFError:
            eof_end = True