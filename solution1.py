def solution(str1, str2, i, j):
    if i == 0:
        return j
    if j == 0:
        return i
    
    if str1[i - 1] == str2[j - 1]:
        return solution(str1, str2, i - 1, j - 1)
    else:
        return min(solution(str1, str2, i - 1, j) + 1,
                   solution(str1, str2, i, j - 1) + 1,
                   solution(str1, str2, i - 1, j - 1) + 1)


result = solution('abc', 'acbd', 3, 4)
print(result)
