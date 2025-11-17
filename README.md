Домашняя работа по дискретной математике. 

Выполнил: Зубов Константин ПМ-2502. 

 

№1 

В данной задачи нужно было реализовать алгоритм для генерации перестановок. Долгое время мне не приходила идея, как это можно реализовать. В моменте мне пришла идея рассмотреть индексы, на которых стоят числа в определенной перестановке. Например индексы каждого для перестановки {1, 2, 3}: 

1 - 0 0 1 2 1 2 

2 - 1 2 0 0 2 1 

3 - 2 1 2 1 0 0 

 

Для понимания возьмем 3 перестановку, в которой 1 - 1, 2 - 0, 3 - 2, это означает, что перестановка будет {2, 1, 3} 

Далее я заметил закономерность. 

Во-первых, в такой записи можно заметить ряд нулей равный    (n - 1)! и который находится на условной диагонали матрицы. 

Во-вторых, можно обратить внимание, что матрицу (n! x n) можно разбить на матрицы ((n - 1)! x 1). Вот как это будет выглядеть: 

1 - 0 0 1 2 1 2 

2 - 1 2 0 0 2 1 

3 - 2 1 2 1 0 0 

То есть условно матрицу можно разбить на n столбцов длинной (n - 1)!, каждый из которых будет состоять из элементов: 0 0, 1 2,  2 1. Так же можно заметить, что каждый последующий столбец отличается от предыдущего расположением 0 0. 

То есть нужно придумать алгоритм, который будет генерировать n-элементов(типа 0 0, 1 2,  2 1) и создавать n столбцов. 

Остается понять что такое 1 2,  2 1. Для этого я рассмотрел еще пару вариантов при n = 2 и n = 4. Получил следующее: 

n = 2: 

1 - 0 1 

2 - 1 0 

 

n = 4: 

1 - 0 0 0 0 0 0 1 1 2 3 2 3 1 1 2 3 2 3 1 1 2 3 2 3 

2 - 1 1 2 3 2 3 0 0 0 0 0 0 2 3 1 1 3 2 2 3 1 1 3 2 

3 - 2 3 1 1 3 2 2 3 1 1 3 2 0 0 0 0 0 0 3 2 3 2 1 1 

4 - 3 2 3 2 1 1 3 2 3 2 1 1 3 2 3 2 1 1 0 0 0 0 0 0 

 

Я обратил внимание, что элементы первого столбца длины         (n – 1)! под нулями при n = 3 равны: 

1 2 

2 1 

Что очень напоминает матрицу при n = 2, к каждому элементу которой добавили единицу.  

Действительно если рассмотреть элементы матрицы при n = 4 первого столбца под нулями: 

1 1 2 3 2 3 

2 3 1 1 3 2 

3 2 3 2 1 1 

 

Можно заметить те же сходства с матрицей n = 3. 

 

Т. е. мы нашли зависимость. В алгоритме я буду генерировать матрицы от 2 до n и для каждого последующей матрицы буду использовать предыдущую. Итак вот программа: 

 
```
def factor(n): 

    result = 1 

 

    for i in range(1, n + 1): 

        result *= i 

     

    return result 

 

 

def add_one(massive): 

    for i in range(len(massive)): 

        for j in range(len(massive[i])): 

            massive[i][j] += 1 

     

    return massive 

 

 

def join_massive(matrix): 

    result = [] 

 

    for i in range(len(matrix)): 

        row_result = [] 

 

        for j in range(len(matrix[i])): 

            row_result += matrix[i][j] 

 

        result += [row_result] 

     

    return result 

 

 

def transposed(matrix): 

    lens = len(matrix) 

    ans = [[[] for _ in range(lens)] for _ in range(lens)]   

 

    for i in range(lens):   

        for j in range(lens):   

            ans[j][i] = matrix[i][j] 

 

    return ans 

 

 

def permutation(number): 

    start_matrix = [[0, 1], [1, 0]] 

 

    for i in range(3, number + 1): 

        step_matrix = [[]] * i 

        zero_fill = [0] * (factor(i) // i) 

        enlarged_start_matrix = add_one(start_matrix) 

 

        for j in range(0, i): 

            step_matrix[j] = enlarged_start_matrix.copy() 

            step_matrix[j].insert(j, zero_fill) 

         

        start_matrix = join_massive(transposed(step_matrix)) 

     

    answer = [[0 for _ in range(len(start_matrix))] for _ in range(len(start_matrix[0]))] 

 

    for i in range(len(start_matrix)): 

        for j in range(len(start_matrix[i])): 

            answer[j][start_matrix[i][j]] = i + 1 

 

    for i in range(len(answer)): 

        print(' '.join(list(map(str, answer[i])))) 

 

number = int(input("(1, 2, ..., n) Введите n: ")) 

permutation(number) 
```
 

Проблема данного алгоритма в его скорости. Так как мы генерируем не только матрицу для n ни и для каждой предыдущей скорость алгоритма значительно ухудшается и равна O((n!)2).  

 

Алгоритм можно улучшить, например придумать как не использовать транспонирование при создании новой матрицы. Ну или как генерировать индексацию цифр по-другому. 

 

 

 

 

 

№ 2 

Для второй задачи я изменил только функцию permutation. Мой номер в БРС - 7. А значит k = 7, m = 188441. Заметим, что m не 188440, так как индексация в Python начинается с нуля, а значит 188440 элемент будет иметь индекс 188441. Код для второй задачи такой же как и в первой, но с измененным permutation: 

 
```
def permutation(number, m): 

    start_matrix = [[0, 1], [1, 0]] 

 

    for i in range(3, number + 1): 

        step_matrix = [[]] * i 

        zero_fill = [0] * (factor(i) // i) 

        enlarged_start_matrix = add_one(start_matrix) 

 

        for j in range(0, i): 

            step_matrix[j] = enlarged_start_matrix.copy() 

            step_matrix[j].insert(j, zero_fill) 

         

        start_matrix = join_massive(transposed(step_matrix)) 

     

    answer = [[0 for _ in range(len(start_matrix))] for _ in range(len(start_matrix[0]))] 

 

    for i in range(len(start_matrix)): 

        for j in range(len(start_matrix[i])): 

            answer[j][start_matrix[i][j]] = i + 1 

 

    return answer[m] 

 

k = 7 

m = factor(9) // 2 + 1000 * k + 1 

 

print(permutation(9, m)) 
```
 

Получим перестановку [5, 7, 3, 8, 2, 6, 9, 4, 1], которую далее будем использовать для алгоритмов сортировки. 

 

 

 

 

№ 3 

В данной задачи необходимо было реализовать алгоритмы сортировки. Мной было создано 5 вариантов: сортировка методом “пузырька”, сортировка методом “модифицированного пузырька”, сортировка методом “выбора максимума”, сортировка “вставками” и “быстрая сортировка”. 

Вот код для каждой сортировки: 

 
```
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

 

print(sorting_simply_bubble(massive)) 

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

 

print(sorting_modify_bubble(massive)) 

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

 

print(sorting_selet_max(massive)) 

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

 

print(sorting_insert(massive)) 

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
```
