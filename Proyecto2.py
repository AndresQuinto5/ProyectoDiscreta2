# Proyecto corto discreta No.2
# Definimos la funcion para dos numeros enteros positivos, de manera que saque el mayor divisor comun
def gcd(a, b):
    if a == 0 :
        return b 
    return gcd(b%a, a)

print("Bienvenido al algoritmo de euclides, porfavor ingrese dos enteros no negativos mayores a cero \n")
a = int(input("Primero: "))
b = int(input("Segundo: "))
print("gcd(", a , "," , b, ") = ", gcd(a, b))
