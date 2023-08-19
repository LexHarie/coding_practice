def reverse_string(string):
    list = []
    for i in range(len(string)):
        list.append(string[i])
    list.sort()
    new_string = "".join(words for words in list)
    return new_string

string = str(input("Please input any characters: "))

print(reverse_string(string))