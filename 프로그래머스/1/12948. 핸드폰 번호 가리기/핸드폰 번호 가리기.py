def solution(phone_number):

    length = len(phone_number)
    
    masked_part = "*" * (length - 4)
    
    last_four_digits = phone_number[-4:]
    
    answer = masked_part + last_four_digits
    
    return answer
