def solution(my_string):
    answer = ''
    
    for ch in my_string:
        if 'A'<=ch<='Z':
            answer+=chr(ord(ch)+32)
        else:
            answer+=chr(ord(ch)-32)
    return answer