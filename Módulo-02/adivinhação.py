print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 48
chute = int(input("Digite um  número:"))
if( numero_secreto == chute):
    print("Você acertou!")
else:
    print("Você errou!")
print("Fim do jogo")

#********************-testes-**************************#
minha_idade = 26
idade_namorado = 25
if(minha_idade == idade_namorado):
    print('temos idades iguais')
else:
    print('temos idades diferentes')
#06 Comparação estranha
numero1 = 10
numero2 = 10
if(numero1 == numero2):
    print("São números iguais")

idade1 = 10
idade2 = int("20")
print(idade1 + idade2)

nome = "Nico"
sobrenome = "Steppat"
print(nome + sobrenome)

nome = "Nico"
sobrenome = "Steppat"
print(nome, sobrenome)
nome = "Nico"
sobrenome = "Steppat"
print(nome, sobrenome, sep="_")

#Diferenças entre o Python 2 e o Python3
print "python2"
print("python2")
#12 Para saber mais: JavaScript vs Python

numero1 = 10
numero2 = "20"
produto = numero1 * numero2
print(produto)