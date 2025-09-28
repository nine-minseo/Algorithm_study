import sys
n = int(sys.stdin.readline().rstrip())
subject_list = list(map(int, sys.stdin.readline().rstrip().split()))

max_subject = max(subject_list)
new_subject_list = []

for subject in subject_list:
    new_subject_list.append(subject / max_subject * 100)

print(sum(new_subject_list) / len(new_subject_list))