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
print(m)
print(permutation(9, m))