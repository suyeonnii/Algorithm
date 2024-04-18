def solution(myString, pat):
    
    if pat.casefold() in myString.casefold():
        return 1
    else:
        return 0