"""
Fatiamento de strings
 0123456789 >> índice positivo
 Olá mundo
-98764321 >> índice negativo
Fatiamente [ i:f:p] [::]
Obs: a função len retorna a quantidade de caracteres 
da strig
"""

variavel = "Olá mundo"
print(variavel[5:8]) # para pegar o índice final, ele omite o final, deve-se colocar o que quer +1 para ele entender o final, os dois pontos (:) indicam o fatiamento
#no fatiamento, o primeiro índice é o início
print(len(variavel)) #o len conta caracteres
#no fatiamento é i(primeiro índice), f é o fim de onde vai analisar, e o p é o passo, seria como seria a contagem
print(variavel[0:1]) #no exemplo a contagem, o passo, está de 2 em 2, se o número do passo for negativo, ele começa à contar "para trás"




