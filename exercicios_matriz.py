def imprimir_matriz(Matriz,n,m):
    i = 0
    while i < n:
        j = 0
        while j < m:
            print(Matriz[i][j], end=' ')
            j += 1
        print()
        i += 1

def criar_matriz(Matriz,n,m):
    i = 0
    while i<n:
        print(f"Digite os elementos da linha {i}")
        j = 0
        linha = [] #guarda os elementos da linha i
        while j<m:
            elem = int(input())
            linha.append(elem)
            j+=1
        Matriz.append(linha) #insere linha i na matriz
        i+=1

def exercicio_1(lin, col):
    matriz = []
    criar_matriz(matriz,lin,col)
    maior = matriz[0][0]
    for i in range(lin):
        for j in range(col):
            if maior < matriz[i][j]:
                maior = matriz[i][j]
    print(maior)

def exercicio_2(dimensao):
    matriz = []
    lin = dimensao
    col = dimensao
    igual = True
    criar_matriz(matriz, lin, col)
    i = 0
    j = 0
    while i < lin and igual == True:
        while j < col and igual == True:
            if matriz[j][i] == matriz[i][j]:
                igual = True
            else:
                igual = False
            j += 1
        i += 1
    if igual == True:
        print("A matriz é simétrica!")
    else:
        print("A matriz não é simétrica")

def exercicio_3(dimensao):
    matriz = []
    lin = dimensao
    col = dimensao
    criar_matriz(matriz, lin, col)
    i = 0
    j = 0
    print("Matriz original:")
    imprimir_matriz(matriz, lin, col)
    print()
    while i < lin:
        while j < col:
            (matriz[i][j], matriz[j][i]) = (matriz[j][i], matriz[i][j])
            j += 1
        i += 1
    print("Matriz transposta:")
    imprimir_matriz(matriz, lin, col)

def exercicio_4(dimensao):
    matriz = []
    i = 0
    j = 0
    identidade = True
    lin = dimensao
    col = dimensao
    criar_matriz(matriz, lin, col)
    while i < lin and identidade == True:
        while j < col and identidade == True:
            if i == j:
                if matriz[i][j] == 1:
                    identidade = True
                else:
                    identidade = False
            else:
                if matriz[i][j] == 0:
                    identidade = True
                else:
                    identidade = False
            j += 1
        i += 1
    print(identidade)

def exercicio_5(lin, col):
    matriz = []
    criar_matriz(matriz,lin,col)
    linhas_nulas = 0
    colunas_nulas = 0
    for linha in matriz:
        linha_nula = True
        for elem in linha:
            if elem != 0:
                linha_nula = False
                break
        if linha_nula == True:
            linhas_nulas += 1

    for coluna in range(len(matriz[0])):
        coluna_nula = True
        for linha in range(len(matriz)):
            if matriz[linha][coluna] != 0:
                coluna_nula = False
                break
        if coluna_nula == True:
            colunas_nulas += 1
    print(colunas_nulas + linhas_nulas)

def exercicio_6():
    lin1 = int(input("Digite quantas linhas tem a 1ª matriz: "))
    col1 = int(input("Digite quantas colunas tem a 1ª matriz: "))
    matriz1 = []
    criar_matriz(matriz1, lin1, col1)
    col2 = int(input("Digite quantas colunas tem a 2ª matriz: "))
    lin2 = col1
    matriz2 = []
    criar_matriz(matriz2, lin2, col2)
    matriz_final = []
    i = 0
    while i < lin1:
        j = 0
        linha = [] #guarda os elementos da linha i
        m = 0
        n = 0
        while j < col2:
            elem = 0
            while n < lin2:
                elem += ((matriz1[i][n]) * (matriz2[n][j]))
                n += 1
            linha.append(elem)
            n = 0
            m += 1
            j+=1
        matriz_final.append(linha) #insere linha i na matriz
        linha = []
        i+=1
    print(matriz_final)





                    
def main():
    print("Selecione o exercício a ser consultado:")
    print("1. Maior elemento da matriz")
    print("2. Matriz simétrica")
    print("3. Matriz transposta")
    print("4. Matriz identidade")
    print("5. Nulos")
    print("6. Produto de matrizes")
    print("0. Sair")
    op = int(input("Escolha uma opção (0-6): "))
    if op == 1 or op == 5:
        lin = int(input("Digite quantas linhas tem a matriz: "))
        col = int(input("Digite quantas colunas tem a matriz: "))
        if op == 1:
            exercicio_1(lin, col)
        else:
            exercicio_5(lin, col)
    elif op == 2 or op == 3 or op == 4:
        dimensao = int(input("Digite as dimensões da raiz quadrada: "))
        if op == 2:
            exercicio_2(dimensao)
        elif op == 3:
            exercicio_3(dimensao)
        elif op == 4:
            exercicio_4(dimensao)
    elif op == 6:
        exercicio_6()
    elif op == 0:
        print("Saindo...")
        print()
    else:
        print("Opção inválida")
        print()
        main()

main()