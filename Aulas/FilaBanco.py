import random

ultimo = 0  # controla o último da fila
fila_regular = []  # fila regular
fila_preferencial = []  # fila preferencial
atendimentos_preferenciais = 0  # contador de atendimentos preferenciais

while True:
    print("\nExistem %d clientes na fila regular" % len(fila_regular))
    print('Fila regular: ', fila_regular)
    print("\nExistem %d clientes na fila preferencial" % len(fila_preferencial))
    print('Fila preferencial: ', fila_preferencial)
    print('Digite\n<R> para adicionar à fila regular\n<P> para adicionar à fila preferencial\n<A> para atender\n<S> para sair')

    op = input('Operação (R, P, A, S): ').strip().upper()

    if op == 'A':  # atendimento
        if atendimentos_preferenciais < 3 and len(fila_preferencial) > 0:
            atendido = fila_preferencial.pop(0)  # remove o primeiro da fila preferencial
            print("Cliente preferencial %d atendido" % atendido)
            atendimentos_preferenciais += 1
        elif len(fila_regular) > 0:  # Atende cliente da fila regular se não houver preferenciais ou após atender 3 preferenciais
            atendido = fila_regular.pop(0)  # remove o primeiro da fila regular
            print("Cliente regular %d atendido" % atendido)
            atendimentos_preferenciais = 0  # Reseta o contador de atendimentos preferenciais
        elif len(fila_preferencial) > 0:  # Se não houver clientes regulares, atende um cliente preferencial para não bloquear a fila
            atendido = fila_preferencial.pop(0)  # remove o primeiro da fila preferencial
            print("Cliente preferencial %d atendido" % atendido)
            atendimentos_preferenciais += 1
        else:
            print('Ambas as filas estão vazias, nenhum cliente para atender')

    elif op == 'R':
        ultimo += 1
        fila_regular.append(ultimo)

    elif op == 'P':
        ultimo += 1
        fila_preferencial.append(ultimo)

    elif op == 'S':
        print("Saindo...")
        break
    else:
        print('Operação inválida. Digite (R, P, A ou S).')
