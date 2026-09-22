tentativas = []

def registrarTentativas():
    for i in range(0,10):
        arremesso = int (input(f"Seu {i+1}º arremesso valeu quantos pontos? (0,1,2,3):\n"))
        if (arremesso > 3 or arremesso < 0 ):
            print("Número Inválido")
        else:
            tentativas.append(arremesso)

def calcularPontuacao():
    total = sum(tentativas)

    return total

def calcularAproveitamento():
    total = calcularPontuacao()
    aproveitamento = total/30

    return aproveitamento*100


def encontrarCestaMaisFrequente():
    mais_frequente = max(set(tentativas), key=tentativas.count)

    return mais_frequente

    
registrarTentativas()
print(f"Pontuação total: {calcularPontuacao()}")
print(f"Aproveitamento: {calcularAproveitamento()}%")
print(f"Cesta mais Frequente: {encontrarCestaMaisFrequente()}")
