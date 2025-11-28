def solution(n):
    answer = 0
    
    odd = []
    even = []
    for i in range(1, n+1):
        if i % 2 == 0:
            even.append(i)
        elif i % 2 == 1:
            odd.append(i)
    
    if n % 2 == 1:
        answer = sum(odd)
    else:
        answer = sum(list([a**2 for a in even]))
            
    return answer