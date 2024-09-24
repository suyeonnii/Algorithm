def solution(age):
    answer=''
    age_str=str(age)
    
    for i in age_str:
        answer+=chr(ord('a')+int(i))
    
    return answer