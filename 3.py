from itertools import permutations, product

# Input
digits = list(map(int, input("Enter digits (space-separated): ").split()))
r = int(input("Enter length of permutation: "))

# Without repetition
print("\nPermutations WITHOUT repetition:")
perm_no_rep = list(permutations(digits, r))
for p in perm_no_rep:
    print(p)

# With repetition
print("\nPermutations WITH repetition:")
perm_with_rep = list(product(digits, repeat=r))
for p in perm_with_rep:
    print(p)



#WITHOUT ITERTOOLS
def permutations_with_repetition(s, length):
    result = set()

    def backtrack(current):
        if len(current) == length:
            result.add(tuple(current))
            return

        for elem in s:
            current.append(elem)
            backtrack(current)
            current.pop()

    backtrack([])   # correct placement
    return result


def permutations_without_repetition(s, length):
    result = set()

    if length > len(s):
        return result

    def backtrack(remaining, current):
        if len(current) == length:
            result.add(tuple(current))
            return

        for elem in list(remaining):
            new_remaining = remaining.copy()
            new_remaining.remove(elem)

            current.append(elem)
            backtrack(new_remaining, current)   # inside loop
            current.pop()

    backtrack(s.copy(), [])
    return result


# Input
digits = input("Enter digits separated by space (e.g. 0 1 2): ")
digit_set = set(map(int, digits.split()))
length = int(input("Enter length: "))

print("\nDigits:", digit_set)
print("Length:", length)

# WITH repetition
with_rep = permutations_with_repetition(digit_set, length)
print("\nPermutations WITH repetition:")
print("{")
for p in sorted(with_rep):
    print(p)
print("}")

# WITHOUT repetition
without_rep = permutations_without_repetition(digit_set, length)
print("\nPermutations WITHOUT repetition:")
print("{")
for p in sorted(without_rep):
    print(p)
print("}")
