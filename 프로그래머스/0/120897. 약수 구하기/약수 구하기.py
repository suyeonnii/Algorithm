def solution(n):
    answer = []
    
    for i in range(1,n+1):
        if n%i==0:
            answer.append(i);
            i=+1;
        else:
            i=+1;
        
    return answer