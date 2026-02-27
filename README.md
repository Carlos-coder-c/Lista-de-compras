🛒 Lista de Compras — CLI em Python
Aplicação simples de terminal para inserir, apagar, listar e sair de uma lista dinâmica.
📌 Código
Python
Copiar código
lista_compras = []

while True:
    escolha = input(
        "Selecione: [i]nserir, [a]pagar, [l]ista, [s]air: "
    ).lower()

    if escolha == 'i':
        item = input('Digite o item: ')
        lista_compras.append(item)

    elif escolha == 'a':
        try:
            apagar_item = int(input('Digite o indice: '))
            del lista_compras[apagar_item]
        except ValueError:
            print('Digite apenas inteiros!')
        except IndexError:
            print('Índice não existe!')
        except Exception:
            print('Erro desconhecido')

    elif escolha == 'l':
        for indice, item in enumerate(lista_compras):
            print(indice, item)

    elif escolha == 's':
        break
⚙️ Como Funciona
lista_compras = [] → estrutura mutável que armazena os itens.
while True → mantém o sistema rodando até o usuário sair.
append() → adiciona item.
del lista[indice] → remove item pelo índice.
enumerate() → gera (índice, valor) durante o loop.
try/except → evita que o programa quebre com entrada inválida.
🔁 Fluxo
Copiar código

Início
  ↓
Usuário escolhe opção
  ↓
Inserir | Apagar | Listar | Sair
  ↓
Loop continua até 's'
🎯 Conceitos Aplicados
Lista mutável
Controle de fluxo (if / elif)
Loop infinito controlado
Tratamento de exceções
Iteração com enumerate()
Projeto simples, mas cobre fundamentos essenciais de lógica e estrutura em Python.