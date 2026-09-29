contador = 0
total = 0

minimo = float('inf')
maior = None

lista = []

while True:
    q1 = input("Gostaria de iniciar seus registros? (s/n): ")
    if q1 == 'n':
        print("Cadastro encerrado")
        break
    
    while True:
        categoria = input("Categoria: ")
        if not categoria:
            print("texto não pode ficar vazio")
        else:
            break

    while True:
        try:
            valor = float(input("Qual foi o valor: "))
            if valor > 0:
                break
            else:
                    print("valor incorreto")
        except ValueError:
                print("Valor incorreto")

    while True:
        descricao = input("Descrição: ") 
            
        if not descricao:
            print("Descrição não pode estar vazia")
        else:
            break 


        
    gasto = categoria, valor, descricao

    lista.append(gasto)

    contador += 1

    resposta = input("Gostaria de adicionar um novo registro? (s/n)").lower()

    if resposta == 'n':
        print("Registros inseridos")
        break

#==================================================================
if lista:
    for categoria, valor, descricao in lista:
        total += valor
        print(categoria, valor, descricao)

    print(f"Gastos totais: {total}")

    orcamento = float(input("Qual seu orçamento mensal?: "))
    saldo = orcamento - total


    for categoria, valor, descricao in lista:
        if valor < minimo:
            minimo = valor

        if maior is None or valor > maior:
            maior = valor


    media = total/len(lista)


    totais = {}
    for categoria, valor, descricao in lista:
        totais[categoria] = totais.get(categoria, 0.0) + valor


    if total < orcamento:
        print(f"Saldo restante: {saldo}")
    elif total == orcamento:
        print (f"Quanto foi gasto: {orcamento}")
    else:
        print(f"Saldo excedido: {saldo * -1}")

    print(f"Valor minimo é: {minimo}")
    print(f"Valor maior é: {maior}")
    print(f"Media de gastos {media:.2f}")
    print(f"Total por gastos: {totais}")

else:
    print("Não a registros")