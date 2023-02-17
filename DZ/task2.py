"""
2) Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open("task2.txt", "r", encoding='utf-8') as my_f:
    content = my_f.read()
    print(content)
    line_count = 0
    word_count = 0
    for line in content.split('\n'):
        for word in line.split():
            word_count += 1
        line_count += 1
    print(f'Количество строк: {line_count}\n'
          f'Количество слов: {word_count}')
