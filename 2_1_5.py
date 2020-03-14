word = input()

if "A" <= word <= "Z" or "a" <= word <= "z":
    print(word, "is an alphabet.")
elif "0" <= word <= "9":
    print(word, "is a number.")
else:
    print(word, "is a symbol.")



# if word.isalpha():
#     if word.isupper():
#         print(word,"is an UPPER alphabet.")
#     else:
#         print(word, "is an lower alphabet.")
# elif word.isnumeric():
#     print(word, "is a number.")
# else:
#     print(word, "is a symbol.")
