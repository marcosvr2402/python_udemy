"""
Formação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
= - Força um número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""

variavel = "ABC"
print(f'{variavel}')
print(f'{variavel: >10}') #esse pad vai preencher com 10 caracteres na esquerda
print(f'{variavel:T<10}') #esse pad vai preencher com 10 caracteres na direita
print(f'{1000.08548487484:,.1f}') #isso aqui ele reduz as casas decimais para o número após o ponto, se vc colocar um + antes da , é pra indicar se o numero for positivo