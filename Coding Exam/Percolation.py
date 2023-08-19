import numpy as np

string = "0"

def percolation(string):
    if string == "1":
        return "Yes"
    elif string == "0":
        return "No"
    number_of_rows = 0
    for i in range(len(string)):
        array = []
        if string[i] == ";":
            number_of_rows += 1
        for i in range(number_of_rows):
            array.append([])

    list = []
    new_array = []
    for i in range(len(string)):
        if string[i] == '1':
            list.append(int(string[i]))
        elif string[i] == '0':
            list.append(int(string[i]))

    for i in range(0, len(list), 5):
        new_array.append(list[i : i + 5])
            

    position = 0
    new_position = 0
    list = []
    for i in range(len(new_array)):
        for x in range(len(new_array[i])):
            if new_array[i][x] == 1:
                position = x
                list.append(position)
    yes = ''

    look = [1, 0 , -1]
    no_list = []

    for i in range(len(list) - 1):
        if (list[i + 1] - list[i]) in look:
            no_list.append('yes')
        else:
            no_list.append('no')

    if 'no' in no_list:
        return "No"
    else:
        return "Yes"

print(percolation(string))  

                    