def solution(num_list):
    sum_odd=0
    sum_even=0
    
    for i in range(0,len(num_list),2):
        sum_odd+=num_list[i]
    
    for i in range(1,len(num_list),2):
        sum_even+=num_list[i]
        
    if sum_odd>=sum_even:
        return sum_odd
    else:
        return sum_even