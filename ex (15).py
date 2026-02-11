
def postfixToInfix(postfix):
    stack = []

    for ch in postfix:
        if ch == ' ':
            continue
        if ch.isalnum():
            stack.append(ch)
        elif ch in "+-*/":
            op2 = stack.pop()
            op1 = stack.pop()
            expr = f"({op1}{ch}{op2})"
            stack.append(expr)
        else:
            print('invalid')
            return
    return stack.pop()
print(postfixToInfix('ab+c*'))