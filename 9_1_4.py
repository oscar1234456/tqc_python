data = []

with open("read2.txt", 'r')as file:
    line = file.readline()
    while line != "":
        print(line)
        tmp = line.strip("\n").split(" ")
        data += [[tmp[0], eval(tmp[1]), eval(tmp[2])]]
        line = file.readline()

sum_height = 0
sum_weight = 0
len_data = len(data)
height = []
weight = []
for i in range(0, len_data):
    sum_height += data[i][1]
    height += [data[i][1]]
    sum_weight += data[i][2]
    weight += [data[i][2]]

avg_height = sum_height / len_data
avg_weight = sum_weight / len_data
print("Average height: %.2f" % avg_height)
print("Average weight: %.2f" % avg_weight)

max_height = max(height)
max_weight = max(weight)
print("The tallest is %s with %.2f cm" % (data[height.index(max_height)][0], max_height))
print("The heaviest is %s with %.2f kg" % (data[weight.index(max_weight)][0], max_weight))
