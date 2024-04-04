# Operadores in e not in
# Strings são iteráveis, as strings em python são iteráveis
# iterável = algo que pode navegar item por item
#Exemplo, da pra identificar todos os índices abaixo (algarismos/letras)
# 0 1 2 3 4 5
# M a r c o s
# -6 -5 -4 -3 -2 -1

#nome ='Marcos' #o que foi lido é a letra r, ou seja 0 = M, 1 = a, 2 = r
#print(nome[2])
#print(nome[-4]) #aqui foi ao contrário, sendo -1 = s, -2 = o, -3 = c, -4 = s

#da para usar IN
#print('r' not in nome) #o not in inverte a impressão, aqui ele traz false, em ptbr ficaria R NÃO ESTÁ EM NOME, ele da falso pois está
#print('r' in nome) #aqui traz true

#Exemplo vida "real"
nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')

else:
    print(f'{encontrar} não está em {nome}')
          