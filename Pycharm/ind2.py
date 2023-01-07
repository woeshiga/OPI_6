#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    s = input("Введите предложение: ")
    if 'чу' not in s and 'щу' not in s:
        print("Нет слов с буквосочетаниями чу или щу.", file=sys.stderr)
        exit(1)
    else:
        print(s.find('чу'), s.find('щу'))
        