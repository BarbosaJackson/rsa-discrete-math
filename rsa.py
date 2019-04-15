import os

dic = ['A', 'B', 'C', 'D', 'E','F', 'G', 'H','I','J','K','L','M','N','O','P','Q','R','S', 'T','U','V', 'W','X','Y', 'Z',' ']

def gcd(a, b):
	if(a % b == 0):
		return b
	else:
		return gcd(b, a % b)

def crypt(filePath, n, e):
	file = open(filePath, "r")
	msg = file.read()
	cryptMsg = ""
	i = 0
	while i < len(msg):
		m = msg[i]
		cryptMsg = cryptMsg + str(((dic.index(m) ** e) % n))
		if(i + 1 != len(msg)):
			cryptMsg += ","
		i += 1
	file.close()
	os.system("rm -r " + filePath)# apaga o arquivo original
	os.system("touch " + filePath) # cria um novo arquivo com o mesmo nome no mesmo local do original
	file = open(filePath, "w")# Abrindo o arquivo para escrever a msg criptografada 
	file.write(cryptMsg)# escreve no arquivo
	file.close()

def decrypt(filePath, n, d):
	file = open(filePath, "r")
	msg = file.read()
	file.close()
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
	os.system("rm -r " + filePath)
	os.system("touch " + filePath)
	file = open(filePath, "w")
	file.write(decryptMsg)
	file.close()

def findInverse(e, fiN) : #calculando o "d" da chave privada (n,d)
	d = 0
	while( int((d * e) % fiN) != 1):
		d += 1
	return d

def validateCryptoFile(filePath):
	myFile = open("utils/validate_input", "w")
	myFile.write(filePath)
	myFile.close()
	os.system("python3 utils/validate_rsa.py < utils/validate_input")

def menu():
	p = 0
	q = 0
	e = 0
	while(True):
		op = int(input("[ 1 ] Gerar chave pública\n[ 2 ] Criptografar\n[ 3 ] Descriptografar\n=>"))
		if(op == 1):
			p = int(input("p = "))
			q = int(input("q = "))
			e = int(input("e = "))
			N = p * q
			fiN = (p - 1) * (q - 1)
			while(gcd(e, fiN) != 1):
				print("'e' não é primo em comum com (p-1)(q-1), escolha outro número")
				e = int(input("e = "))
		elif(op == 2):
			file = input("Digite o nome do arquivo: ")
			validateCryptoFile(file)		
			crypt(file, N, e)
		elif(op == 3):
			file = input("Digite o nome do arquivo: ")
			d = findInverse(e,fiN)
			decrypt(file, N, d)
menu()

# pra executar phyton3 <nome_do_arquivo>.py