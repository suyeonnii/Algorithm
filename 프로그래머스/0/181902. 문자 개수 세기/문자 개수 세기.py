def solution(my_string):
    count = [0] * 52
    for ch in my_string:
        if 'A' <= ch <= 'Z':
            count[ord(ch) - ord('A')] += 1
        elif 'a' <= ch <= 'z':
            count[ord(ch) - ord('a') + 26] += 1
    return count