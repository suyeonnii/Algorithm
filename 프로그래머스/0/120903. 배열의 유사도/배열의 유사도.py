def solution(s1,s2):
    result=0
    for val in s1:
        if val in s2:
            result+=1
    return result