n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite outro número: "))

lista = [n1, n2, n3]
lista.sort()

print(f"{lista[0]} < {lista[1]} < {lista[2]}")