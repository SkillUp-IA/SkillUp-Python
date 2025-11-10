# Global Solution 2025 - Python (Allen)

# Integrantes:
# 1. Diogo Pelinson- RM:
# 2. Lorenzo Andolfatto Coque - RM: 563385
# 3. Pedro Henrique Caires- RM:
# ----------------------------------------------------------

import requests
import time

# ----------------------------------------------------------
# Obtendo Tendências de Emprego (API)

def obter_tendencias_emprego():
    url = "https://jsearch.p.rapidapi.com/search"
    querystring = {
        "query": "developer jobs in chicago",
        "page": "1",
        "num_pages": "1",
        "country": "us",
        "date_posted": "all"
    }
    headers = {
        "x-rapidapi-key": "44641a4f6cmsh0678bf11e166adap119a54jsn505deef1456f",
        "x-rapidapi-host": "jsearch.p.rapidapi.com"
    }
    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        data = response.json()
        empregos = []

        for item in data.get("data", []):
            profissao = {
                "titulo": item.get("job_title", "Não informado"),
                "empresa": item.get("employer_name", "Desconhecida"),
                "localizacao": item.get("job_city", "Desconhecida"),
                "descricao": item.get("job_description", "Sem descrição disponível."),
                "crescimento": len(item.get("job_description", "")) % 10
            }
            empregos.append(profissao)

        return empregos

    except requests.exceptions.RequestException as e:
        print(f" Erro ao acessar a API: {e}")
        return []


# ----------------------------------------------------------

# Filtrando Profissões

def filtrar_profissoes(lista_profissoes, termo):
    return [p for p in lista_profissoes if termo.lower() in p["titulo"].lower()]

# ----------------------------------------------------------

# Cálculo Recursivo de Crescimento

def calcular_crescimento_total(lista, indice=0):
    if indice == len(lista):
        return 0
    return lista[indice]["crescimento"] + calcular_crescimento_total(lista, indice + 1)

# ----------------------------------------------------------

# Exibindo Profissões

def exibir_profissoes(lista):
    if not lista:
        print("Nenhuma profissão encontrada.\n")
        return

    print("\n=== Profissões Encontradas ===")
    for p in lista:
        print(f"\n Título: {p['titulo']}")
        print(f" Empresa: {p['empresa']}")
        print(f" Localização: {p['localizacao']}")
        print(f" Crescimento estimado: {p['crescimento']}%")
        print(f" Descrição: {p['descricao'][:200]}...\n")


def escolher_profissao(profissoes):
    opcoes_disponiveis = sorted(set([p["titulo"] for p in profissoes]))

    print("\n PROFISSÕES DISPONÍVEIS:\n")
    for i, titulo in enumerate(opcoes_disponiveis[:15], start=1):  # mostra as 15 primeiras
        print(f"{i}. {titulo}")
    print("\n( Dica: Você pode digitar parte do nome, como 'Python' ou 'Engineer')")

    while True:
        termo = input("\nDigite o nome (ou parte) da profissão desejada: ").strip()
        filtradas = filtrar_profissoes(profissoes, termo)

        if filtradas:
            return filtradas
        else:
            print("\n Profissão não encontrada. Tente novamente.\n")
            time.sleep(1)


# ----------------------------------------------------------

# Programa Principal

def main():
    print(" Obtendo tendências de emprego...\n")
    profissoes = obter_tendencias_emprego()

    if not profissoes:
        print(" Não foi possível obter dados da API. Verifique sua chave ou conexão.")
        return
    filtradas = escolher_profissao(profissoes)
    exibir_profissoes(filtradas)
    total_crescimento = calcular_crescimento_total(filtradas)
    print(f"\n Crescimento total estimado das profissões filtradas: {total_crescimento}%\n")

if _name_ == "_main_":
    main()
# ----------------------------------------------------------
