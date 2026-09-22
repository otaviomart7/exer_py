nomes = []
precos = []
estoques = []

def registrar():
    for i in range(0, 5): 
        nome = input("Qual o nome do medicamento?\n")
        nomes.append(nome)

        preco = input("Qual o preco do medicamento?\n")
        precos.append(float(preco))

        estoque = input("Qual a quantidade em estoque?\n")
        estoques.append(int(estoque))
        print("\n")

def listarMedicamentos():
    for i in range(0, 5): 
        print(f"{nomes[i]} - {precos[i]} - Estoque: {estoques[i]}")

def pesquisarMedicamento():
    nomePesquisa = input("Qual o nome do medicamento?\n")
    acheipae = False

    for i in range(0, 5): 
        if(nomes[i].lower() == nomePesquisa.lower()):
            print(f"{nomes[i]} - R$ {precos[i]} - Estoque: {estoques[i]}")
            acheipae = True
            break

    if(not acheipae):
        print("Medicamento não encontrado")

def registrarVenda():
    nomePesquisa = input("Qual o nome do medicamento?\n")
    indexEncontrado = -1

    for i in range(0, 5): 
        if(nomes[i].lower() == nomePesquisa.lower()):
            indexEncontrado = i
            break

    if(indexEncontrado == -1):
        print("Medicamento nao encontrado")
        return

    qtd = int(input("Qual a quantidade vendida?\n"))

    if(qtd <= 0):
        print("Quantidade invalida")
        return

    if(qtd > estoques[indexEncontrado]):
        print("Estoque insuficiente")
    else:
        estoques[indexEncontrado] -= qtd
        print("Venda realizada com sucesso!")

def reporEstoque():
    nomePesquisa = input("Qual o nome do medicamento?\n")
    indexresenhudo = -1

    for i in range(0, 5): 
        if(nomes[i].lower() == nomePesquisa.lower()):
            indexresenhudo = i
            break

    if(indexresenhudo == -1):
        print("Medicamento não encontrado")
        return

    qtd = int(input("Qual a quantidade para repor?\n"))

    if(qtd <= 0):
        print("Quantidade invalida")
        return

    estoques[indexresenhudo] += qtd
    print("Estoque reposto com sucesso!")

def verificarEstoqueBaixo():
    print("Medicamentos com estoque baixo : ")
    temEstoqueBaixo = False

    for i in range(0, 5): 
        if(estoques[i] < 5):
            print(f" - {nomes[i]} : {estoques[i]} unidades")
            temEstoqueBaixo = True

    if(not temEstoqueBaixo):
        print("Nenhum medicamento com estoque baixo")

registrar()

while True:
    print("""\n1 - Listar medicamentos
2 - Pesquisar medicamento
3 - Registrar venda
4 - Repor estoque
5 - Mostrar estoque baixo
6 - Encerrar
""")
    opcao = int(input("Escolha uma opção: "))

    if(opcao == 1):
        listarMedicamentos()
    elif(opcao == 2):
        pesquisarMedicamento()
    elif(opcao == 3):
        registrarVenda()
    elif(opcao == 4):
        reporEstoque()
    elif(opcao == 5):
        verificarEstoqueBaixo()
    elif(opcao == 6):
        break
    else:
        print("Opcao invalida.")