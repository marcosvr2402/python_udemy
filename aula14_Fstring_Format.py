a = 'A'
b = "B"
c = 1.1
string = 'a={nome1} b={nome2} c={nome3:.2f}' #se colocar chave, ele puxa a primeira variavel; #erro OUT OF RANGE significa que esta procurando um item que acabou
formato = string.format(#quando uma função está dentro de um objeto, ela é chamada de método (method)
    nome1=a, #tudo que vier depois de um parâmetro nomeado tem que ser nomeado
     nome2=b,
      nome3=c) #tudo que tem uma ordem (índice), começa do 0, entao o a no 0, b 1 c 2 #parâmetro nomeado é quando da nome pras coisas dentro das funções

print(formato)
print('"Já sei!"')

numero_1 = 10
numero_2 = 20
resultado = numero_1 * numero_2
print(resultado)