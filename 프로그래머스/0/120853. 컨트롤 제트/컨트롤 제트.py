def solution(s):
    answer = 0
    num=0
    last=0
    stack=[]
    
    for token in s.split():
        if token=='Z' and stack:
            last=stack.pop()
            answer-=last
        else:
            num=int(token)
            answer+=num
            stack.append(num)
        
    return answer