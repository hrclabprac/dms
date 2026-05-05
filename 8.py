#indegree outdegree
def input_graph(n):
    print("Enter adjacency matrix:")
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix


def compute_degrees(matrix, n):
    in_degree = [0] * n
    out_degree = [0] * n

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                out_degree[i] += 1
                in_degree[j] += 1

    return in_degree, out_degree


def display_degrees(in_degree, out_degree, n):
    print("\nVertex\tIn-degree\tOut-degree")
    for i in range(n):
        print(f"{i}\t{in_degree[i]}\t\t{out_degree[i]}")


n = int(input("Enter number of vertices: "))

matrix = input_graph(n)
in_deg, out_deg = compute_degrees(matrix, n)
display_degrees(in_deg, out_deg, n)