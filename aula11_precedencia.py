#Ordem do que vai ser executado numa expressão matemática
#1. (n  + n) parenteses, os mais internos são os que serão feitos primeiro
#2. ** exponenciação (potenciação)
#3. * / // % multiplicação, divisão, divisão inteira e módulo
#4. +- adição e subtração

conta_1 = (1 + 1) ** (5 + 5)
print(conta_1)