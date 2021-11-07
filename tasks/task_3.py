#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Найти среднее арифметическое чисел.
"""


def arithmetic(**kwargs):
    x = 0
    k = 0
    len_of = len(kwargs)
    for numbers in kwargs.values():
        x += float(numbers)
    sum_of = x / len_of

    for n in kwargs.values():
        k += float(n)
    tip = k
    print(f"Сумма чисел: {tip}")
    print('Среднее арифметическое чисел: ', sum_of)


if __name__ == '__main__':
    arithmetic(a=5, b=10, c=4, d=1)