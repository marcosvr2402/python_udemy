#if / elif ....... /else
#se / se não se / se não
#não pode ter else ou elif sozinho, sem if
#else é sempre a última condição, último a ser executado

condicao1 = False #pode marcar como breakpoint, a marcação vermelha
condicao2 = False
condicao3 = True
condicao4 = True

if condicao1:
    print('Código para condição 1')
    print('Código para condição 1')
elif condicao2:   
    print('Código para condição 2')
elif condicao3:
    print("Código para condição 3")
elif condicao4:
    print("Código para condição 4")

if 10 == 10:
    print("terminou")