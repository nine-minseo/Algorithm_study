import sys
num = int(sys.stdin.readline().strip())

moves = []

def hanoi(n, frm, tmp, to):
    if n == 1:
        moves.append((frm, to))
        return 1
    
    a = hanoi(n-1, frm, to, tmp)
    moves.append((frm, to))
    b = hanoi(n-1, tmp, frm, to)
    return a + 1 + b

print(hanoi(num, 1, 2, 3))
for move in moves:
    print(move[0], move[1])