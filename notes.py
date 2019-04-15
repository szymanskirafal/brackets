import re

def simple_print():
    print('Brackets file is running')


opening_brackets = tuple('({[')
closing_brackets = tuple(')}]')
mapping = dict(zip(opening_brackets, closing_brackets))

expression = '2+4+(2-(3+1+(4+1))1)'

            '2+(4+2)-(3+1+(4+1))1)'

            '2+4+)2-(3+1+(4+1))1)'

check_for_brackets

    brackets = "[({)}]"
    prog = re.compile(closing_brackets)
    string = str(expression)
    result = prog.search(string)

if )
    fail

if (

    check_nested



    it must be ) as pair

    check another run








                    2 * (y^{(x + 2) * 6})



             (    ()    ()    )














            check another (

            if bracket_is_closing:
                print('fail')

            elif:
                bracket is opening

                    check for braket

                    check for closing braket cos it should be there

    else:
        theres no brakcet at all



check_for_opening_bracket
    check_for_

def check_for_closing_bracket(expression = expression):
    closing_brackets = "[)}]"
    prog = re.compile(closing_brackets)
    string = str(expression)
    result = prog.search(string)
    if result:
        print('There should not be closing brackets if there are not opening')
        print(' but i have found one at position ', result.start(), result)

def check_for_opening_bracket(expression = expression):
    pattern = "[({]"
    prog = re.compile(pattern)
    string = str(expression)
    result = prog.search(string)
    if result == None:
        print('---- no opening brackets here ----')
        check_for_closing_bracket(expression = expression)
    else:
        print(result)
        print('we examine expression: ', expression)
        print('we have found an opening bracket at position ', result.start(), result.end())
        print('we cut out first part of the expression')
        cut_from_here = result.end()
        expression = expression[cut_from_here:]
        print('and rest of the expression is: ', expression)
        check_for_opening_bracket(expression)

    """
    _string = str(expression)
    result = re.match(patern, string)

    print('checking the expression: ', _string)
    if _string.find('('):
        print(' - An opening brackets have been found at position: ', _string.find('('))
    else:
        print('No opening bracket have been found')


    opening_bracket = any(opening_brackets)

    if opening_brackets in _string:
        print('we have something here', opening_bracket)
        #print('the position is: ', _string.find(opening_bracket))



    for x in _string:
        if x in opening_brackets:
            print('-- ', x, ' this one is an opening bracket')
            index_of_bracket = expression.index(x)
            slice_from_here = index_of_bracket + 1
            expression = expression[slice_from_here:]
            print(' sliced expression is ', expression )
            check_for_opening_bracket(expression)
        #else:
        #    print('-- ', x)

    """




if __name__ == '__main__':
    simple_print()
    #expression = '2+4+6-(2-(3+1+(4+1))1)'
    check_for_opening_bracket()
