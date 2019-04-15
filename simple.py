
def check(string):
    brackets = ''.join([x for x in string if x in ['(',')','{','}']])
    while brackets:
        index = max(brackets.find('()'), brackets.find('{}'))
        if index == -1:
            return False
        else:
            brackets = brackets[:index] + brackets[index+2:]
    return True


if __name__ == '__main__':
    f = check('(2+3)+2-1')
    if f:
        print('True')
    else:
        print('False')
