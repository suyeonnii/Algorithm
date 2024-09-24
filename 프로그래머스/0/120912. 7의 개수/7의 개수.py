def solution(array):
    answer = 0
    
    for i in array:
        ch=str(i)
        answer+=ch.count(str(7))
        
    return answer