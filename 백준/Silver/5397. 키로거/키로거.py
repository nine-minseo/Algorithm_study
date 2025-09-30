import sys
input = sys.stdin.readline

case = int(input())

for i in range(case):
    left_stack = []
    right_stack = []

    # 테스트 케이스를 한 줄 입력받음
    messy_password = input().strip()
    # 문자 하나씩 동작
    for str in messy_password:
        # 문자가 '<'이고 왼쪽 스택에 원소가 있으면 왼쪽 스택의 마지막 원소를 오른쪽 스택에 삽입
        if str == '<':
            if len(left_stack) > 0:
                right_stack.append(left_stack.pop())
                #print(f"left_stack: {left_stack}")
                #print(f"right_stack: {right_stack}\n")
            continue
        # 문자가 '>'이고 오른쪽 스택에 원소가 있으면 오른쪽 스택의 마지막 원소를 왼쪽 스택에 삽입 
        elif str == '>':
            if len(right_stack) > 0:
                left_stack.append(right_stack.pop())
                #print(f"left_stack: {left_stack}")
                #print(f"right_stack: {right_stack}\n")
            continue
        # 문자가 '-'이고 왼쪽 스택에 문자가 있다면 문자 삭제
        elif str == '-' and len(left_stack) > 0:
            left_stack.pop()
            #print(f"left_stack: {left_stack}")
            #print(f"right_stack: {right_stack}\n")
            continue
        # 문자가 숫자, 영단어라면 패스워드에 추가
        elif str.isalnum() == True:
            #print(f"str: {str}")
            left_stack.append(str)
            #print(f"left_stack: {left_stack}")
            #print(f"right_stack: {right_stack}\n")

    while len(right_stack) > 0:
        left_stack.append(right_stack.pop())
        #print(f"left_stack: {left_stack}")
        #print(f"right_stack: {right_stack}\n")

    # 패스워드 출력
    print("".join(left_stack))
