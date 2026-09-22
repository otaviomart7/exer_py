jogadores = []
gols = []


def registrar():
    for i in range(0, 5):
        nome = input("Nome do Jogador: ")
        jogadores.append(nome)
        gol_jogador = input("Quantos gols ele fez? ")
        gols.append (int(gol_jogador))
        print("\n")


def calcularTotalGols():
    soma = 0
    for i in range(0,5):
        soma += gols[i]

    return soma
    
def calcularMediaGols():
    media = calcularTotalGols()/5

    return media


def encontrarArtilheiros():
    res = max(gols)
    indice = gols.index(res)

    artilheiro = jogadores[indice]

    return artilheiro


def mostrarRelatorio():
    for i in range(0,5):
        print(f"{jogadores[i]} - {gols[i]}")

    print(f"Total de gols do Time: {calcularTotalGols()}")
    print(f"Média de gols por Jogador: {calcularMediaGols()}")
    print(f"Artilheiro: {encontrarArtilheiros()}")




registrar()
mostrarRelatorio()


