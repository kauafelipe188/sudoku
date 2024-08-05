def pode_adicionar(sudoku, linha, coluna, numero):
    for i in range(9):
        if sudoku[linha][i] == numero:
            return False
    for i in range(9):
        if sudoku[i][coluna] == numero:
            return False
    return True

def adicionar_numero(sudoku, linha, coluna, numero):
    if linha < 0 or linha >= 9 or coluna < 0 or coluna >= 9:
        print("Posição inválida")
        return
    if pode_adicionar(sudoku, linha, coluna, numero):
        sudoku[linha][coluna] = numero
        print(f"Número {numero} adicionado à posição ({linha}, {coluna})")
    else:
        print("Ação inválida: número já existe na linha ou coluna")

def exibir_sudoku(sudoku):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if j == 8:
                print(sudoku[i][j])
            else:
                print(f"{sudoku[i][j]} ", end="")

def variaveis():
    linha = int(input("Digite a linha (0-8): "))
    coluna = int(input("Digite a coluna (0-8): "))
    numero = int(input("Digite o número (1-9): "))
    return linha, coluna, numero

sudoku = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

linha, coluna, numero = variaveis()
adicionar_numero(sudoku, linha, coluna, numero)
exibir_sudoku(sudoku)