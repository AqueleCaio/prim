def prim(matriz):
    V = len(matriz)
    S = [0]*V
    N = 0
    S[0] = True
    T = []
    custo_total = 0
    while (N < V - 1):
        minimum = float('Inf')
        x = 0
        y = 0
        for i in range(V):
            if S[i]:
                for j in range(V):
                    if ((not S[j]) and matriz[i][j]):  
                        if minimum > matriz[i][j]:
                            minimum = matriz[i][j]
                            x = i
                            y = j
        T.append((x, y))
        custo_total += matriz[x][y]
        S[y] = True
        N += 1
    print(T, custo_total) 
