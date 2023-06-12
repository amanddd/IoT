def contador_vogais(string):
    vogais = ['a', 'e', 'i', 'o', 'u']
    contador = 0
    
    for caractere in string:
        if caractere in vogais:
            contador = contador +1
    
    return contador

frase = input("Digite a frase: ")
result = contador_vogais(frase)

print("A quantidade de vogais é: ", result)