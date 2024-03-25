def solution(money):
    coffee=0
    change_money=0
    
    coffee = money//5500
    change_money = money % 5500
    
    answer = [coffee,change_money]
    return answer