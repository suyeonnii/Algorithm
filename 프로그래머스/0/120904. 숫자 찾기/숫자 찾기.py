def solution(num, k):
    answer=0;
    
    for i,char in enumerate(str(num)):
        if char==str(k):
            return i+1;
        
    return -1;
        
        
        