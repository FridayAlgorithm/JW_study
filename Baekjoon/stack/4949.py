while True:
    line = input()
    if line == ".":
        break
    stack = []
    check = True

    for ch in line:
        if ch == "(" or ch == "[":
            stack.append(ch)

        elif ch == ")":
            if len(stack) == 0:
                check = False
                break
            if stack[-1] == "(":
                stack.pop()
            else:
                check = False
                break

        elif ch == "]":
            if len(stack) == 0:
                check = False
                break
            if stack[-1] == "[":
                stack.pop()
            else:
                check = False
                break

    if check and len(stack)==0:
        print("yes")
    else:
        print("no")
