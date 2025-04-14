def solution(myString):
    
    parts = myString.split("x")
    
    filtered = [part for part in parts if part]
    
    return sorted(filtered)
