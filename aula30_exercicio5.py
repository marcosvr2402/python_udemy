'''
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é (nome)
        Seu nome invertido é (nome invertido)
        Seu nome contém (ou não) espaços
        Seu nome tem (n) letras
        A primeira letra do seu nome é (letra)
        A última letra do seu nome é (letra)

Se nada for digitado em nome ou idade:
    Exiba: 'Desculpe, você deixou campos vazios.'
'''

nome = input('Digite seu nome: ').strip()
nome_invertido = nome[::-1]
n_letras = len(nome)
primeira_letra = nome[0] if nome else ''
ultima_letra = nome[-1] if nome else ''

if nome and nome.strip():
    idade = input('Digite sua idade: ').strip()
    if idade and idade.strip():
        print('Seu nome é ', nome)
        print('Seu nome invertido é', nome_invertido)
        print('Seu nome tem', n_letras, 'letras')
        print('A primeira letra do seu nome é', primeira_letra)
        print('A última letra do seu nome é', ultima_letra)
        if ' ' in nome:
            print('Seu nome contém espaços')

        else:
            print('Seu nome não contém espaços')     
    
else:
    print('Desculpe, você deixou campos vazios')



