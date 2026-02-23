escolha = input('Selecione: \
[i]nserir, [a]pagar, [l]ista, [s]air').lower()

lista_compras = []



while True:
 
    if escolha == 'i':
        item = input('Digite o item: ')
         lista.append(item)
    
    if escolha == 'a':
        apagar_item = input('Digite o indice: ')
         del lista_compras[apagar_item]

    if escolha == 'l':
      for indice, itens in lista_compras:
        print(indice, itens)
        break

    elif escolha == 's':
        break

    else:
        print('Digite apenas s l, a ou i')

if len(escolha) < 1:
    print('Digite apenas 1 caracter')