"""Exercício Python 3: Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido."""
import math
numero = float(input("Digite um número: "))

if numero > 0:
	raizq = math.sqrt(numero)
	print( "A raiz quadrada do número {} é {:.2f}.".format(numero, raizq))
elif numero == 0:
	print("O número digitado é zero.")
else:
	print("Número inválido")