def solution(sides):
    a, b = sides
    min_len = abs(a - b) + 1
    max_len = a + b - 1
    return max_len - min_len + 1
