
INF = 999999

def printme(final, file):
    for i in range(0, len(final)):
        first = final[i][0] + 1
        second = final[i][1] + 1
        if(first > second):
            file.write("(" + str(second) + ", " + str(first) + ") ")
            print("(", second,", ",first,")", end=' ', sep='')
        else:
            file.write("(" + str(first) + ", " + str(second) + ") ")
            print("(", first,", ",second,")", end=' ',sep='')
    print()

def min_elem(G, vis):
    m = INF
    ind = INF
    to_rep = INF
    for i in vis:
        tmp = min(G[i])
        cur_ind = G[i].index(tmp)
        if (m == INF or tmp <= m) and cur_ind not in vis:
            m = tmp
            ind = G[i].index(tmp)
            to_rep = i
    return [m, ind, to_rep]

def prim(G, start, size):

    to_visit = [] #amount of times we need to visit 
    for i in range(0, size):
        to_visit.append(i)
    visited = []
    check = to_visit
    visited.append(start)  # easier to understand
    check.remove(start)

    for j in range(0, len(G)):
        G[j][start] = INF
    all_weight = 0
    final =[]
    weight_matrix =[]
    for i in range(0, size):
        row = []
        for j in range(0, size):
            row.append(0)
        weight_matrix.append(row)

    for i in range(0, size-1):
        m, ind, to_rep = min_elem(G, visited) # m - min elem in G[X], ind == elem of min elem in G[X]
        if m == INF:
            ind = check[0]
            visited.append(ind)
            check.remove(ind)
            for j in range(0, len(G)):
                G[j][ind] = INF
            continue
        all_weight+= int(m)
        for j in range(0, len(G)):
            G[j][ind] = INF
        check.remove(ind)
        final.append([to_rep, ind])
        weight_matrix[to_rep][ind] = 1
        weight_matrix[ind][to_rep] = 1

        visited.append(ind)

    print(all_weight)
    for line in weight_matrix:
        print(line)
    with open ("input.out", "w") as Out:
        Out.write(str(all_weight) + '\n')
        for i in range(0, len(weight_matrix)):
            for j in range(0, len(weight_matrix[i])):
                if( j == len(weight_matrix[i]) - 1):
                    Out.write(str(weight_matrix[i][j]))
                else:
                    Out.write(str(weight_matrix[i][j]) + ', ')
            Out.write('\n')
        printme(final, Out)


if __name__ == '__main__':
    inp = "input.in"
    with open(inp, "r") as myFile:
        size, alg_type, node = myFile.readline().split() # node - node to start from
        G = myFile.readlines()     # alg_type - Prim's alg
        for i in range(int(size)):                       # size - amount of nodes
            G[i] = (G[i].rstrip()).split(' ')[:int(size)]
        G=G[:int(size)] 
    node = int(node)
    alg_type = int(alg_type)
    size = int(size)

    for i in range(0, len(G)):
        G[i] = [int(x) for x in G[i]]
    for i in range(0, len(G)):
        for j in range(0, len(G[i])):
            if G[i][j] == 0:
                G[i][j] = INF
    prim(G, node-1, size) # -1 because numeration starts with 0

   
