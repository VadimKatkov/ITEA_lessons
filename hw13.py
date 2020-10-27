'''
Задана матрица неотрицательных чисел.
Посчитать сумму элементов в каждом столбце. Определить, какой столбец содержит максимальную
сумму.
'''

def matrixprint(matrix): # создали функцию для вывода на печать
    for line in matrix:
        for j in range(len(line)):
            print('%3d' % (line[j]), end=' ')
        print()


if __name__ == '__main__':
    with open('matrix.txt') as dataFile: #читаем файл и формируем матрицу данных
        matrix = []
        for line in dataFile:
            strTemp = []
            line_new = line.strip('\n').split(' ')
            for j in line_new:
                strTemp.append(int(j))
            matrix.append(strTemp)

    sumArr = []
    for line in range(len(matrix)):   # формируем список с суммами по колонокам
        checkSum = 0
        for j in range(len(matrix)):
            checkSum += matrix[j][line]
        sumArr.append(checkSum)
    print()



