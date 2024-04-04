#Operador lógicos
#and (e) or (ou) not (não)
# and --- Todas as condições precisam ser verdadeiras.
# Se qualquer valor for considerado falso, a expressão inteira será avaliada como falso e será avaliada naquele valor
# São considerados falsy (que vc já viu)
#  0 0.0 '' False - são considerados falsos pelo python
# Também existe o tipo None que é usado para representar um não valor


#entrada = input('[E]ntrar [S]air: ')
#senha_digitada = input ('Senha: ')
#senha_permitida = '123456'

#if (entrada == 'E' or entrada == 'e')1 and senha_digitada == senha_permitida:
#print('Entrar')

#else:
#print('Sair')

#Avaliação de curto circuito, ele le a expressão inteira, reproduz só o false e retorna nele

# Na avaliação de curto circuito, ele sempre avalia a primeira verdadeira quando for OR, logo no exemplo abaixo ele vai dar print no 'abc', da da pra jogar o 'or' em uma variável

print(0 or False or 0 or 'abc' or True or False)