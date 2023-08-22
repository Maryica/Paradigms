# Задача 2: Поиск наименьшего числа в списке.
# Напишите программу, которая находит наименьшее число в заданном списке с помощью цикла.


listNum = [21, 43, 90, 11, 36]
minNum = listNum[0]
for i in range(len(listNum)):
    if listNum[i] < minNum:
        minNum = listNum[i]
print("Наименьшее число:  ", minNum)
