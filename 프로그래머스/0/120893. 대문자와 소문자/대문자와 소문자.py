def solution(my_string):
    result=""
    for ch in my_string:
        if ch.isupper():
            result+=ch.lower()
        else:
            result+=ch.upper()
    
    return result