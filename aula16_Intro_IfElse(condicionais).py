#if / elif ....... /else
#se / se não se / se não

entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Você entrou no sistema')    #para colocar dentro do "bloco" do if, dar um tab embaixo pra digitar o print
                                        #pode ter vários códigos dentros desse bloco

elif entrada == 'sair':         #elif pode se repetir
        print ("Você saiu do sistema")
else:
    print('Você não digitou nem entrar e nem sair.')

#aqui já está fora dos blocos