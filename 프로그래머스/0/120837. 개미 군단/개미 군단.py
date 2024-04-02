def solution(hp):
    answer = 0
    rest=hp
    
    while rest>0:
        if rest > 5:
            answer+=rest//5
            rest%=5
        elif 3<= rest < 5:
            answer+=rest//3
            rest%=3
        else:
            answer+=rest//1
            rest%=1
    
    return answer