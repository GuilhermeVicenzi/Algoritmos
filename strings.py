frase = "Isso é uma frase"

letras = []

#itera sobre cada caracter e adiciona na lista
for i in frase:
    letras.append(i)

print(f"Essas são as letras da frase: {letras}")

#separa a string onde foi determinado pelo parâmetro
partes = frase.split(" ")

print(f"Essas são as partes da frase {partes}")

#troca um caracter pelo outro, sendo especificado nos parâmetros
frase = frase.replace("é", "e")
print(f"Essa é a frase sem acentos: {frase}")
