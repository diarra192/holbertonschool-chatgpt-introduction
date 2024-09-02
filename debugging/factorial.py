#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Décrémenter n à chaque itération
    return result

if len(sys.argv) > 1:
    try:
        f = factorial(int(sys.argv[1]))
        print(f)
    except ValueError:
        print("Veuillez entrer un entier valide.")
else:
    print("Veuillez fournir un argument.")

