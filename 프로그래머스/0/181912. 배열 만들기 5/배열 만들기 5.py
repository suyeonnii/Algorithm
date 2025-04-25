def solution(intStrs, k, s, l):
    answer = []
    for num_str in intStrs:
        num = int(num_str[s:s+l])
        if num > k:
            answer.append(num)
    return answer
