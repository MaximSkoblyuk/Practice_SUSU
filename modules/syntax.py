def count(numbers_list: list):
    """Count amount of numbers in list"""

    counter = 0
    for item in numbers_list:
        if str(item).isdigit():
            counter += 1
    return counter


def chaining(numbers_list: list, counter: int):
    """Chaining numbers with signs"""
    numbers, index = ['', ''], 0
    if counter == 2:
        for x in numbers_list:
            numbers[index] += x
            if str(x).isdigit():
                index += 1
    return numbers


def compare(numbers_list: list):
    """Compare first and second numbers"""

    if int(numbers_list[0]) < int(numbers_list[1]):
        return True
    return False


def syntax(identified_list: list):
    """Realization of syntax block by transition machine and using state"""

    state, flag, nums = 'start', True, []
    for item in identified_list:
        if state == 'start':
            if item[1] == 'var':
                state = 'var'
            else:
                flag = False
        elif state == 'var':
            if item[1] == 'identifier':
                state = 'identifier'
            else:
                flag = False
        elif state == 'identifier':
            if item[1] == 'comma' or item[1] == 'identifier':
                continue
            elif item[1] == 'colon':
                state = 'colon'
            else:
                flag = False
        elif state == 'colon':
            if item[1] == 'array':
                state = 'array'
            else:
                flag = False
        elif state == 'array':
            if item[1] == 'square_bracket_start':
                state = 'square_bracket_start'
            else:
                flag = False
        elif state == 'square_bracket_start':
            if item[1] == 'identifier_lower':
                state = 'identifier_lower'
            elif item[1] == 'sign' or item[1] == 'number_lower':
                state = 'number_lower'
                nums.append(item[0])
            else:
                flag = False
        elif state == 'identifier_lower':
            if item[1] == 'dots':
                state = 'dots'
            else:
                flag = False
        elif state == 'number_lower':
            if item[1] == 'dots':
                state = 'dots'
            elif item[1] == 'number_lower':
                nums.append(item[0])
                continue
            else:
                flag = False
        elif state == 'dots':
            if item[1] == 'identifier_upper':
                state = 'identifier_upper'
            elif item[1] == 'sign' or item[1] == 'number_upper':
                state = 'number_upper'
                nums.append(item[0])
            else:
                flag = False
        elif state == 'identifier_upper':
            if item[1] == 'square_bracket_end':
                state = 'square_bracket_end'
            else:
                flag = False
        elif state == 'number_upper':
            if item[1] == 'square_bracket_end':
                state = 'square_bracket_end'
            elif item[1] == 'number_upper':
                nums.append(item[0])
                continue
            else:
                flag = False
        elif state == 'square_bracket_end':
            if item[1] == 'of':
                state = 'of'
            else:
                flag = False
        elif state == 'of':
            if item[1] == 'type':
                state = 'type'
            else:
                flag = False
        elif state == 'type':
            if item[1] == 'semicolon':
                state = 'semicolon'
            else:
                flag = False
        elif state == 'semicolon':
            if item[1]:
                flag = False
    if state != 'semicolon':
        flag = False

    counter = count(nums)
    chaining_nums = chaining(nums, counter)
    if flag and counter == 2:
        flag = compare(chaining_nums)

    return flag


if __name__ == '__main__':
    list = [('var', 'var'), ('Inp', 'identifier'), (':', 'colon'), ('array', 'array'), ('[', 'square_bracket_start'),
            ('1', 'number_lower'), ('..', 'dots'), ('-', 'sign'), ('2', 'number_upper'), (']', 'square_bracket_end'),
            ('of', 'of'), ('Char', 'type'), (';', 'semicolon')]
    print(syntax(list))
    # borders = ['1', '-', '2']
    # numbers = chaining(borders, 2)
    # print(compare(numbers))
