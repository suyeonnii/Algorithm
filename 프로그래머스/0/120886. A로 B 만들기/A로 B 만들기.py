def solution(before, after):
    answer = 0
    
    list_before=list(before)
    list_after=list(after)
    
    if sorted(list_before)==sorted(list_after):
        answer=1
    else:
        answer=0
        
    return answer