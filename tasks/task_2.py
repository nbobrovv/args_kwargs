#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Решить поставленную задачу:
написать функцию, вычисляющую среднее гармоническое
своих аргументов a1, a2, ... an
Если функции передается пустой список аргументов,
то она должна возвращать значение  None
"""


def harmonic_mean(*args):
    x = 0
    for i in args:
        if i == 0:
            return "Ошибка! В функции присутствует 0"
        else:
            x += 1 / float(i)
    harmonic = 1 / (1 / len(args) * x)
    return harmonic


if __name__ == '__main__':
    try:
        arg = list(map(float, input('Введите список аргументов: ').split(' ')))
        print("Среднее гармоническое элементов: ",
              harmonic_mean(*arg))
    except ValueError:
        print(None)
