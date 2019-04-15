def check(equation):
    parentheses = ''.join(c for c in equation if c in {'{', '}', '(', ')'})

    if len(parentheses) % 2 != 0:
        return False

    stack = []
    chars = {'{': '}', '(': ')'}

    for c in parentheses:
        if c in chars.keys():
            stack.append(chars[c])
        else:
            if not stack or c != stack.pop():
                return False
    return not stack

if __name__ == '__main__':
    f = check('2+()3+(2-()(1))')
    if f:
        print('True')
    else:
        print('False')
