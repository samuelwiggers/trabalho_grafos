
import heapq

def menor_caminho(grafo, origem, destino):
    # Inicializa todas as distâncias como infinito
    distancias = {cidade: float("inf") for cidade in grafo}
    anteriores = {}

    distancias[origem] = 0
    fila = [(0, origem)]

    while fila:
        custo_atual, cidade = heapq.heappop(fila)

        if custo_atual > distancias[cidade]:
            continue

        if cidade == destino:
            break

        # Vai percorrer as cidades vizinhas
        for vizinha, custo in grafo[cidade].items():
            novo_custo = custo_atual + custo

            if novo_custo < distancias[vizinha]:
                distancias[vizinha] = novo_custo
                anteriores[vizinha] = cidade

                heapq.heappush(fila, (novo_custo, vizinha))

    # Aqui verifica se tem um caminho existente, caso não tenha retorna nulo
    if distancias[destino] == float("inf"):
        return [], None

    # Reconstrói o caminho encontrado
    caminho = [destino]

    while caminho[0] != origem:
        caminho.insert(0, anteriores[caminho[0]])

    return caminho, distancias[destino]
