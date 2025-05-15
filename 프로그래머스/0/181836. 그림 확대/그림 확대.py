def solution(picture, k):
    enlarged = []
    for row in picture:
        
        stretched_row = ''.join(char * k for char in row)
        
        for _ in range(k):
            enlarged.append(stretched_row)
    return enlarged
