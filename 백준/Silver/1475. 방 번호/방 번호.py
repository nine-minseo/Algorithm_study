import sys
room_num = sys.stdin.readline()

num_list = []

for i in range(len(room_num)-1):
    num_list.append(int(room_num[i]))

count_list = [0] * 9

for num in num_list:
    if num == 9:
        count_list[6] += 1
    else:
        count_list[num] += 1

count_list[6] = (count_list[6] // 2 + count_list[6] % 2)

print(max(count_list))

