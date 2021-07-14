from string import ascii_letters

numbers = tuple([str(i) for i in range(10)])
letters = ascii_letters + "_"  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_
symbols = {numbers: "digit",
           letters: "letter",
           " ": "space",
           ";": "semicolon",
           ".": "dot",
           ",": "comma",
           ":": "colon",
           "+-": "sign",
           "[": "square_bracket_start",
           "]": "square_bracket_end"}


def transliterator(string: str):
    """Realization of Transliteration block and dividing the string into separate symbols """

    n = len(string)
    transliteration_list = [[''] * 2 for _ in range(n)]  # двумерный список: символ-класс
    flag = 1  # показывает, есть ли в строке хотя бы один символ класса other
    for index, symbol in enumerate(list(string)):
        for key, value in symbols.items():
            if symbol in key:
                transliteration_list[index][0], transliteration_list[index][1] = symbol, value
                break
            elif key == "]" and not transliteration_list[index][0]:
                flag = 0
                transliteration_list[index][0], transliteration_list[index][1] = symbol, "other"
                return transliteration_list[:index+1], flag
    return transliteration_list, flag


if __name__ == '__main__':
    inp = 'var Inp: array [1..- 2] of Char;'

    result = transliterator(string=inp)
    my_list, my_flag = result[0], result[1]
    print(my_list)
    print(my_flag)
