def solution(arr, k):
    result=[]
    if k%2!=0:
        for i in range(len(arr)):
            result.append(arr[i]*k)
    else:
         for i in range(len(arr)):
                result.append(arr[i]+k)
    
    return result