freq =eval(input())
word_dic = {}
with open("read4.txt", "r") as file:
    line = file.readline()
    while line != "":
        print(line, end="")
        word = line.strip("\n").split(" ")
        for s in word:
            if s not in word_dic:
                word_dic[s] = 1
            else:
                word_dic[s] += 1
        line = file.readline()

word_list = word_dic.items()
res = [words for (words, frequency) in word_list if frequency == freq ]

res.sort()
print()
for word in res:
    print(word)