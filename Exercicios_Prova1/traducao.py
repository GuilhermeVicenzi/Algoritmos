#cria o vetor de palavras em portugues (port)
port = ["como", "oi", "bonito", "azul"]
#cria o vetor de palavras em ingles (ing)
ing = ["how ", "hi ", "beatiful ", "blue "]
#cria a frase que sera traduzida (frase)
frase = "oi como bonito"
#inicializa a frase traduzida (traducao)
traducao = ""
#cria um laco de repeticao para percorrer a frase cortada
for i in frase.split():
    #se o valor estiver em (port)
    if i in port:
        #pega o index da palavra
        index = int(port.index(i))
        #adiciona o equivalente em ingles usando o index
        traducao = traducao + ing[index]
    #senão
    else:
        #adiciona a palavra em portugues
        traducao = traducao + i
#mostra a traducao
print(traducao)