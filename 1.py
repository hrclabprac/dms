

class SET:
    def __init__(self):
        self.elements = []

    def input_set(self):
        n = int(input("enter the no. of elements: "))
        self.elements = []
        print("enter elements:")
        for _ in range(n):
            val = int(input())
            if val not in self.elements:
                self.elements.append(val)

    def display(self):
        print("{", *self.elements, "}")

    def is_member(self, val):
        return val in self.elements

    def union(a, b):
        result = SET()
        result.elements = a.elements.copy()
        for e in b.elements:
            if e not in result.elements:
                result.elements.append(e)
        return result

    def intersection(a, b):
        result = SET()
        for e in a.elements:
            if e in b.elements:
                result.elements.append(e)
        return result

    def is_subset(a, b):
        for e in a.elements:
            if e not in b.elements:
                return False
        return True

    def difference(a, b):
        result = SET()
        for e in a.elements:
            if e not in b.elements:
                result.elements.append(e)
        return result

    def symmetric_difference(a, b):
        d1 = SET.difference(a, b)
        d2 = SET.difference(b, a)
        return SET.union(d1, d2)

    def complement(universal, a):
        return SET.difference(universal, a)

    def power_set(self):
        n = len(self.elements)
        total = 1 << n
        print("power Set:")
        for i in range(total):
            subset = []
            for j in range(n):
                if i & (1 << j):
                    subset.append(self.elements[j])
            print("{", *subset, "}")

    def cartesian_product(a, b):
        print("{ ", end="")
        for x in a.elements:
            for y in b.elements:
                print(f"({x},{y})", end=" ")
        print("}")


A = SET()
B = SET()
U = SET()

while True:
    print("\n SET OPERATIONS - PROGRAM CODED BY VEDANT SHARMA.")
    print("1.Input Set A")
    print("2.Input Set B")
    print("3.Input Universal Set")
    print("4.Check Membership in A")
    print("5.Power Set of A")
    print("6.Check if A subset of B")
    print("7.Union")
    print("8.Intersection")
    print("9.Complement of A")
    print("10.Difference (A-B)")
    print("11.Symmetric Difference")
    print("12.Cartesian Product")
    print("0.Exit")
    a = set()
    b=set()
    print(a.union)
    choice = int(input("enter your choice: "))

    if choice == 1:
        A.input_set()

    elif choice == 2:
        B.input_set()

    elif choice == 3:
        U.input_set()

    elif choice == 4:
        val = int(input("Enter element: "))
        print("the element is present" if A.is_member(val) else "the element is not present")

    elif choice == 5:
        A.power_set()

    elif choice == 6:
        print("A is a subset of B" if SET.is_subset(A, B) else "A is NOT a subset of B")

    elif choice == 7:
        res = SET.union(A, B)
        print("union =", end=" ")
        res.display()

    elif choice == 8:
        res = SET.intersection(A, B)
        print("intersection =", end=" ")
        res.display()

    elif choice == 9:
        res = SET.complement(U, A)
        print("complement of A =", end=" ")
        res.display()

    elif choice == 10:
        res = SET.difference(A, B)
        print("A - B =", end=" ")
        res.display()

    elif choice == 11:
        res = SET.symmetric_difference(A, B)
        print("symmetric Difference =", end=" ")
        res.display()

    elif choice == 12:
        print("cartesian Product:")
        SET.cartesian_product(A, B)

    elif choice == 0:
        print("program ended.")
        break

    else:
        print("invalid choice")