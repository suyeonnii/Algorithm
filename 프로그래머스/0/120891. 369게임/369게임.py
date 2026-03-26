def solution(order):
    clap=0
    order=str(order)
    for ch in order:
        if ch in "369":
            clap+=1
    return clap