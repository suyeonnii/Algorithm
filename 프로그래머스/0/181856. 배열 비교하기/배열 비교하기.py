def solution(arr1, arr2):
    sum1=0
    sum2=0
    
    if len(arr1)==len(arr2):
        for num in arr1:
            sum1+=num
        for num in arr2:
            sum2+=num
        if sum1>sum2:
            return 1
        elif sum1==sum2:
            return 0
        else:
            return -1
    else:
        if len(arr1)>len(arr2):
            return 1
        else:
            return -1
        