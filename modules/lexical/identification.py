def identification(lexical_list: list):
    """Search keywords of Pascal in string and changing them class"""

    pascal = ['and', 'end', 'nil', 'set', 'array', 'file', 'not', 'then', 'begin', 'for', 'of', 'to', 'case',
              'function', 'or', 'type', 'const', 'goto', 'packed', 'until', 'div', 'if', 'procedure', 'var', 'do', 'in',
              'program', 'while', 'downto', 'label', 'record', 'with', 'else', 'mod', 'repeat']
    data_type = ['boolean', 'byte', 'char', 'integer', 'longint', 'real', 'string', 'word']
    identified_list = []

    for item in lexical_list:
        if item[0].lower() in pascal:
            identified_list.append((item[0], item[0]))
        elif item[0].lower() in data_type:
            identified_list.append((item[0], 'type'))
        else:
            identified_list.append(item)
    return identified_list


if __name__ == '__main__':
    list = [('var', 'k_word_var'), ('arr', 'identifier'), (':', 'colon'), ('array', 'k_word_array'),
            ('[', 'square_bracket_start'), ('+', 'sign'), ('1', 'number_lower'), ('..', 'dots'),
            ('N', 'identifier_upper'), (']', 'square_bracket_end'), ('of', 'k_word_of'),
            ('Real', 'k_word_type_of_data'), (';', 'semicolon')]
    list = identification(list)
    print(list)
