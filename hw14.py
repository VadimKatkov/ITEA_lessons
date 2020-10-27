'''
Посчитать количество строк в файле и количество слов и символов в каждой строке
В текстовом файле посчитать количество строк, а также для каждой отдельной строки определить количество в ней символов и слов.

Hello world!
Привет мир!
One, two, three
Один, два, три

Результат
Hello world!
 13 симв. 2 сл.

Привет мир!
 12 симв. 2 сл.

One, two, three
 16 симв. 3 сл.

Один, два, три
 15 симв. 3 сл.
4 строки
'''

import re
with open('story.txt', encoding='utf-8') as file:
    story = []
    for lane in file:
        lane_words = lane.strip('\n')
        lane_words = re.split(' +',lane)
        print(lane, end='')
        print(len(lane), 'симв.', len(lane_words),  'cл.', end='\n')
        print()
        story.append(lane)
print(len(story), 'строки')