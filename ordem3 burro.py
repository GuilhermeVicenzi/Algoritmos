n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite outro número: "))

if n1 < n2 and n1 < n3:
    print(f"{n1} é o menor número")
    if n2 < n3:
        print(f"{n2} é o número intermediário")
        print(f"{n3} é o maior dos números")
        print(f"{n1} < {n2} < {n3}")
    else:
        print(f"{n3} é o número intermediário")
        print(f"{n2} é o maior dos números")
        print(f"{n1} < {n3} < {n2}")

elif n2 < n1 and n2 < n3:
    print(f"{n2} é o menor número")
    if n1 < n3:
        print(f"{n1} é o número intermediário")
        print(f"{n3} é o maior dos números")
        print(f"{n2} < {n1} < {n3}")
    else:
        print(f"{n3} é o número intermediário")
        print(f"{n1} é o maior dos números")
        print(f"{n2} < {n3} < {n1}")
else:
    print(f"{n3} é o menor número")
    if n1 < n2:
        print(f"{n1} é o número intermediário")
        print(f"{n2} é o maior dos números")
        print(f"{n3} < {n1} < {n2}")
    else:
        print(f"{n2} é o número intermediário")
        print(f"{n1} é o maior dos números")
        print(f"{n3} < {n2} < {n1}")