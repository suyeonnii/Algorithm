def solution(my_string, is_suffix):
    if len(my_string)<len(is_suffix):
        return 0
    
    for i in range(1,len(is_suffix)+1):
        if my_string[-i]!=is_suffix[-i]:
            return 0
    return 1