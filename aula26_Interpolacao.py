#Interpolação básica de strings
# s- string
# d e i - int
# f - float
#  x e X - Hexadecima (ABCDEF0123456)

nome = 'Marcos'
preco = 100.98
variavel = '%s, o preço total foi R$%.2f' % (nome, preco) #interpolação é o % antes de alguma das letras, no caso do f ali, do float, coloca-se .numerof pra dar o numero de casas decimais
print(variavel)
print('O hexadecimal de %d é %04x' % (15, 15))