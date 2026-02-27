lista_compras = []



while True:
  escolha = input('Selecione: \
    [i]nserir, [a]pagar, [l]ista, [s]air: ').lower()
 
  if escolha == 'i':
        item = input('Digite o item: ')
        lista_compras.append(item)

  if escolha == 'a':
    try:
      apagar_item = int(input('Digite o indice: '))
      del lista_compras[apagar_item]

    except ValueError:
        print('Digite apenas inteiros!')

    except IndexError:
        print('Índicenao existe!')

    except Exception:
        print('Erro desconhecido')

  elif escolha == 'l':
      for indice, itens in enumerate(lista_compras):
        print(indice, itens)

  elif escolha == 's':
        break


if len(escolha) < 1:
    print('Digite apenas 1 caracter')



