def solution(str1, str2, i, j):
    """
    递归求解
    :param str1:
    :param str2:
    :param i:
    :param j:
    :return:
    """
    if i == 0:
        return j
    if j == 0:
        return i
    # 如果末尾相同
    if str1[i - 1] == str2[j - 1]:
        return solution(str1, str2, i - 1, j - 1)
    # 如果末尾不同
    else:
        return min(solution(str1, str2, i - 1, j) + 1,
                   solution(str1, str2, i, j - 1) + 1,
                   solution(str1, str2, i - 1, j - 1) + 1)

if __name__ == '__main__':
    result = solution('abc', 'acbd', 3, 4)
    print(result)
