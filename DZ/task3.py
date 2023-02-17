"""
3) Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные. При этом английские числительные должны заменяться на
русские. Новый блок строк должен записываться в новый текстовый файл.
"""

with open("task3-0.txt", "r", encoding='utf-8') as my_f:
    content = my_f.read()
    content = content.replace('One', 'Один')
    content = content.replace('Two', 'Два')
    content = content.replace('Three', 'Три')
    content = content.replace('Four', 'Четыре')
    print(content)

    with open("test3-1.txt", "w", encoding='utf-8') as my_file:
        for line in content.split('\n'):
            my_file.write(f'{line}\n')
