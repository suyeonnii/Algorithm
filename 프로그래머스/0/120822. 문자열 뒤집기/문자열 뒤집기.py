def solution(my_string):
    answer = ''
    for char in reversed(my_string):
        answer += char
    return answer