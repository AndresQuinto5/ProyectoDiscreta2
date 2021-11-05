import random
import sys
import math
import textwrap

from random import randrange

primesBelowFourDigits =   [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97
                            ,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179
                            ,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269
                            ,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367
                            ,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461
                            ,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571
                            ,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661
                            ,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773
                            ,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883
                            ,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997]


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def rabinMillerTest(n, k=10):

    if n == 2:
        return True
    if not n & 1:
        return False


    def check(a, s, j, n):
        x = pow(a, j, n)
        if x == 1:
            return True
        for j in range(1, s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1

    s = 0
    j = n - 1

    while j % 2 == 0:
        j >>= 1
        s += 1

    for j in range(1, k):
        a = randrange(2, n - 1)
        if not check(a, s, j, n):
            return False
    return True


def isPrime(n):
    
    if (n >= 3):
        if (n & 1 != 0):
            for p in primesBelowFourDigits:
                if (n == p):
                    return True
                if (n % p == 0):
                    return False
            return rabinMillerTest(n)
    return False


def generateLargePrime(k):
    r = 100*(math.log(k, 2)+1)  
    attempts = r
    while r > 0:
        n = random.randrange(2**(k-1), 2**(k))
        r -= 1
        if isPrime(n) == True:
            return n

    failure = "There's a failure, you have done " + str(attempts) + "attempts."
    return failure


def multInverse(a, b):
    x = 0
    ly = 0
    y = 1
    lx = 1
    original_a = a  
    original_b = b  


    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lx) = ((lx - (q * x)), x)
        (y, ly) = ((ly - (q * y)), y)
    if lx < 0:
        lx += original_b  
    if ly < 0:
        ly += original_a  

    return lx


def multiply(x, y):
    _CUTOFF = 1536
    if x.bit_length() <= _CUTOFF or y.bit_length() <= _CUTOFF: 
        return x * y
    else:
        n = max(x.bit_length(), y.bit_length())
        half = (n + 32) // 64 * 32
        mask = (1 << half) - 1
        xlow = x & mask
        ylow = y & mask
        xhigh = x >> half
        yhigh = y >> half

        a = multiply(xhigh, yhigh)
        b = multiply(xlow + xhigh, ylow + yhigh)
        c = multiply(xlow, ylow)
        j = b - a - c
        return (((a << half) + j) << half) + c


def generateKeypair(keySize=10):
    p = generateLargePrime(keySize)

    q = generateLargePrime(keySize)


    if p == q:
        raise ValueError('p and q cannot be equal')

    n = multiply(p, q)

    z = multiply((p-1), (q-1))

    k = random.randrange(1, z)

    g = gcd(k, z)


    while g != 1:
        k = random.randrange(1, z)
        g = gcd(k, z)


    j = multInverse(k, z)

    return ((k, n), (j, n))


def encrypt(privateKey, plainText):

    key, n = privateKey

    cipher = [(ord(char) ** key) % n for char in plainText]

    return cipher


def decrypt(publicKey, ciphertext):

    key, n = publicKey

    plain = [chr(pow(char, key, n)) for char in ciphertext]

    return ''.join(plain)



wantsToContinue1= True
print("******************************************************")
print("------ WELCOME TO OUR RSA Encripter/Decripter ------\n")
print("******************************************************")
    
print("Generating recommended public/private keypairs . . .")
public, private = generateKeypair()
print("PUBLIC KEY: ", public, " - PRIVATE KEY: ", private, "\n\n")

while(wantsToContinue1==True):
    
    print("Please choose one of the following options:\n 1) Encode a message\n 2) Decode a message\n 3) Exit")
    choosedOption= int(input("> "))

    if(choosedOption==1):
        message = input("Please type the MESSAGE you want to encrypt: ")
        keypair= input("Please type the PRIVATE KEY, comma separated (example: 15,20): ")
        result = [x.strip() for x in keypair.split(',')]

        privateKey = int(result[0]), int(result[1])        
        encryptedMessage = encrypt(privateKey, message)

        print("Encrypted message is: ")
        print(','.join(map(lambda x: str(x), encryptedMessage)))
    
    elif(choosedOption==2):
        encryptedMessage = input("Please type the MESSAGE you want to decrypt: ")
        keypair= input("Please type the PUBLIC KEY, comma separated (example: 20,15): ")
        result = [x.strip() for x in keypair.split(',')]

        publicKey = int(result[0]), int(result[1]) 

        #Converting crypted text to array of bytes
        encryptedMessage = [x.strip() for x in encryptedMessage.split(',')]
        bytesCrypted = [int(i) for i in encryptedMessage]

        print("Decrypted message is:")
        print(decrypt(publicKey, bytesCrypted))

    elif(choosedOption==3):
        print("BYE...")
        wantsToContinue1= False