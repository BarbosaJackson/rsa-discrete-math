import os
from utils.validate_rsa import validate

dic = ['A', 'B', 'C', 'D', 'E','F', 'G', 'H','I','J','K','L','M','N','O','P','Q','R','S', 'T','U','V', 'W','X','Y', 'Z',' ']

def check_prime(x):
	if(x == 2):
		return True
	elif(x % 2 == 0):
		return False
	i = 3
	while(i <= x ** 0.5):
		if(x % i == 0):
			return False
		i += 2
	return True

def read_prime_number(text):
	number = int(input(text))
	while(check_prime(number) == False):
		print("Tente um número primo")
		number = int(input(text))
	return number

def read_file(file_path, text_error):
	try:
		file = open(file_path, "r")
		msg = file.read()
		file.close()
		return msg
	except FileNotFoundError:
		print(text_error)
		return ""

def write_file(file_path, msg):
	try:
		file = open(file_path, "w")
		file.write(msg)
		file.close()
	except FileNotFoundError:
		print("nao conseguiu criar o arquivo")

def gcd(a, b):
	if(a % b == 0):
		return b
	else:
		return gcd(b, a % b)

def crypt(file_path, n, e):
	msg = read_file(file_path, "arquivo de entrada não encontrado!")
	# msg = ''.join([l for l in msg if l in dic])
	cryptMsg = ""
	i = 0
	while i < len(msg):
		m = msg[i]
		cryptMsg = cryptMsg + str(((dic.index(m) ** e) % n))
		if(i + 1 != len(msg)):
			cryptMsg += ","
		i += 1
	write_file(file_path, cryptMsg)

def decrypt(file_path, n, d):
	msg = read_file(file_path, "Arquivo de entrada não encontrado!")
	i = 0
	decryptMsg = ""
	while(i < len(msg)):
		C = ""
		while(i < len(msg) and msg[i] != ','):
			C += msg[i]
			i += 1
		i += 1
		C = int(C)
		decryptMsg += dic[(C ** d) % n]
	write_file(file_path, decryptMsg)

def findInverse(e, fiN) :
	d = 0
	while( int((d * e) % fiN) != 1):
		d += 1
	return d

def menu():
	p = 0
	q = 0
	e = 0
	fiN = 0
	while(True):
		op = int(input("[ 1 ] Gerar chave pública\n[ 2 ] Criptografar\n[ 3 ] Descriptografar\n[ 0 ] Sair\n=> "))
		if(op == 1):
			p = read_prime_number("p = ")
			q = read_prime_number("q = ")
			e = int(input("e = "))
			N = p * q
			fiN = (p - 1) * (q - 1)
			while(gcd(e, fiN) != 1):
				print("'e' não é primo em comum com (p-1)(q-1), escolha outro número")
				e = int(input("e = "))
			public_key = str(N) + " " + str(e)
			write_file("public_key.txt", public_key)
		elif(op == 2):
			file_path = input("Digite o nome do arquivo: ")
			if(validate(dic, file_path)):
				try:
					file = open("public_key.txt")
					N, e = file.read().split(" ")
					N = int(N)
					e = int(e)
					crypt(file_path, N, e)
				except FileNotFoundError:
					print("chave não foi gerada!")
		elif(op == 3):
			file_path = input("Digite o nome do arquivo: ")
			d = findInverse(e, fiN)
			decrypt(file_path, N, d)
		elif(op == 0):
			return 0
menu()

# pra executar phyton3 <nome_do_arquivo>.py
