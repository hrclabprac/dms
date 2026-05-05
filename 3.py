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