def solution(order):
    answer = 0
    
    for char in str(order):
        if char in ['3','6','9']:
            answer+=1
            
    return answer    