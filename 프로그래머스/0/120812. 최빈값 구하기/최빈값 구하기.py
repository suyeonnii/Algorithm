from collections import Counter

def solution(array):
    count = Counter(array)
    max_freq = max(count.values())

    modes = [num for num, freq in count.items() if freq == max_freq]

    if len(modes) > 1:
        return -1
    return modes[0]
