#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    s = input("Введите слово, оканчивающее символом «.»: ")
    symb = input("Введите букву: ")
    num = int(input("Введите номер: "))

    if s[-1] != '.':
        print("Слово не оканчивается на «.»", file=sys.stderr)
        exit(1)
    if num > len(s):
        print("Буквы с таким номером в слове нет", file=sys.stderr)
    else:
        print(s[:num+1] + symb + s[num+1:])
