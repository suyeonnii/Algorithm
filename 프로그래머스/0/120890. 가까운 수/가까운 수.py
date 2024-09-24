def solution(array, n):
    answer = 0
    result=[]
    min_num=0
    ans_list=[]
    
    for i in array:
        result.append(abs(i-n))
        
    min_num=min(result)
    
    for i in range(len(result)):
        if result[i]==min_num:
            ans_list.append(array[i])
    
    answer=min(ans_list)
    
    return answer