#gcd, isprime, modexp, integer rep
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def mod_exp(base, exp, mod):
    result = 1
    base = base % mod

    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2

    return result


def integer_representation(n):
    print("\nInteger Representations:")
    print("Binary:", bin(n))
    print("Octal:", oct(n))
    print("Hexadecimal:", hex(n))

while True:
    print("\n--- Number Theory Operations ---")
    print("1. GCD")
    print("2. Prime Check")
    print("3. Modular Exponentiation")
    print("4. Integer Representation")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("GCD =", gcd(a, b))

    elif choice == 2:
        n = int(input("Enter number: "))
        if is_prime(n):
            print(n, "is Prime")
        else:
            print(n, "is Not Prime")

    elif choice == 3:
        base = int(input("Enter base: "))
        exp = int(input("Enter exponent: "))
        mod = int(input("Enter modulus: "))
        print("Result =", mod_exp(base, exp, mod))

    elif choice == 4:
        n = int(input("Enter number: "))
        integer_representation(n)

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice")