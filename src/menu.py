import networkx as nx
import csv
import matplotlib.pyplot as plt
import gcol  
import time

def criaGrafoCsv(arquivo_csv):
    inicio = time.time()
    with open(arquivo_csv, 'r') as f:
        dados = csv.reader(f)
        next(dados)  # pula linha de cabeçalho
        g = nx.Graph()
        for linha in dados:
            g.add_edge(linha[0].strip(), linha[1].strip())
        print("Número de disciplinas:", len(g.nodes()))
        print("Número de conflitos:", len(g.edges()))
        
    fim = time.time()
    delta = round(fim - inicio,6)
    print(f"Tempo gasto para gerar o grafo: {delta}s")
    return g


def desenhaGrafo(grafo, titulo="Grafo de Conflitos", cores=None):
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(grafo, seed=42)
    
    if cores:
        lista_cores = [cores.get(n, 0) for n in grafo.nodes()]
        cmap = plt.cm.get_cmap('Set3', len(set(lista_cores)))
    else:
        lista_cores = "lightblue"
        cmap = None

    nx.draw(
        grafo,
        pos,
        with_labels=True,
        node_color=lista_cores,
        cmap=cmap,
        node_size=1000,
        font_size=10,
        font_weight="bold",
        edge_color="gray"
    )

    plt.title(titulo)
    plt.show()


def coloreGrafoGcol(grafo):
    inicio = time.time()
    cores = gcol.node_coloring(grafo)
    fim = time.time()
    delta = round(fim - inicio,6)
    print(f"Tempo gasto para colorir o grafo: {delta}s")

    print("\nCores atribuídas aos nós (via gCol):")
    for nodo, cor in cores.items():
        print(f"{nodo}: cor {cor}")

    print(f"\nTotal de cores usadas: {len(set(cores.values()))}")
    return cores


def menu():
    while True:
        opcao = input("Digite o caminho para o arquivo juntamente com sua extensão (0 para sair): ")
        if opcao == "0":
            print("-------Execução Encerrada---------")
            return
        try:
            g = criaGrafoCsv(opcao)
            break
        except Exception as e:
            print(f"Erro: {e}")
            print("Arquivo inválido, tente novamente.")

    cores = None

    while True:
        print("\n===== MENU =====")
        print("1 - Ler outro arquivo CSV")
        print("2 - Mostrar grafo")
        print("3 - Colorir grafo com gCol")
        print("0 - Sair")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida -- digite um número válido:")
            continue

        match opcao:
            case 1:
                arquivo_csv = input("Digite o nome do arquivo CSV: ")
                g = criaGrafoCsv(arquivo_csv)
            case 2:
                desenhaGrafo(g, "Grafo de Conflitos", cores)
            case 3:
                cores = coloreGrafoGcol(g) #a variavel cores tem um dicionario com um vertice e a cor que ele pode ser
                desenhaGrafo(g, "Grafo Colorido (gCol)", cores)
            case 0:
                print("-------Execução Encerrada---------")
                break
            case _:
                print("///// Opção inválida /////")
