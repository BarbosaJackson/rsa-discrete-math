import os

dic = ['A', 'B', 'C', 'D', 'E','F', 'G', 'H','I','J','K','L','M','N','O','P','Q','R','S', 'T','U','V', 'W','X','Y', 'Z',' ']

def main():
	path = input()
	file = open(path, "r")
	msg = file.read().upper()
	file.close()
	i = 0
	size = len(msg)
	out = ""
	while(i < size):
		if(msg[i] in dic):
			out += msg[i]
		i += 1
		file = open(path, "w")
		file.write(out)
		file.close()
main()