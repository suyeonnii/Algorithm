def solution(arr, intervals):
    a1, b1 = intervals[0]
    a2, b2 = intervals[1]
    
    part1 = arr[a1:b1+1]  
    part2 = arr[a2:b2+1] 
    
    return part1 + part2 