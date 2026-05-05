from itertools import product
n= int(input("enter the number of variables: "))
C = int(input("enter the val of C(<=10): "))


# cartesian product function that prints every value and repeats till n 
for values in product(range(C+1), repeat=n):
    if(sum(values)==C): #generates a tuple
        print(values)

#generates all the combinations
# filter out the possible solutions with C
# follows the brute force