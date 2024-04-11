def solution(n_str):
    idx=0
    
    for num in n_str:
        if num=='0':
            idx+=1
        else:
            break
    
    return n_str[idx:]