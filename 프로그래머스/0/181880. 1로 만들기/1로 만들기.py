def solution(num_list):
    count = 0
    for num in num_list:
        while num > 1:
            num //= 2
            count += 1
    return count
