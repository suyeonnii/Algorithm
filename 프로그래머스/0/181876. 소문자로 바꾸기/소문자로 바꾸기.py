def solution(myString):
    answer = ''
    
    for ch in myString:
        if 'A'<=ch<='Z':
            answer+=chr(ord(ch)+32)
        else:
            answer+=ch
            
    return answer