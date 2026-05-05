class RELATION:
    def __init__(self, n):
        self.n = n
        self.matrix = []

    def input_relation(self):
        print("Enter relation matrix (row-wise, space separated):")
        for i in range(self.n):
            row = list(map(int, input().split()))
            if len(row) != self.n:
                raise ValueError("Row size must be equal to n")
            self.matrix.append(row)

    def display(self):
        print("the relation matrix is:")
        for row in self.matrix:
            print(*row)

    def is_reflexive(self):
        for i in range(self.n):
            if self.matrix[i][i] != 1:
                return False
        return True

    def is_symmetric(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.matrix[i][j] != self.matrix[j][i]:
                    return False
        return True

    def is_antisymmetric(self):
        for i in range(self.n):
            for j in range(self.n):
                if i != j and self.matrix[i][j] == 1 and self.matrix[j][i] == 1:
                    return False
        return True

    def is_transitive(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.matrix[i][j] == 1:
                    for k in range(self.n):
                        if self.matrix[j][k] == 1 and self.matrix[i][k] != 1:
                            return False
        return True

    def relation_type(self):
        reflexive = self.is_reflexive()
        symmetric = self.is_symmetric()
        antisymmetric = self.is_antisymmetric()
        transitive = self.is_transitive()

        print("\nProperties:")
        print("Reflexive:", reflexive)
        print("Symmetric:", symmetric)
        print("Anti-symmetric:", antisymmetric)
        print("Transitive:", transitive)

        if reflexive and symmetric and transitive:
            print("\nThe relation is an Equivalence Relation.")
        elif reflexive and antisymmetric and transitive:
            print("\nThe relation is a Partial Order Relation.")
        else:
            print("\nThe relation is neither equivalence nor partial order.")


n = int(input("Enter number of elements in set: "))
R = RELATION(n)

R.input_relation()
R.display()
R.relation_type()