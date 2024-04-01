def solution(num_list):
    answer = 0
    product=1
    squared_num=sum(num_list)**2
    
    for num in num_list:
        product*=num
    
    if product > squared_num:
        answer=0
    else:
        answer=1
        
    return answer