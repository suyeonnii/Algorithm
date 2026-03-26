def solution(my_string, num1, num2):
    answer=""
    ch1=my_string[num1]
    ch2= my_string[num2]
    for i in range(len(my_string)):
        if i==num1:
            answer+=ch2
        elif i==num2:
            answer+=ch1
        else:
            answer+=my_string[i]
    
    return answer