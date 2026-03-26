def solution(cipher, code):
    result=""
    i=0
    for ch in cipher:
        i+=1
        if i%code==0:
            result+=ch
    
    return result