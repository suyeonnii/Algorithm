def solution(my_string):
    
    suffixes = [my_string[i:] for i in range(len(my_string))]
    
    suffixes.sort()
    return suffixes