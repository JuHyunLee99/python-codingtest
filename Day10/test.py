def solution2(n, lost, reserve):
    for i in reserve:
        if i in lost:
            lost.remove(i)
        elif i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)
    return n-len(lost)

n = 5
lost = [2, 4]

reserve = [1,3,5]

print(solution2(n, lost, reserve)) # return 5