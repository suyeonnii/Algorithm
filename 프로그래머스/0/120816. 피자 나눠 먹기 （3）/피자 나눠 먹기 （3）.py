def solution(slice, n):
    answer = 0
    
    if slice >= n:
        answer=1
    else:
        answer=(n+slice-1)//slice
        
    return answer