# 💼 SkillUp IA – Tendências de Emprego  
### Global Solution 2025 – Python (Allen)

Projeto desenvolvido para a FIAP como parte da **Global Solution 2025**, integrado ao tema **Futuro do Trabalho**.  
A ideia da **SkillUp IA** é ajudar pessoas a tomarem decisões de carreira com base em **tendências reais do mercado de trabalho**, utilizando dados de vagas de emprego em tempo real.

---

## 👥 Integrantes

- **Diogo Pelinson** – RM: 563321  
- **Lorenzo Andolfatto Coque** – RM: 563385  
- **Pedro Henrique Caires** – RM: 562344  

---

## 🎯 Objetivo do Projeto

O sistema permite que o usuário:

- Faça **cadastro e login** com validação de dados (nome, data de nascimento, CPF e senha);
- Pesquise uma **profissão desejada** (ex: _Python Developer_, _Engineer_, etc.);
- Escolha um **país** para análise (ex: `us`, `br`, `jp`, `fr`);
- Consulte uma API de vagas de emprego (**JSearch – RapidAPI**) e veja:
  - Título da vaga  
  - Empresa  
  - Localização  
  - Descrição resumida  
  - Um valor de **“crescimento estimado”** calculado a partir da descrição  
- Visualize:
  - Uma **lista resumida** das vagas encontradas;
  - Uma **versão detalhada** com mais informações;
  - O **crescimento total estimado** (calculado com uma função recursiva).

Tudo isso simulando uma primeira versão de uma plataforma SkillUp IA focada em apoiar decisões de carreira com base em dados.

---

## 🧩 Funcionalidades Principais

### 👤 Cadastro e Login

- Armazena os usuários em um arquivo `usuarios.json`;
- Valida:
  - Nome completo (precisa ter pelo menos 2 nomes);
  - Data de nascimento (formato `DD/MM/AAAA` e idade mínima de **18 anos**);
  - CPF (apenas números, exatamente **11 dígitos**);
- Impede cadastro de CPFs duplicados;
- Login realizado por **CPF + senha**.

### 🌎 Consulta a Tendências de Emprego

- Integração com a API **JSearch** (via RapidAPI);
- Busca por vagas usando:
  - Profissão informada pelo usuário;
  - País escolhido (`us`, `br`, `jp`, `fr`, etc.);
- Exibição de:
  - Lista resumida das vagas (título, empresa, cidade);
  - Detalhes completos (com descrição truncada);
  - Cálculo do **crescimento estimado** por vaga;
  - Soma do crescimento total com **função recursiva**.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.x  
- **Bibliotecas principais:**
  - `requests` – requisições HTTP para a API de empregos  
  - `json` – manipulação de arquivos e dados em JSON  
  - `datetime` – validação de datas e cálculo de idade  
  - `os`, `sys`, `time` – suporte ao funcionamento do CLI

---

## 📦 Instalação e Configuração

- Clone o repositório ou copie os arquivos do projeto

```
git clone <url-do-repositorio>
cd <pasta-do-projeto>
```


- (Opcional) Crie e ative um ambiente virtual

```
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate
```

- Instale as dependências a partir do requirements.txt ✅
  
```
pip install -r requirements.txt
```
