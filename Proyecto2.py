# Proyecto corto discreta No.2
# Factorizando primos en Python
import numpy as np
# Funciones a utilizar

def gcd(a, b):
    if a == 0 :
        return b 
    return gcd(b%a, a)

def criba_eratostenes(n):
    """Criba Eratostenes"""
    l=[]
    multiplos = set()
    for i in range(2, n+1):
        if i not in multiplos:
            l.append(i)
            multiplos.update(range(i*i, n+1, i))
    return l

def factorizar_primos(n): 
    """Factoriza un entero positivo en primos
    
    >>>factorizar_primos(28)
    [2, 2, 7]
    """
    if n <=1:
        return "Ingresar un entero mayor a 1"
                
    factores = []
    primos = criba_eratostenes(n)
    pindex = 0
    p = primos[pindex]
    num = n
    
    while p != num:
        if num % p == 0:
            factores.append(p)
            num //= p
        else:
            pindex += 1
            p = primos[pindex]
            
    factores.append(p)
    
    return factores

#EJERCICIO 1

# Program to check if a number is prime or not

#num = 407

# To take input from the user
num = int(input("Ingrese un numero: "))

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2,num):
        if (num % i) == 0:
            print(num,"no es un numero primo")
            print(i,"veces",num//i,"es",num)
            break
    else:
        print(num,"es un numero primo")
        
# if input number is less than
# or equal to 1, it is not prime
else:
    print(num,"no es un numero primo")

# EJERCICIO 2
print(factorizar_primos(28))  # Factores primos de 28

# Definimos la funcion para dos numeros enteros positivos, de manera que saque el mayor divisor comun

# EJERCICIO 3
print("Bienvenido al algoritmo de euclides, porfavor ingrese dos enteros no negativos mayores a cero \n")
a = int(input("Primero: "))
b = int(input("Segundo: "))
print("gcd(", a , "," , b, ") = ", gcd(a, b))




