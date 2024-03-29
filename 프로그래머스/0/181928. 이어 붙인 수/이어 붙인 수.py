def solution(num_list):
    answer = 0
    odd_num=[]
    even_num=[]
    
    for num in num_list:
        if num%2==0:
            even_num.append(str(num))
        else:
            odd_num.append(str(num))
        
        odd_str="".join(odd_num)
        even_str="".join(even_num)
        
    answer=int(odd_str)+int(even_str)       
    
    return answer