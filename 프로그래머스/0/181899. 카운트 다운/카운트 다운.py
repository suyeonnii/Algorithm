def solution(start, end_num):
    answer = []
    
    for num in range(end_num,start+1):
        answer.append(num)
        
    
    answer.sort(reverse=True)
    
    return answer