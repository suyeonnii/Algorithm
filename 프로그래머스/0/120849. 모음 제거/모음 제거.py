def solution(my_string):
    result=""
    for ch in my_string:
        if ch not in "aeiou":
            result+=ch
    
    return result
        