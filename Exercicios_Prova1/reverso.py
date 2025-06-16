#pede a string e armazena (frase)
frase = str(input("Digite uma frase para inverte-lá: "))
#cria uma string vazia (reversa)
reversa = ""
frase_mutavel = frase
#cria um laco de repeticao
for i in frase:
    #pega o ultimo caracter da string
    caracter = frase[-1]
    #tira o ultimo caracter da string
    frase = frase[:-1]
    #adiciona na string reversa
    reversa = reversa + caracter
    
print(reversa)