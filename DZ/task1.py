"""
1) Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

with open("test_file.txt", "w", encoding='utf-8') as my_file:

    def input_line():
        line_str = input(f'Введите строку: ')
        if not line_str:
            return
        else:
            my_file.write(f'{line_str}\n')
            input_line()

    input_line()



