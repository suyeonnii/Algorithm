def solution(array):
    max_num=max(array)
    result=[]
    for index, num in enumerate(array):
        if max_num==num:
            result.append(num)
            result.append(index)
    return result