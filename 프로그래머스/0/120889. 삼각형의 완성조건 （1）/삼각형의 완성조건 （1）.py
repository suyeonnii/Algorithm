def solution(sides):
    answer = 0
    
    sides.sort() #세 변을 오름차순으로 정렬
    
    longest=sides[-1] # 가장 긴 변의 길이
    sum_others=sum(sides[:-1]) #나머지 두 변의 길이 합
    
    if longest < sum_others:
        answer=1
    else:
        answer=2
        
    return answer