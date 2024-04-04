#quando tiver ... exibir raciocionio
nome = 'Marcos Rodrigues'
altura = 1.72
peso = 118
imc = peso / (altura * altura) #poderia fazer peso / altura ** 2
#colocar f no começo da string, habilita possibilidade de usar variaveis dentro do texto, dentro de chaves
linha_1 = f'{nome} tem {altura:.2f} de altura' #esse final .2f é para especificar duas casas decimais, qualquer .numerof, nessa situação, gera casas decimais
#se colocar virgula, da pra separar dinheiro formato americano 100,000=100k
linha_2 = f'pesa {peso} quilos e seu imc é,'
linha_3 = f'{imc:.2f}'

#f-string, esse f significa formatação

print(linha_1)
print(linha_2)
print(linha_3)