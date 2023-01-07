#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    word1 = input("Введите первое слово: ")
    word2 = input("Введите второе слово: ")

    # рассмотрели первое условие:
    for symb in word2:
        if symb not in word1:
            print("NO")
            break
    else:
        print("YES")

    # рассмотрели второе условие
    for symb in word1:
        if word2.count(symb) != word1.count(symb):
            print("NO")
            break
        elif symb not in word2:
            print("NO")
            break
    else:
            print("YES")
