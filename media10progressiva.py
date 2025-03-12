s = 0

for i in range(10):
    if i < 1:
        n1 = int(input("Digite um número: "))
        s += n1
    else:
        n1 = int(input("Digite outro número: "))
        s += n1
        s /= 2
        print(f'A média de agora é {s}')

print(f"A média é {s}")
