#input é uma função que solicita dados para o usuário, pode coletar dados da variável, sempre entra no tipo string (str)
#nome = input('Qual o seu nome? ')
numero_1 = (input('Digite um número: '))
numero_2 = (input('Digite outro numero ')) #isso serve para conseguir dar um "gato", pode gerar transtornos no futuro, não é bom colocar pois com int ele iria converter letras por exemplo

#o ideal seria fazer checagem (vamos aprender) e colocar o seguinte de forma correta
int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)
print(f'A soma dos números é: {int_numero_1 + int_numero_2}') #se colocar = depois da variável, ele ja puxa o = no final da variaveis