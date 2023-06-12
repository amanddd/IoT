#declarando variaveis
variavel = "hello world, mario!"
variavelDois = "super mario world"

#comentario de uma so linha
'''comentario de blocos'''

#printando variaveis
print(variavel)

#estrutura condicional if 
#em python se usa identação para definir os blocos
if variavel !=  variavelDois:
    print("diferente")


#é possivel tipar com python
#numeros inteiros
num1: int = 2
num2: int = 4
#strings
nome: str = "maria clara"
#listas
lista = [1, 2, 7]
#tuplas
#tuplas sao imutaveis
tupla = ("maria", 7)

#metodos com strings
print(nome.upper)
nome.lower

#entrada de dados
entrada = int(input("digite aqui "))

#if, else, elif
if entrada > 7:
    print("maior que 7")
    
elif entrada == 7:
    print("igual a 7")
else:
    print("menor que 7")
    
#ciclo while    
while entrada != 0:
    print(entrada)
    entrada = entrada -1
    
#laço for
lista_nomes = ['taylor','marina', 'duda']

for nomes in lista_nomes:
    print(nomes)
    
#funçoes e modulos

def multiplicacao (a,b):
    return a * b

result = multiplicacao(3, 8)
print(result)