def solution(price):
    if price >= 500000:
        return int(price * 0.80)  # 20% 할인
    elif price >= 300000:
        return int(price * 0.90)  # 10% 할인
    elif price >= 100000:
        return int(price * 0.95)  # 5% 할인
    else:
        return price  # 할인 없음