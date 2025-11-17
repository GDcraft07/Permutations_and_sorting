massive = [5, 7, 3, 8, 2, 6, 9, 4, 1]

def sorting_simply_bubble(massive):
    switch = 0
    compare = 0

    for i in range(len(massive)):
        for j in range(len(massive) - (i + 1)):
            compare += 1
            if massive[j] > massive[j + 1]:
                switch += 1
                massive[j], massive[j + 1] = massive[j + 1], massive[j]
    return [massive, compare, switch]

# print(sorting_simply_bubble(massive))
# Количество сравнений: 36
# Количество перестановок: 21

def sorting_modify_bubble(massive):
    switch = 0
    compare = 0

    for i in range(len(massive)):
        flag = True
        for j in range(len(massive) - (i + 1)):
            compare += 1
            if massive[j] > massive[j + 1]:
                switch += 1
                massive[j], massive[j + 1] = massive[j + 1], massive[j]
                flag = False
        if flag:
            break
    
    return [massive, compare, switch]

# print(sorting_modify_bubble(massive))
# Количество сравнений: 36
# Количество перестановок: 21

def sorting_selet_max(massive):
    length = len(massive)
    switch = 0
    compare = 0

    for i in range(length - 1):
        maximum_index = 0

        for j in range(1, length - i):
            compare += 1
            if massive[j] > massive[maximum_index]:
                maximum_index = j
        
        switch += 1
        massive[maximum_index], massive[length - (i + 1)] = massive[length - (i + 1)], massive[maximum_index]
    
    return [massive, compare, switch]

# print(sorting_selet_max(massive))
# Количество сравнений: 36
# Количество перестановок: 8

def sorting_insert(massive):
    switch = 0
    compare = 0

    for i in range(1, len(massive)):
        element = massive[i]
        j = i - 1

        while j >= 0:
            compare += 1
            if massive[j] > element:
                massive[j + 1] = massive[j]
                j -= 1
                switch += 1
            
            else:
                break
        
        massive[j + 1] = element
    
    return [massive, compare, switch]

# print(sorting_insert(massive))
# Количество сравнений: 26
# Количество перестановок: 21

def sorting_quick(massive):
    if len(massive) < 2:
        return massive
    
    start = massive[0]
    low_elements = [i for i in massive[1:] if i < start]
    high_elements = [i for i in massive[1:] if i >= start]

    return sorting_quick(low_elements) + [start] + sorting_quick(high_elements)

# print(sorting_quick(massive))