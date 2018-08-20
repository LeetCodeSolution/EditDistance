def solution(str1, str2):
    str1_length = len(str1)
    str2_length = len(str2)
    
    matrix = [[0 for _ in range(str2_length)] for _ in range(str1_length)]
    
    print(matrix)
    
    for i in range(str1_length):
        matrix[i][0] = i
    for j in range(str2_length):
        matrix[0][j] = j
    print(matrix)
    
    for i in range(1, str1_length):
        for j in range(1, str2_length):
            if str1[i] == str2[j]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                matrix[i][j] = min(matrix[i - 1][j] + 1,
                                   matrix[i][j - 1] + 1,
                                   matrix[i - 1][j - 1] + 1)
    
    return matrix[-1][-1]


result = solution('bcd', 'abcde')
print(result)
