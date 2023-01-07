#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input("Введите предложение: ")
    symb = list(s[2::3])
    print('\n'.join(symb))
