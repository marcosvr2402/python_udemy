#Operador lógicos
#and (e) or (ou) not (não)
# and --- Todas as condições precisam ser verdadeiras.
# Se qualquer valor for considerado falso, a expressão inteira será avaliada como falso e será avaliada naquele valor
# São considerados falsy (que vc já viu)
#  0 0.0 '' False - são considerados falsos pelo python
# Também existe o tipo None que é usado para representar um não valor

#O que for TRUE vira FALSE, o que for FALSE vira TRUE
#senha = input('Senha: ')

#if not senha: #o not inverteu a formula
#print('Você não digitou nada.')


#Avaliação de curto circuito, ele le a expressão inteira, reproduz só o false e retorna nele

#Ele inverte o valor existente

print(not True) # vira False
print(not False) # vira True