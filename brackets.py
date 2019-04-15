class BracketsOpenAndCloseTester:

    def __init__(self, expression = '2*((4))-1'):
        self.brackets_allowed = "[({)}]"
        self.opening_brackets = "[({"
        self.closing_brackets = "])}"
        self.pairs = ['()', '{}', "[]", ]
        self.expression = expression
        self.brackets_in_expression = ''

    def find_any_bracket_in_expression(self):
        expression = self.expression
        brackets_allowed = self.brackets_allowed
        bracket_found = [expression.find(x) for x in expression if x in brackets_allowed]
        print('-- brackets are in expression at positions: ', bracket_found)
        return bracket_found

    def create_a_string_with_brackets_found_in_expression(self):
        expression = self.expression
        brackets_allowed = self.brackets_allowed
        brackets_extracted = [x for x in expression if x in brackets_allowed]
        brackets_extracted = ''.join(brackets_extracted)
        print('-- created string with brackets found: ', brackets_extracted)
        self.brackets_in_expression = brackets_extracted
        print('-- brackets_in_expresion: ', self.brackets_in_expression)
        return True

    def remove_pair(self, position = None):
        print('-- will try to remove pair which begins at position ', position)
        brackets_in_expression = self.brackets_in_expression
        first_part_of_expression = brackets_in_expression[:position]
        second_part_of_expression = brackets_in_expression[position+2:]
        brackets_in_expression = first_part_of_expression + second_part_of_expression
        print('-- brackets in expression: ', brackets_in_expression)
        self.brackets_in_expression = brackets_in_expression
        return self.check_pairs()

    def check_brackets(self):
        bracket_found_in_expression = self.find_any_bracket_in_expression()
        if bracket_found_in_expression:
            self.proccess_with_brackets()
        else:
            print("There are no brackets but it's ok.")
            return True

    def check_brackets_are_balanced(self):
        expression = self.expression
        opening_brackets = self.opening_brackets
        closing_brackets = self.closing_brackets
        opening_brackets = [x for x in expression if x in opening_brackets]
        number_of_opening_brackets = len(opening_brackets)
        closing_brackets = [x for x in expression if x in closing_brackets]
        number_of_closing_brackets = len(closing_brackets)
        if number_of_opening_brackets == number_of_closing_brackets:
            return True
        else:
            return False

    def check_pairs(self):
        brackets = self.brackets_in_expression
        pairs = self.pairs
        positions_of_pair_found = []
        for pair in pairs:
            p = brackets.find(pair)
            positions_of_pair_found.append(p)
        position = max(positions_of_pair_found)
        if position != -1:
            print('-- position: ', position)
            return self.remove_pair(position = position)
        else:
            print("-- There aren't any pairs.")
            return False

    def proccess_with_brackets(self):
        self.create_a_string_with_brackets_found_in_expression()
        brackets_are_balanced = self.check_brackets_are_balanced()
        if brackets_are_balanced:
            print('-- brackets are balanced.')
            return self.check_pairs()
        else:
            print("Brackets are not balanced in given expression.")
            return False


if __name__ == '__main__':
    test = BracketsOpenAndCloseTester()
    result = test.check_brackets()
