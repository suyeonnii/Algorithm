def solution(myStr):
    
    parts = []
    temp = ''
    for ch in myStr:
        if ch in 'abc':
            if temp:
                parts.append(temp)
                temp = ''
        else:
            temp += ch
    if temp:
        parts.append(temp)
    
    return parts if parts else ["EMPTY"]
