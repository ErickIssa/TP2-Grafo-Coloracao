import networkx as nx
import csv

import matplotlib.pyplot as plt
import networkx as nx

def criaGrafoCsv(arquivo_csv):
    with open(arquivo_csv, 'r') as f:
        dados = csv.reader(f) # ja separa por ,
        next(dados) #pula linha disciplinas
        g = nx.Graph()
        for linha in dados:
             g.add_edge(linha[0].strip(), linha[1].strip()) # isso faz com que cada linha seja add no grafo se tiver apenas 2 elementos, mo locura kkk

        print("Número de disciplinas:", len(g.nodes())) #debugs apagar dps
        print("Número de conflitos:", len(g.edges()))
    
    return g


def desenhaGrafo(grafo, titulo="Grafo de Conflitos", cores=None):
    """
    Desenha o grafo na tela usando matplotlib.
    
    Parâmetros:
    - grafo: objeto networkx.Graph
    - titulo: título do gráfico (string)
    - cores: dicionário opcional {nó: cor}, para coloração de grafos
    
    Exemplo:
        desenhaGrafo(G)
        desenhaGrafo(G, cores={'A':1,'B':2,'C':1})
    """

    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(grafo, seed=42)  # layout automático (arranjo dos vértices)

    # Define cor padrão dos nós
    if cores:
        # Garante que cada nó receba uma cor numérica (convertida para um mapa de cores)
        lista_cores = [cores.get(n, 0) for n in grafo.nodes()]
        cmap = plt.cm.get_cmap('Set3', len(set(lista_cores)))  # paleta de cores
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


def menu():
        
   

    while True:
        opcao = (input("Digite o caminho para o arquivo juntamente com sua extensão(0 para sair):"))
        arquivo_csv = opcao #APAGAR ISSO DPS E COLOCAR UMA VERIFICAÇÃO PARA CASO DE ERRADO USAR UM ARQV GENERICO
        try:  
            g = criaGrafoCsv(arquivo_csv)
            break
        except :
            if opcao == "0":
                print("-------Execucao Encerrada---------")
                return
            print("arquivo inválido, tente novamente (lembre-se de adicionar o data e o .csv")
        
            


    
    while True:
        print("\n===== MENU =====")
        print(" 1 - Ler outro arquivo csv")
        print("2 - Printa Grafo")
        print("0 - Sair")
        
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opcao Invalida -- Digite um Numero Valido:")
            continue

        match opcao:
            case 1:
                arquivo_csv = (input("Digite o nome do arquivo de texto que está na pasta DATA com sua extensão:"))
                g = criaGrafoCsv(arquivo_csv)
            case 2:
                desenhaGrafo(g,"G conflicts")
            case 0:
                print("-------Execucao Encerrada---------")
                break
            
            case _:
                print("/////Opcao Invalida/////")
