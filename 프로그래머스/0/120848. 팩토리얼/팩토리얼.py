def solution(n):
    answer=1
    factorial=1
    
    i =1
    
    while factorial<=n:
        answer=i
        i+=1
        factorial*=i
        
    return answer
    