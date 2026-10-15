import streamlit as st
import folium
from streamlit_folium import st_folium

from cidades import CIDADES, ARESTAS
from dijkstra import menor_caminho


st.set_page_config(
    page_title="Trabalho Grafos - Dijkstra",
    layout="wide"
)

st.title("Trabalho de Grafos - Dijkstra")

# Monta o grafo com conexões nos dois sentidos
grafo = {sigla: {} for sigla in CIDADES}

for origem, destino, custo in ARESTAS:
    grafo[origem][destino] = custo
    grafo[destino][origem] = custo


# Retorna o nome completo da cidade
def nome(sigla):
    return CIDADES[sigla][0]


siglas = list(CIDADES)

# Select das cidades de origem e destino
col1, col2 = st.columns(2)

with col1:
    origem = st.selectbox(
        "Cidade de origem",
        siglas,
        format_func=nome
    )

with col2:
    destinos = [s for s in siglas if s != origem]

    destino = st.selectbox(
        "Cidade de destino",
        destinos,
        format_func=nome
    )


# Esse parte vai executar a lógica do algoritmo de Dijkstra definida na função de menor_caminho ao clicar no botão
if st.button("Calcular menor caminho", type="primary"):
    caminho, custo = menor_caminho(grafo, origem, destino)

    st.session_state["rota"] = (
        origem, destino, caminho, custo
    )


rota = st.session_state.get("rota")

# Limpa visualmente a rota quando a seleção muda
if rota and (rota[0] != origem or rota[1] != destino):
    rota = None


# Cria o mapa de Santa Catarina
mapa = folium.Map(
    location=[-27.15, -49.78],
    zoom_start=9,
    tiles="OpenStreetMap"
)


# Aqui vai realizar os traços de todas as conexões das cidades em cinza
for a, b, custo in ARESTAS:
    pontos = [
        (CIDADES[s][1], CIDADES[s][2])
        for s in (a, b)
    ]

    folium.PolyLine(
        pontos,
        color="gray",
        weight=2,
        opacity=0.6,
        tooltip=f"{nome(a)} ↔ {nome(b)}: {custo} km"
    ).add_to(mapa)


# Destaca o menor caminho em azul
if rota and rota[2]:
    caminho = rota[2]

    pontos = [
        (CIDADES[s][1], CIDADES[s][2])
        for s in caminho
    ]

    folium.PolyLine(
        pontos,
        color="#1677ff",
        weight=7,
        opacity=0.95
    ).add_to(mapa)

    mapa.fit_bounds(pontos, padding=(35, 35))


# Adiciona os marcadores das cidades
for sigla, (cidade, latitude, longitude) in CIDADES.items():
    cor = "blue" # Cor padrão das cidades

    if rota and rota[2]:
        if sigla == origem:
            cor = "green" # Cor da cidade de origem
        elif sigla == destino:
            cor = "red" # Cor da cidade de destino

    folium.Marker(
        [latitude, longitude],
        tooltip=cidade,
        popup=f"{cidade} ({sigla})",
        icon=folium.Icon(color=cor)
    ).add_to(mapa)


# Exibe o mapa na interface
st_folium(
    mapa,
    height=520,
    use_container_width=True,
    returned_objects=[]
)


# Mostra o resultado do algoritmo, exibindo o trajeto com o menor custo encontrado
if rota:
    if rota[2]:
        st.success(f"Menor custo: {rota[3]} km")
    else:
        st.warning("Não existe caminho entre essas cidades.")