import math
import os

printSteps = True

def drawASCII():
    file = open("ascii.txt")
    for line in file:
        print(line.strip("\n"))
    file.close

def topow( x, y ):
    value = 1
    for i in range(0, y):
        value *= x
    return value

def pause():
    input("\nPress enter to continue...")
    os.system("cls")

def brute_force_prime( n ):
    if n == 1:
        return True

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def getN( constant ):
    valid = False
    while not valid:
        try:
            n = int(input("\nEnter value for " + constant + ": "))
            valid = True
            print("")
            return n
        except ValueError:
            print("Invalid input")
            valid = False

def find_primes():
    n = getN("n")
    for i in range(1, n):
        if brute_force_prime(i):
            print(str(i) + " is prime;")
    pause()    

def check_brute_force():
    n = getN("P")
    if brute_force_prime( n ):
        print(str(n) + " is prime by the brute force test.")
    else:
        print(str(n) + " is not prime by the brute force test.")
    pause()

def check_wilson_theorem():
    n = getN("P")
    print("By the Wilson Theorem: (P-1)! + 1 is divisible by P\n")
    value = math.factorial(n - 1) + 1
    print("\n(" + str(n) + "-1)! + 1 = " + str(value))
    if value % n == 0:
        print("\n" + str(value) + " is divisible by " + str(n))
        print("\nTherefore: " + str(n) + " is prime by the Wilson Theorem.")
    else:
        print("\n" + str(value) + " is not divisible by " + str(n))
        print("\nTherefore: " + str(n) + " is not prime by the Wilson Theorem.")
    pause()

def check_wilson_prime():
    n = getN("P")
    print("By the Wilson Theorem: (P-1)! + 1 is divisible by P\n")
    value = math.factorial(n - 1) + 1
    print("\n(" + str(n) + "-1)! + 1 = " + str(value))
    if printSteps:
        print("\n(" + str(n) + "-1)! + 1 = " + str(value))
    if value % n == 0:
        print("\n" + str(value) + " is divisible by " + str(n))
        print("\n" + str(value) + " / " + str(n) + " = " + str(value / n))
        value = int(value / n)
        if value % n == 0:
            print("\n" + str(value) + " is divisible by " + str(n))
            print("\nTherefore: " + str(n) + " is a Wilson Prime.")
        else:
            print("\n" + str(value) + " is not divisible by " + str(n))
            print("\nTherefore: " + str(n) + " is not a Wilson Prime.")
    else:
        print("\n" + str(value) + " is not divisible by " + str(n))
        print("\nTherefore: " + str(n) + " is not a Wilson Prime.")
    pause()

def check_fermat_theorem():
    global printSteps
    p = getN("P")
    isPrime = True
    if printSteps:
        print("By Fermat's Theorem: a^P - a is divisible by P\n")
    for a in range(1, p + 1):
        value = (topow(a, p) - a)
        if printSteps: 
            print(str(a) + "^" + str(p) + " - " + str(a) + " = " + str(value))
        if value % p == 0:
            if printSteps:
                print(str(value) + " is divisible by " + str(p))
        else:
            if printSteps:
                print(str(value) + " is not divisible by " + str(p))
            isPrime = False
            break
        if printSteps:
            print("\n")
    if isPrime:
        print("Therefore: " + str(p) + " is prime by Fermat's Little Theorem.")
        if not brute_force_prime(p):
            print("However, " + str(p) + " isn't a prime number.")
            print("Therefore, " + str(p) + " is a Carmichael Number.")
    else:
        print("Therefore: " + str(p) + " is not prime by Fermat's Little Theorem.")
    pause()

def main():
    global printSteps
    option = ""
    while option != "q":
        drawASCII()
        print("\nA: Find primes from 0 to n")
        print("B: Check if digit is prime by brute force")
        print("C: Check if digit is prime by Fermat's Little Theorem")
        print("D: Check if digit is prime by Wilson's Theorem")
        print("E: Check if digit is a Wilson Prime")
        print("F: Check if digit is prime by AKS Test")
        print("Q: Quit")

        option = input("\nOption: ").lower()

        if option == "a":
            find_primes()
        elif option == "b":
            check_brute_force()
        elif option == "c":
            check_fermat_theorem()
        elif option == "d":
            check_wilson_theorem()
        elif option == "e":
            check_wilson_prime()
        elif option == "f":
            print ("fdfkjsdfk")
        elif option == "p":
            printSteps = not printSteps
            if printSteps:
                print("\nPrinting steps...")
            else:
                print("\nNot printing steps...")
            pause()
        elif option == "q":
            pause()
        else:
            print("Invalid option \"" + option + "\"")
            pause()

main()
