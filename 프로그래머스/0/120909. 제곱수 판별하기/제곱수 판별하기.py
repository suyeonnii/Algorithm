import math

def solution(n):
    answer = 0
    
    if math.sqrt(n) == int(math.sqrt(n)) and math.sqrt(n) >= 1:
        answer=1
    else:
        answer=2
    return answer