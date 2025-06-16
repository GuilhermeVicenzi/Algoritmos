#Define a funcao
def invertida(frase):
    #Paramentro string que sera revertida
    print(frase)
    #Se a string tiver 1 caracter
    if len(frase) == 1:
        #Retorna ela mesma
        return frase
    #Retorna o ultimo caracter + funcao(string sem ultimo caracter)
    return frase[-1] + invertida(frase[:-1])

frase_invertida = invertida("Daqui a pouco vamos ir fazer prova")
print(frase_invertida)