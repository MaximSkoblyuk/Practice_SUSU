from modules.lexical import identification


def refactor(lexical_list_src: list):
    """Create new list without spaces"""

    lexical_list = []
    for element in lexical_list_src:
        if element[1] is not None:
            lexical_list.append(element)
    return lexical_list


def lexical(transliteration_list: list):
    """Realization of lexical block by transition machine and using state"""

    flag = 1
    lexical_list_src = [('', None)]

    def addKey(symbol, type_name):
        """Add symbol from string to definite lexeme or create new lexem"""

        if lexical_list_src[-1][1] == type_name:
            lexical_list_src[-1] = (lexical_list_src[-1][0] + symbol, lexical_list_src[-1][1])
        else:
            lexical_list_src.append((symbol, type_name))

    state = 'start'
    for item in transliteration_list:
        if state == 'start':
            if item[1] == 'letter':
                state = 'k_word_var'
                addKey(item[0], 'k_word_var')
            else:
                flag = 0
        elif state == 'k_word_var':
            if item[1] == 'letter':
                addKey(item[0], 'k_word_var')
            elif item[1] == 'space':
                state = 'space1'
                addKey(item[0], None)
            else:
                flag = 0
        elif state == 'space1':
            if item[1] == 'letter':
                state = 'identifier'
                addKey(item[0], 'identifier')
            elif item[1] == 'space':
                addKey(item[0], None)
            else:
                flag = 0
        elif state == 'identifier':
            if item[1] == 'letter' or item[1] == 'digit':
                addKey(item[0], 'identifier')
            elif item[1] == 'space':
                state = 'space2'
                addKey(item[0], None)
            elif item[1] == 'comma':
                state = 'space1'
                addKey(item[0], 'comma')
            elif item[1] == 'colon':
                state = 'space3'
                addKey(item[0], 'colon')
            else:
                flag = 0
        elif state == 'space2':
            if item[1] == 'space':
                addKey(item[0], None)
            elif item[1] == 'colon':
                state = 'space3'
                addKey(item[0], 'colon')
            else:
                flag = 0
        elif state == 'space3':
            if item[1] == 'space':
                addKey(item[0], None)
            elif item[1] == 'letter':
                state = 'k_word_array'
                addKey(item[0], 'k_word_array')
            else:
                flag = 0
        elif state == 'k_word_array':
            if item[1] == 'space':
                state = 'space4'
                addKey(item[0], None)
            elif item[1] == 'letter':
                addKey(item[0], 'k_word_array')
            elif item[1] == 'square_bracket_start':
                state = 'space5'
                addKey(item[0], 'square_bracket_start')
            else:
                flag = 0
        elif state == 'space4':
            if item[1] == 'space':
                addKey(item[0], None)
            elif item[1] == 'square_bracket_start':
                state = 'space5'
                addKey(item[0], 'square_bracket_start')
            else:
                flag = 0
        elif state == 'space5':
            if item[1] == 'space':
                addKey(item[0], None)
            elif item[1] == 'letter':
                state = 'identifier_lower'
                addKey(item[0], 'identifier_lower')
            elif item[1] == 'digit':
                state = 'number_lower'
                addKey(item[0], 'number_lower')
            elif item[1] == 'sign':
                state = 'space_lower'
                addKey(item[0], 'sign')
            else:
                flag = 0
        elif state == 'identifier_lower':
            if item[1] == 'space':
                state = 'space6'
                addKey(item[0], None)
            elif item[1] == 'letter' or item[1] == 'digit':
                addKey(item[0], 'identifier_lower')
            elif item[1] == 'dot':
                state = 'dots'
                addKey(item[0], 'dots')
            else:
                flag = 0
        elif state == 'space_lower':
            if item[1] == 'space':
                addKey(item[0], None)
            elif item[1] == 'digit':
                state = 'number_lower'
                addKey(item[0], 'number_lower')
            else:
                flag = 0
        elif state == 'number_lower':
            if item[1] == 'space':
                state = 'space6'
                addKey(item[0], None)
            elif item[1] == 'digit':
                addKey(item[0], 'number_lower')
            elif item[1] == 'dot':
                state = 'dots'
                addKey(item[0], 'dots')
            else:
                flag = 0
        elif state == 'space6':
            if item[1] == 'space':
                addKey(item[0], None)
            elif item[1] == 'dot':
                state = 'dots'
                addKey(item[0], 'dots')
            else:
                flag = 0
        elif state == 'dots':
            if item[1] == 'dot':
                state = 'space7'
                addKey(item[0], 'dots')
            else:
                flag = 0
        elif state == 'space7':
            if item[1] == 'space':
                addKey(item[0], None)
            elif item[1] == 'letter':
                state = 'identifier_upper'
                addKey(item[0], 'identifier_upper')
            elif item[1] == 'digit':
                state = 'number_upper'
                addKey(item[0], 'number_upper')
            elif item[1] == 'sign':
                state = 'space_upper'
                addKey(item[0], 'sign')
            else:
                flag = 0
        elif state == 'identifier_upper':
            if item[1] == 'space':
                state = 'space8'
                addKey(item[0], None)
            elif item[1] == 'letter' or item[1] == 'digit':
                addKey(item[0], 'identifier_upper')
            elif item[1] == 'square_bracket_end':
                state = 'space9'
                addKey(item[0], 'square_bracket_end')
            else:
                flag = 0
        elif state == 'space_upper':
            if item[1] == 'space':
                addKey(item[0], None)
            elif item[1] == 'digit':
                state = 'number_upper'
                addKey(item[0], 'number_upper')
            else:
                flag = 0
        elif state == 'number_upper':
            if item[1] == 'space':
                state = 'space8'
                addKey(item[0], None)
            elif item[1] == 'digit':
                addKey(item[0], 'number_upper')
            elif item[1] == 'square_bracket_end':
                state = 'space9'
                addKey(item[0], 'square_bracket_end')
            else:
                flag = 0
        elif state == 'space8':
            if item[1] == 'space':
                addKey(item[0], None)
            elif item[1] == 'square_bracket_end':
                state = 'space9'
                addKey(item[0], 'square_bracket_end')
            else:
                flag = 0
        elif state == 'space9':
            if item[1] == 'space':
                addKey(item[0], None)
            elif item[1] == 'letter':
                state = 'k_word_of'
                addKey(item[0], 'k_word_of')
            else:
                flag = 0
        elif state == 'k_word_of':
            if item[1] == 'space':
                state = 'space10'
                addKey(item[0], None)
            elif item[1] == 'letter':
                state = 'space10'
                addKey(item[0], 'k_word_of')
            else:
                flag = 0
        elif state == 'space10':
            if item[1] == 'space':
                addKey(item[0], None)
            elif item[1] == 'letter':
                state = 'k_word_type_of_data'
                addKey(item[0], 'k_word_type_of_data')
            else:
                flag = 0
        elif state == 'k_word_type_of_data':
            if item[1] == 'space':
                state = 'space11'
                addKey(item[0], None)
            elif item[1] == 'letter':
                addKey(item[0], 'k_word_type_of_data')
            elif item[1] == 'semicolon':
                state = 'semicolon'
                addKey(item[0], 'semicolon')
            else:
                flag = 0
        elif state == 'space11':
            if item[1] == 'space':
                addKey(item[0], None)
            elif item[1] == 'semicolon':
                state = 'semicolon'
                addKey(item[0], 'semicolon')
            else:
                flag = 0
        elif state == 'semicolon':
            if item[1]:
                flag = 0
    if state != 'semicolon':
        flag = 0

    lexical_list = refactor(lexical_list_src)
    lexical_list = identification.identification(lexical_list)
    return lexical_list, flag


if __name__ == '__main__':
    my_list = [['v', 'letter'], ['a', 'letter'], ['r', 'letter'], [' ', 'space'], ['I', 'letter'], ['n', 'letter'],
               ['p', 'letter'], [':', 'colon'], [' ', 'space'], ['a', 'letter'], ['r', 'letter'], ['r', 'letter'],
               ['a', 'letter'], ['y', 'letter'], [' ', 'space'], ['[', 'square_bracket_start'], ['1', 'digit'],
               ['.', 'dot'], ['.', 'dot'], ['-', 'sign'], [' ', 'space'], ['2', 'digit'], [']', 'square_bracket_end'],
               [' ', 'space'], ['o', 'letter'], ['f', 'letter'], [' ', 'space'], ['C', 'letter'], ['h', 'letter'],
               ['a', 'letter'], ['r', 'letter'], [';', 'semicolon']]
    result = lexical(my_list)
    for x in result:
        print(x)
