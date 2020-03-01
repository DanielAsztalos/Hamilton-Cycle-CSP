import sys
import numpy as np

class Node:
    def __init__(self, N):
        self.domain = []
        self.value = -1

    def add_to_domain(self, idx):
        self.domain.append(idx)
        self.domain.sort()

    def remove_from_domain(self, idx):
        self.domain.remove(idx)

    def set_value(self, val):
        self.value = val
    
    def get_domain_count(self):
        return len(self.domain)
    
    def __str__(self):
        return str(self.domain)

def exist_duplicates(lst):
    global N
    cnt = [0] * N
    for elm in lst:
        cnt[elm] += 1
    for elm in cnt:
        if elm > 1:
            return True
    return False


def are_neighbours(adj, sol):
    for i in range(len(sol) - 1):
        if adj[sol[i]][sol[i + 1]] == 0:
            return False
    return True


def is_solution(adj, sol):
    '''Helper function that checks if a given state is a solution'''
    if not exist_duplicates(sol) and \
            adj[sol[0]][sol[-1]] == 1 and are_neighbours(adj, sol):
        return True
    return False
    

def plain_backtrack(sol, i):
    global adj_mat
    global num_assig
    
    if i == N:
        if is_solution(adj_mat, sol):
            print(sol)
            return True
        else:
            return False

    num_assig += 1
    for n in range(N):
        sol[i] = n
        if plain_backtrack(sol, i + 1) == True:
            return True
        sol[i] = -1
    return False

def forward_check(nodes, i):
    for neigh in nodes[i].domain:
        nodes[neigh].remove_from_domain(i)

def backward_check(nodes, i):
    for neigh in nodes[i].domain:
        nodes[neigh].add_to_domain(i)

def get_interval(nodes, i, sol):
    if i == 0:
        lista = [j for j in range(N)]
    else:
        lista = nodes[sol[i - 1]].domain
    lista.sort(key=lambda x: nodes[x].get_domain_count())
    return lista

    
def mvr_fc(sol, i, nodes):
    global adj_mat
    global num_assig
    
    if i == N:
        if is_solution(adj_mat, sol):
            return True
        else:
            return False
    num_assig += 1
    var = get_interval(nodes, i, sol)
    for n in var:
        sol[i] = n
        forward_check(nodes, n)
        if mvr_fc(sol, i + 1, nodes) == True:
            return True
        backward_check(nodes, n)
        sol[i] = -1
    return False

def ac3(sol, i, nodes):
    global adj_mat
    for j, node in enumerate(adj_mat[sol[i]]):
        if adj_mat[sol[i]][j] == 1:
            nodes[j].remove_from_domain(sol[i])

    if i == N - 2:
        for j in sol[i].domain:
            if adj_mat[j][sol[0]] != 1:
                nodes[sol[i]].remove_from_domain(j)

def mvr_ac3(sol, i, nodes):
    global adj_mat
    global num_assig
    
    if i == N:
        if is_solution(adj_mat, sol):
            return True
        else:
            return False
    num_assig += 1
    var = get_interval(nodes, i, sol)
    for n in var:
        sol[i] = n    
        ac3(sol, i, nodes)    
        if mvr_fc(sol, i + 1, nodes) == True:
            return True
        sol[i] = -1
    return False

    
def create_domains(nodes):
    for i in range(len(adj_mat)):
        for j in range(len(adj_mat[i])):
            if adj_mat[i][j] == 1:
                nodes[i].add_to_domain(j)
    return nodes
                

N = 5
adj_mat = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]

num_assig = 0

def generate_graph():
    global adj_mat
    adj_mat = list(np.random.randint(2, size=(N * N)).reshape(N, N))
    for i, row in enumerate(adj_mat):
        adj_mat[i] = list(row)
    
    for i in range(N):
        for j in range(i, N):
            if i == j:
                adj_mat[i][j] = 0
            else:
                adj_mat[j][i] = adj_mat[i][j]
    print(adj_mat)

def main():
    if not len(sys.argv) == 3:
        print("Expected 2 arguments got {}!".format(len(sys.argv) - 1))
        return
    if not int(sys.argv[2]) in [1, 2, 3]:
        print("Second argument must be one of the following values: 1, 2, 3!")
        return
    
    N = int(sys.argv[1])
    generate_graph()
    solution = [-1] * N

    strategy = int(sys.argv[2])

    if strategy == 1:
        plain_backtrack(solution, 0)
        print(num_assig)
    elif strategy == 2:
        nodes = [Node(N) for x in range(N)]
        nodes = create_domains(nodes)

        mvr_fc(solution, 0, nodes)
        print(num_assig)
    elif strategy == 3:
        nodes = [Node(N) for x in range(N)]
        nodes = create_domains(nodes)

        mvr_ac3(solution, 0, nodes)
        print(num_assig)


main()