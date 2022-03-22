import math
import random

# Zad 1

# A = []
# A = [1-x for x in range(1,11)]
# print(A)

# B = []
# B = [4 ** x for x in range(0,8)]
# print(B)

# C = []
# for x in B:
#     if x % 2 == 0:
#         C.append(x)
# print(C)

# Zad 2

# lista1 = [random.randint(0,20) for x in range(0,11)]
# print(lista1)

# lista2 = [x for x in lista1 if x % 2 == 0]
# print(lista2)

# Zad 3

# slowniczek = {"Masło": "Wiaderka", "Bułka": "Na wage", "Chlebek": "Kromki"}
# print(slowniczek)
#
# slowniczek_do_gury_noga={value:key for key, value in slowniczek.items()}
# print(slowniczek_do_gury_noga)

# Zad 4

# def trujkacik(a, b, c):
#     if a ** 2 + b ** 2 == c ** 2:
#         print('Trójkąt prostokątny')
#         return 1
#     if a ** 2 + b ** 2 != c ** 2:
#         print('Trójkąt nie jest prostokątny')
#         return 0
# print(trujkacik(3,4,5))
# print(trujkacik(7,7,7))

# Zad 5

# def trapezik(a=3, b=4, h=5):
#     return (((a+b)*h)/2)
# print(trapezik())

# Zad 6

# def ciag(a=1, b=4, ile=10):
#     for x in range(ile):
#         a = a * b
#     return a
# print(ciag())

# Zad 7

# def ciag(* liczby):
#     suma = 1
#     for x in liczby:
#         suma*=x
#     return suma
# print(ciag(4,4,4,4))

# Zad 8

# def zakupy(** rzeczy):
#     ile = str()
#     for x in rzeczy:
#         ile+=x
#     return ile
# zakupy(czekolada='5zł', gra='100zł', kebs='14zł')
