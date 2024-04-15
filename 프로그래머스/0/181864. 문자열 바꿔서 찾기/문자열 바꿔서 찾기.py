def solution(myString, pat):
    string=[]
    
    for ch in myString:
        if ch=='A':
            string.append('B')
        else:
            string.append('A')
            
    if pat in ''.join(string):
        return 1
    else:
        return 0
   