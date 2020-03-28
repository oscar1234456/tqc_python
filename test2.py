# lst = [1,2,3]
# print(lst)
# lst.append(5)
# print(lst)
# lst.insert(1, 6)
# print(lst)
# re = lst.remove(6)
# print(lst)
# print(re) #re不會有東西
# popitem = lst.pop()
# print(lst)
# print(popitem)
# popitem = lst.pop(1)
# print(lst)
# print(popitem)

# lst2 = [1,3,5,7,1,3,5,9]
# co = lst2.count(1)
# print(co)
# ind = lst2.index(3)
# print(ind)

# print(sorted(lst2))
# print(lst2)

# lst2.sort()
# print(lst2)

# lst2.reverse()
# print(lst2)

# print(3 in lst2)
# print(10 in lst2)
# print(sum(lst2))
# print(max(lst2))
# print(min(lst2))

# lst2 += [10,15,11]
# print(lst2)
# lst2.extend([900,1000,1001])
# print(lst2)
# lst2 *= 2
# print(lst2)

# lst1 = [1,2,3]
# lst2 = [1,3,2]
# print(lst1 == lst2)

# set1 = {1,2,3}
# set2 = set()

# set1.add(2)
# print(set1)
# set2.add(2)
# print(set2)
# set1.add(6)
# print(set1)
# set1.add(5)
# print(set1)  #set為外表無序，每次順序都可能不一樣

# set1.remove(2)
# print(set1)

# set3 = {"1","2"}
# print(set3)
# set3.add("A")
# print(set3)
# print(ord("A"), ord("1"), ord("2"))
# set3.add("3")
# print(set3)

# set4 = {1,2,3,4,5}
# set4.add(3)
# print(set4)
# print(sum(set4))
# print(len(set4))
# print(max(set4))
# print(min(set4))
# print(3 in set4)


# set4 = set([x for x in range(10)])
# print(set4)
# set5 = set((1, 5, 3,6,8,7,9,10)) 
# print(set5)
# set6 = {"a","c","b","g","e"}
# print(set6)
# print(sorted(set6))  #become list, set6.sort()不能用

# set1 = {2,4,6,1}
# set2 = {1,3,5,7,2}
# print(set1|set2)
# print(set1.union(set2))
# print(set1)

# print(set1&set2)
# print(set1.intersection(set2))
# print(set1)

# print(set1-set2)
# print(set1.difference(set2))
# print(set1)

# print(set1^set2)
# print(set1.symmetric_difference(set2))
# print(set1)

# set1 = {1,3,8,10}
# set2 = {1,3,8}

# print(set2.issubset(set1))
# print(set1.issuperset(set2))

# set1 = {1,2,3}
# set2 = {1,3,2}
# print(set1==set2)

# tuple1 = (1,2,3)
# print(tuple1)
# tuple2 = tuple([x for x in range(10) if x>=3])
# print(tuple2)
# tuple3 = tuple("python")
# print(tuple3)
# print(sum(tuple1))
# print(max(tuple1))
# print(min(tuple1))
# print(len(tuple1))

# tuple1 += (5,)
# print(tuple1)
# tuple1 += (5,6)
# print(tuple1)

# tuple1 *= 2
# print(tuple1)
# print(tuple1[2])
# print(tuple1[2:5])
# del tuple1 #print(tuple1)

# tuple3 = (1,2,3,4,5)
# print(2 in tuple3) # tuple3.sort()不能用
# print(sorted(tuple3)) # become list

# tuple1 = (1,2,3)
# tuple2 = (1,3,2)
# print(tuple1 == tuple2)

# tuple1 = (1,2,3) #tuple1.append(3)不行

# dict1 = {"key1":1, "key2":2, "key3":3}
# print(dict1["key1"])
# dict1["key4"] = 4
# print(dict1)

# dict1 = {"key1":1, "key3":3, "key2":2}
# print(dict1["key1"])
# dict1["key4"] = 4
# print(dict1)
# for key in dict1:
#     print("%s : %d" % (key, dict1[key]))

