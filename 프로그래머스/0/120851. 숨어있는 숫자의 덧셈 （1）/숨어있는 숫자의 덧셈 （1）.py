def solution(my_string):
    result=0
    for ch in my_string:
        if ch.isdigit():
            result+=int(ch)
    return result