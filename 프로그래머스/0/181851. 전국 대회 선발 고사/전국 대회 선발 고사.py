def solution(rank, attendance):
    n = len(rank)
    
    students = [(rank[i], i) for i in range(n) if attendance[i]]
    
    students.sort()

    a = students[0][1]
    b = students[1][1]
    c = students[2][1]
    
    return 10000 * a + 100 * b + c
