contador = 0
total = 0

lista = []

while contador < 3:
    categoria = input("Categoria: ")
    valor = float(input("Qual foi o valor: "))
    descricao = input("Descrição: ")  

    gasto = categoria, valor, descricao

    lista.append(gasto)

    contador += 1

for categoria, valor, descricao in lista:
    total += valor
    print(categoria, valor, descricao)

print(f"Gastos totais: {total}")

minimo = float('inf')
maior = None

for categoria, valor, descricao in lista:
    if valor < minimo:
        minimo = valor

    if maior is None or valor > maior:
        maior = valor

print(f"Valor minimo é: {minimo}")
print(f"Valor maior é: {maior}")
