def solution(i, j, k):
    answer = 0
    
    for num in range(i,j+1):
        ch=str(num)
        
        answer+=ch.count(str(k))
            
    return answer