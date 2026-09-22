assentos = [
    ["L", "L", "L", "L", "L", "L"],
    ["L", "L", "L", "L", "L", "L"],
    ["L", "L", "L", "L", "L", "L"],
    ["L", "L", "L", "L", "L", "L"],
    ["L", "L", "L", "L", "L", "L"]
]

faturamento = [0.0]
vendas = [0, 0, 0]

def mostrarAssentos():
    print("      A   B   C   D   E   F")
    for i in range(0, 5):
        linha = f"{i + 1}   "
        for j in range(0, 6):
            linha += f" {assentos[i][j]}  "
        print(linha)
        
def validarAssento(assento):
    if(len(assento) == 2 and assento[0] in "12345" and assento[1].upper() in "ABCDEF"):
        return True
        
    return False

def pegarLinha(assento):
    return int(assento[0]) - 1

def pegarColuna(assento):
    colunas = ["A", "B", "C", "D", "E", "F"]
    return colunas.index(assento[1].upper())

def verificarDisponibilidade(assento):
    l = pegarLinha(assento)
    c = pegarColuna(assento)
    
    if(assentos[l][c] == "L"):
        return True
        
    return False

def calcularCategoria(assento):
    l = pegarLinha(assento)
    
    if(l == 0):
        return "Executiva"
    elif(l == 1 or l == 2):
        return "Espaco extra"
    else:
        return "Economica"

def calcularPreco(assento):
    l = pegarLinha(assento)
    
    if(l == 0):
        return 850.00
    elif(l == 1 or l == 2):
        return 600.00
    else:
        return 400.00

def comprarAssento():
    assento = input("Assento desejado: ")
    
    if(not validarAssento(assento)):
        print("Assento invalido.")
        return
        
    if(not verificarDisponibilidade(assento)):
        print(f"O assento {assento} ja esta ocupado.")
        print("Escolha outro assento.")
        return
        
    categoria = calcularCategoria(assento)
    preco = calcularPreco(assento)
    
    print(f"Categoria: {categoria}")
    print(f"Valor: R$ {preco:.2f}")
    
    confirmacao = input("Confirmar compra? S/N\n")
    
    if(confirmacao.upper() == "S"):
        l = pegarLinha(assento)
        c = pegarColuna(assento)
        
        assentos[l][c] = "O"
        faturamento[0] += preco
        
        if(categoria == "Executiva"):
            vendas[0] += 1
        elif(categoria == "Espaco extra"):
            vendas[1] += 1
        else:
            vendas[2] += 1
            
        print("\nCompra realizada com sucesso.")
        print(f"O assento {assento} agora esta indisponivel.")
    else:
        print("\nCompra cancelada.")

def consultarAssento():
    assento = input("Assento desejado: ")
    
    if(not validarAssento(assento)):
        print("Assento invalido.")
        return
        
    if(not verificarDisponibilidade(assento)):
        print(f"O assento {assento} ja esta ocupado.")
    else:
        print(f"O assento {assento} esta livre.")
        print(f"Categoria: {calcularCategoria(assento)}")
        print(f"Valor: R$ {calcularPreco(assento)}")

def mostrarResumo():
    livres = 0
    ocupados = 0
    
    for i in range(0, 5):
        for j in range(0, 6):
            if(assentos[i][j] == "L"):
                livres += 1
            else:
                ocupados += 1
                
    percentual = (ocupados / 30) * 100
    
    print(f"Quantidade de assentos livres: {livres}")
    print(f"Quantidade de assentos ocupados: {ocupados}")
    print(f"Percentual de ocupacao: {percentual:.2f}%")
    print(f"Faturamento total: R$ {faturamento[0]:.2f}")
    print("Vendas por categoria:")
    print(f" - Executiva: {vendas[0]}")
    print(f" - Espaco extra: {vendas[1]}")
    print(f" - Economica: {vendas[2]}")

while True:
    print("""\n1 - Visualizar assentos
2 - Comprar assento
3 - Consultar assento
4 - Mostrar resumo do voo
5 - Encerrar
""")
    opcao = int(input("Escolha uma opção: "))

    if(opcao == 1):
        mostrarAssentos()
    elif(opcao == 2):
        comprarAssento()
    elif(opcao == 3):
        consultarAssento()
    elif(opcao == 4):
        mostrarResumo()
    elif(opcao == 5):
        break
    else:
        print("Opção invalida.")