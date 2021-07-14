from modules import input, output, transliterator, syntax
from modules.lexical import lexical


def main():
    """Main function"""

    input_str = input.input_file('files/input.txt')  # Входная строка

    transliteration_list, transliteration_flag = transliterator.transliterator(input_str)  # Этап транслитерации

    if transliteration_flag:
        lexical_identified_list, lexical_flag = lexical.lexical(transliteration_list)  # Лексический блок
        if lexical_flag:
            syntax_flag = syntax.syntax(lexical_identified_list)  # Синтаксический блок

    if transliteration_flag and lexical_flag and syntax_flag:
        output.output_file('files/output.txt', 'ACCEPT')
    else:
        output.output_file('files/output.txt', 'REJECT')

    # print(input_str)
    # print(transliteration_list)
    # print(lexical_identified_list)
    # print(lexical_flag)
    # print(syntax_flag)
    return 0


if __name__ == '__main__':
    main()
