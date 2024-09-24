def solution(s):
    answer=[]
    
    for ch in s:
        if s.count(str(ch)) ==1:
            answer.append(ch)
            
    return ''.join(sorted(answer))