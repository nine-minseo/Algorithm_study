import sys
alphabet = sys.stdin.readline().rstrip()

count = 0
changed_alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

i = 0
while i < len(alphabet):
    if alphabet[i:i+3] == "dz=":
        #print(alphabet[i:i+3])
        count += 1
        i += 3
    elif alphabet[i:i+2] in ["c=", "c-", "d-", "lj", "nj", "s=", "z="]:
        #print(alphabet[i:i+2])
        count += 1
        i += 2
    else:
        #print(alphabet[i])
        count += 1
        i += 1

print(count)