import sys
ALFABETO = 'abcdefghijklmnopqrstuvwxyz'
ROT = 5

def cifrar(message, dir):
	m = ''
	for c in message:
		if c in ALFABETO:
			c_index = ALFABETO.index(c)
			m += ALFABETO[(c_index + (dir * ROT)) % len(ALFABETO)]
		else:
			m += c
	return m

def encrypt(message):
	return cifrar(message, 1)

def decrypt(message):
	return cifrar(message, -1)

def main():
	command = sys.argv[1].lower()
	message = sys.argv[2].lower()

	if command == 'encrypt':
		print(encrypt(message))
	elif command == 'decrypt':
		print(decrypt(message))
	else:
		print(command + ' -> command not found')

if __name__ == '__main__':
    main()
