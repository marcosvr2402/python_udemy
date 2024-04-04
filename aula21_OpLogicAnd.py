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

# and é usado para checar mais de uma expressão/condição
#if entrada == 'E' and senha_digitada == senha_permitida:
#    print('Entrar')

#else:
#    print('Sair')

#Avaliação de curto circuito, ele le a expressão inteira, reproduz só o false e retorna nele

#print(True and False and True)
#print(True and 0.0 and True)
#print(True and True and True)

if 1 and 1:
    print(True and 1 and False)