def check_parentheses(expression : str) -> bool: # type hint
    stack = []
    for letter in expression:
        if letter == "(":
            stack.append(letter)
        if letter == ")":
            if(len(stack) == 0):
                return False
            else:
                stack.pop() #집어 넣은 걸 뺀다
    return len(stack) == 0

print(check_parentheses("(2+3)"))
print(check_parentheses("(2+(2*3))"))
print(check_parentheses("(2+(2*3)")) # 삽입 2번 팝 1번 stack에 여는 소괄호 하나가 남아서 False
print(check_parentheses(")2+(2*3)("))