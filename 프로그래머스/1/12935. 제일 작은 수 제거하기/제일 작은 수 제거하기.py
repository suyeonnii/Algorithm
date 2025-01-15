def solution(arr):
    
    # 배열의 길이가 1인 경우, [-1] 반환
    if len(arr) == 1:
        return [-1]
    
    # 가장 작은 수를 제거한 배열 반환
    min_value = min(arr)
    arr.remove(min_value)
    return arr
