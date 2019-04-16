import os

def validate(dic, file_path):
	try:
		file = open(file_path, "r")
		msg = file.read().upper()
		file.close()
	except FileNotFoundError:
		print("arquivo não encontrado!")
		return False
	i = 0
	size = len(msg)
	out = ""
	while(i < size):
		if(msg[i] in dic):
			out += msg[i]
		i += 1
	try:
		file = open(file_path, "w")
		file.write(out)
		file.close()
	except FileNotFoundError:
		print("Arquivo não encontrado!")
		return False
	return True
