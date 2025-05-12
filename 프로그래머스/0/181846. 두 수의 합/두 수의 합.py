def solution(a, b):
    result = []
    carry = 0

    a = a[::-1]
    b = b[::-1]
    
    max_len = max(len(a), len(b))
    
    for i in range(max_len):
        digit_a = int(a[i]) if i < len(a) else 0
        digit_b = int(b[i]) if i < len(b) else 0
        
        total = digit_a + digit_b + carry
        carry = total // 10
        result.append(str(total % 10))
    
    if carry:
        result.append(str(carry))

    return ''.join(result[::-1])
