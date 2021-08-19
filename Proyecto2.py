# Proyecto corto discreta No.2
# Factorizando primos en Python
import numpy as np

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

print(factorizar_primos(28))  # Factores primos de 28
# Definimos la funcion para dos numeros enteros positivos, de manera que saque el mayor divisor comun
def gcd(a, b):
    if a == 0 :
        return b 
    return gcd(b%a, a)

print("Bienvenido al algoritmo de euclides, porfavor ingrese dos enteros no negativos mayores a cero \n")
a = int(input("Primero: "))
b = int(input("Segundo: "))
print("gcd(", a , "," , b, ") = ", gcd(a, b))

# Program to check if a number is prime or not

num = 407

# To take input from the user
#num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")



