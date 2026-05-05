# check if a graph is complete using adjoint matrix

def is_complete_graph(adj_matrix):
    n = len(adj_matrix)
    for i in range(n):
        for j in range(n):
            if i == j:
                # Diagonal must be 0
                if adj_matrix[i][j] != 0:
                    return False
            else:
                # Non-diagonal must be 1
                if adj_matrix[i][j] != 1:
                    return False
    return True


n = int(input("Enter number of vertices: "))
print("Enter adjacency matrix:")

adj_matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    adj_matrix.append(row)

# Check
if is_complete_graph(adj_matrix):
    print("The graph is a COMPLETE graph.")
else:
    print("The graph is NOT a complete graph.")