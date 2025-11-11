# Global Solution 2025 - Python (Allen)

# Integrantes:
# 1. Diogo Pelinson - RM: 563321
# 2. Lorenzo Andolfatto Coque - RM: 563385
# 3. Pedro Henrique Caires - RM: 562344
# ----------------------------------------------------------

import requests
import time
import json
import os
import sys
from datetime import datetime

# ----------------------------------------------------------
# Funções de Login e Cadastro

USERS_FILE = "usuarios.json"

def carregar_usuarios():
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w") as f:
            json.dump([], f)
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def salvar_usuarios(usuarios):
    with open(USERS_FILE, "w") as f:
        json.dump(usuarios, f, indent=4)

def validar_nome(nome):
    return len(nome.split()) >= 2

def validar_data_nascimento(data_str):
    try:
        dia, mes, ano = map(int, data_str.split("/"))

        if dia < 1 or dia > 31:
            print(" Dia inválido (deve estar entre 1 e 31).")
            return False

        if mes < 1 or mes > 12:
            print(" Mês inválido (deve estar entre 1 e 12).")
            return False

        if ano < 1930:
            print(" Ano inválido (não pode ser menor que 1930).")
            return False

        data_nasc = datetime(ano, mes, dia)
        hoje = datetime.now()
        idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))

        if idade < 18:
            print(" Você deve ter pelo menos 18 anos para se cadastrar.")
            return False

        return True

    except ValueError:
        print(" Data inválida. Use o formato DD/MM/AAAA.")
        return False

def formatar_data(data_str):

    try:
        dia, mes, ano = map(int, data_str.split("/"))
        return f"{dia:02d}/{mes:02d}/{ano}"
    except:
        return data_str  # se falhar, retorna como veio

def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11

def cadastrar_usuario():
    print("\n=== CADASTRO DE NOVO USUÁRIO ===")
    usuarios = carregar_usuarios()

    while True:
        nome = input("Nome completo: ").strip()
        if not validar_nome(nome):
            print(" O nome deve conter pelo menos dois nomes.")
            continue

        data_nascimento = input("Data de nascimento (DD/MM/AAAA): ").strip()
        data_nascimento = formatar_data(data_nascimento)  # <-- Formata automaticamente
        if not validar_data_nascimento(data_nascimento):
            continue

        cpf = input("CPF (apenas números): ").strip()
        if not validar_cpf(cpf):
            print(" CPF inválido. Deve conter exatamente 11 números.")
            continue

        usuario_existente = next((u for u in usuarios if u["cpf"] == cpf), None)
        if usuario_existente:
            print(" Já existe um usuário com esse CPF.")
            continue

        senha = input("Crie uma senha: ").strip()
        usuarios.append({
            "nome": nome,
            "data_nascimento": data_nascimento,
            "cpf": cpf,
            "senha": senha
        })
        salvar_usuarios(usuarios)
        print(f"\n Usuário {nome} cadastrado com sucesso!\n")
        return {"nome": nome, "cpf": cpf}

def login():
    print("\n=== LOGIN ===")
    usuarios = carregar_usuarios()

    while True:
        cpf = input("CPF: ").strip()
        senha = input("Senha: ").strip()

        usuario = next((u for u in usuarios if u["cpf"] == cpf and u["senha"] == senha), None)
        if usuario:
            print(f"\n Bem-vindo, {usuario['nome']}!\n")
            return usuario
        else:
            print(" Usuário ou senha incorretos.\n")
            return None

# ----------------------------------------------------------
# Menu Principal

def menu_inicial():
    while True:
        print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("       💼 𝑺𝒌𝒊𝒍𝒍𝒖𝒑𝑨𝑰 💼")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
        print("1. Entrar")
        print("2. Criar conta")
        print("3. Sair\n")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            usuario = login()
            if usuario:
                return usuario
        elif opcao == "2":
            usuario = cadastrar_usuario()
            return usuario
        elif opcao == "3":
            print("\n Encerrando o programa. Até logo!\n")
            sys.exit()
        else:
            print(" Opção inválida. Tente novamente.\n")

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
# Funções auxiliares

def filtrar_profissoes(lista_profissoes, termo):
    return [p for p in lista_profissoes if termo.lower() in p["titulo"].lower()]

def calcular_crescimento_total(lista, indice=0):
    if indice == len(lista):
        return 0
    return lista[indice]["crescimento"] + calcular_crescimento_total(lista, indice + 1)

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
    for i, titulo in enumerate(opcoes_disponiveis[:15], start=1):
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
    usuario = menu_inicial()  # menu com login/cadastro/saída
    print(f"Acesso liberado para {usuario['nome']} (CPF: {usuario['cpf']})\n")

    print(" Obtendo tendências de emprego...\n")
    profissoes = obter_tendencias_emprego()

    if not profissoes:
        print(" Não foi possível obter dados da API. Verifique sua chave ou conexão.")
        return

    filtradas = escolher_profissao(profissoes)
    exibir_profissoes(filtradas)
    total_crescimento = calcular_crescimento_total(filtradas)
    print(f"\n Crescimento total estimado das profissões filtradas: {total_crescimento}%\n")

# ----------------------------------------------------------
if __name__ == "__main__":
    main()
# ----------------------------------------------------------
