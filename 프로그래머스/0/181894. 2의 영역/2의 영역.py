def solution(arr):
    if 2 not in arr:
        return [-1]
    
    first = arr.index(2)
    last = len(arr) - 1 - arr[::-1].index(2)
    
    return arr[first:last+1]