# dict1 = {"key1":1, "key2":5, "key3":3,"key3":3}
# print(dict1)
# dict1 = {"key1":1, "key2":5, "key3":3,"key4":3}
# print(dict1)
# print(len(dict1))
# print(max(dict1))  #print出key的尾端與前端
# print(min(dict1))

# dict1 = {1:1, 2:5, 3:3,4:3}
# print(max(dict1))  #print出key的尾端與前端
# print(min(dict1))

# dict1 = {"key1":1, "key2":5, "key3":3,"key4":3}
# dict2 = {"key1":1, "key2":5, "key3":3,"key5":3}
# print(dict1==dict2)
# del dict1["key4"] #dict1.remove("key4")不行
# print(dict1)
# print(dict1.pop("key3"))
# print(dict1) #is value
# print(dict1.popitem()) #is the item (tuple)
# print(dict1)
# dict1 = {"key1":1, "key2":5, "key3":3,"key4":3}
# print(dict1)
# dict1.clear()
# print(dict1)

# dict1 = {"key1":1, "key2":5, "key3":3,"key4":3}
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())

# print(list(dict1.keys()))
# print(list(dict1.values()))
# print(list(dict1.items()))

# print(tuple(dict1.keys()))
# print(tuple(dict1.values()))
# print(tuple(dict1.items()))

# dict1_item = list(dict1.items())
# for sumitem in dict1_item:
#     print("key: %5s  value: %3d" % (sumitem[0],sumitem[1]))

# dict1 = {"key1":1, "key2":5, "key3":3,"key4":3}
# dict2 = dict1.copy()
# print(dict2)
# dict2 = {"key1":1, "key2":6, "key3":3,"key4":3,"key5":10}
# dict1.update(dict2)
# print(dict1)

# str1 = str()
# print(type(str1))
# str1 = "ad'c"
# print(str1)
# print(len(str1))
# print(max(str1))
# print(min(str1))

# str2 = "python"
# print(str2[1:-3])
# str3 = str2+"123"
# print(str3)
# str4 = str3 * 2
# print(str4)

# print("y" in str2)
# print("q" in str2)
# print(str2<str3)

# for s in str3:
#     print(s)

# str1 = "python123@"
# print(str1.isalnum())
# str1 = "python123"
# print(str1.isalpha())
# str1 = "python"
# print(str1.isalpha())
# str1 = "python123"
# print(str1.isnumeric())
# str1 = "1232"
# print(str1.isnumeric())
# print(str1.isdigit())
# print(str1.isidentifier())
# str1 = "list"
# print(str1.isidentifier())
# print(str1.islower())
# print(str1.isupper())
# print(str1.isspace())
# str1 = ""
# print(str1.isspace())
# str1 = " "
# print(str1.isspace())

# str1 = "python3"
# print(str1.endswith("3"))
# print(str1.endswith("2"))
# print(str1.startswith("p"))
# str1 = "pytphon3"
# print(str1.find("p"))
# print(str1.rfind("p"))
# print(str1.count("p"))

# str1 = "python123 I like"
# print(str1.upper())
# print(str1)
# print(str1.lower())
# print(str1)
# print(str1.capitalize())
# print(str1)
# print(str1.title())
# print(str1)
# print(str1.swapcase())
# print(str1)
# print(str1.replace("py","SSS"))
# print(str1)

# str1 = "\nPython\n"
# print(str1)
# print(str1.strip("\n"),end="")

# str2 = "ppthonpp"
# print(str2.strip("p"))

# str3="apple banana grava"
# print(str3.split(" "))

# str1 = "python"
# print("|"+str1.center(10)+"|")
# print("|"+str1.ljust(10)+"|")
# print("|"+str1.rjust(10)+"|")

# print("%-5x" % 10)
# print("%-5o" % 10) #print(" %b" % 10)沒有
# print(format(10,"<5b"))

# print("%5x" % 10)
# print("%5o" % 10) #print(" %b" % 10)沒有
# print(format(10,">5b"))

# print("{:.^5d}".format(123))