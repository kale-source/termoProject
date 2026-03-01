# 🎯 Termo Project

Implementação do jogo **Termo (Wordle brasileiro)** desenvolvida como desafio pessoal de lógica.

Este projeto foi construído **sem uso de Inteligência Artificial**, com foco total em desenvolvimento de raciocínio lógico, manipulação de strings e estruturação de regras corretamente — principalmente o tratamento de letras repetidas.

---

## 🧠 Sobre o Desafio

O objetivo deste projeto foi:

- Reproduzir a lógica do jogo Termo
- Implementar corretamente o sistema de cores:
  - 🟩 Verde → letra correta na posição correta
  - 🟨 Amarelo → letra existe na palavra, mas em outra posição
  - ⬜ Cinza → letra não existe na palavra
- Resolver corretamente o problema de **letras repetidas**
- Desenvolver a solução do zero, apenas com lógica e testes

Foi um desafio que exigiu bastante raciocínio e refinamento da lógica até chegar na versão final correta.

---

## 🎮 Como Funciona

O jogador:

1. Digita uma palavra de 5 letras
2. O sistema compara com a palavra secreta
3. Retorna as cores correspondentes
4. O jogador tem número limitado de tentativas

---

## ⚙️ Lógica Principal

A parte mais importante do projeto foi:

- Controlar a contagem de letras
- Evitar marcar letras repetidas incorretamente
- Separar a verificação em etapas:
  1. Verificar letras corretas (verde)
  2. Depois verificar letras existentes em outras posições (amarelo)
  3. Marcar o restante como cinza

A solução final utiliza estruturas como:

- Dicionários para controle de contagem
- Comparação por índice
- Validação de entrada
- Controle de tentativas

---

## 📁 Estrutura do Projeto

```
termoProject/
│
├── main.py
├── termo.py
└── README.md
```

*(A estrutura pode variar conforme seu repositório.)*

---

## 🚀 Como Executar

Clone o repositório:

```bash
git clone https://github.com/kale-source/termoProject.git
cd termoProject
```

Execute:

```bash
python main.py
```

Requisitos:

- Python 3.x

---

## 🎯 O Que Este Projeto Demonstra

- Raciocínio lógico sólido
- Manipulação de strings
- Controle de fluxo
- Tratamento correto de edge cases
- Persistência na resolução de problemas
- Capacidade de resolver problemas complexos sem apoio de IA

---

## 🔍 Principal Aprendizado

O maior desafio foi implementar corretamente a lógica de letras repetidas.

Exemplo:

Palavra secreta: `BANAL`  
Tentativa: `BALAO`

A lógica precisa garantir que:

- Apenas a quantidade correta de letras seja marcada como válida
- Não marcar letras extras como amarelas indevidamente

Esse tipo de detalhe exige controle preciso da contagem de caracteres.

---

## 💡 Possíveis Melhorias Futuras

- Interface gráfica (Tkinter / Pygame)
- Versão Web
- Sistema de pontuação
- Dicionário externo de palavras válidas
- Modo multiplayer
- Histórico de partidas

---

## 👨‍💻 Autor

Desenvolvido por **Kaiky Leandro**

Projeto criado como desafio pessoal para fortalecimento da lógica de programação.
Sem uso de Inteligência Artificial durante o desenvolvimento da solução.
