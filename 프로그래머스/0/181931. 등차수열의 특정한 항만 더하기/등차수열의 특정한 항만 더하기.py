def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        term = a + d * i 
        if included[i]:
            answer += term
    return answer
