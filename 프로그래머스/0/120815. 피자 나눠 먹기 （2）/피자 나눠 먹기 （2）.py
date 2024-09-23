def solution(n):
    pizza=1;
    slice=6
    
    while slice%n!=0:
        pizza+=1;
        slice=6*pizza;
        
    return pizza;