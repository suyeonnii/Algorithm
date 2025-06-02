def solution(score):
    
    avg_with_index = []
    for i, s in enumerate(score):
        avg = (s[0] + s[1]) / 2
        avg_with_index.append((avg, i))
    
    avg_with_index.sort(reverse=True)
    
    rank = [0] * len(score)
    current_rank = 1
    for i in range(len(avg_with_index)):
        if i > 0 and avg_with_index[i][0] != avg_with_index[i - 1][0]:
            current_rank = i + 1
        idx = avg_with_index[i][1]
        rank[idx] = current_rank
    
    return rank
