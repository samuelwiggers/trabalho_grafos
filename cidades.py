
# Definindo os nomes e coordenadas das cidades para o mapa
CIDADES = {
    "RS": ("Rio do Sul", -27.2149, -49.6431),
    "IB": ("Ibirama", -27.0567, -49.5178),
    "IT": ("Ituporanga", -27.4148, -49.6020),
    "TA": ("Taió", -27.1167, -49.9997),
    "PR": ("Pouso Redondo", -27.2583, -49.9333),
    "PG": ("Presidente Getúlio", -27.0500, -49.6230),
    "TC": ("Trombudo Central", -27.3033, -49.7944),
    "AG": ("Agronômica", -27.2667, -49.7111),
    "LA": ("Laurentino", -27.2167, -49.7333),
    "DE": ("Dona Emma", -26.9833, -49.7333),
    "WI": ("Witmarsum", -26.9278, -49.7961),
    "JB": ("José Boiteux", -26.9550, -49.6280),
    "SA": ("Salete", -26.9800, -49.9980),
    "RC": ("Rio do Campo", -26.9450, -50.1430),
    "AT": ("Atalanta", -27.4220, -49.7790)
}

# Conexões das cidades, contém a origem, destino e custo em km
ARESTAS = [
    ("RS", "IB", 23),
    ("RS", "PG", 24),
    ("RS", "TC", 26),
    ("RS", "IT", 34),
    ("RS", "LA", 20),
    ("RS", "AG", 30),
    ("RS", "PR", 22),
    ("RS", "AT", 45),
    ("IB", "PG", 8),
    ("IB", "DE", 15),
    ("IB", "WI", 12),
    ("IB", "JB", 18),
    ("IB", "TA", 25),
    ("IT", "TA", 40),
    ("IT", "SA", 55),
    ("IT", "RC", 60),
    ("IT", "AG", 28),
    ("IT", "PR", 38),
    ("TA", "PG", 30),
    ("TA", "DE", 20),
    ("TA", "RC", 35),
    ("PR", "TC", 10),
    ("PR", "LA", 15),
    ("PR", "SA", 25),
    ("PG", "TC", 18),
    ("PG", "AG", 22),
    ("TC", "DE", 20),
    ("AG", "LA", 12),
    ("LA", "WI", 25),
    ("DE", "JB", 10),
    ("AT", "AG", 18)
]