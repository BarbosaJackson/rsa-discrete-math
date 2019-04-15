import os

def validate(dic, file_path):
	file = open(file_path, "r")
	msg = file.read().upper()
	file.close()
	i = 0
	size = len(msg)
	out = ""
	while(i < size):
		if(msg[i] in dic):
			out += msg[i]
		i += 1
	file = open(file_path, "w")
	file.write(out)
	file.close()
