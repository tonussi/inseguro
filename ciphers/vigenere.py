#!/usr/bin/python

import sys, getopt

class Error(Exception):
    """Deciphering Exception Bad Password as Input."""
    pass

def vigenereCipher(plainText, key):

	# @see [asciitable] http://www.asciitable.com/
	# @authors:
	#   - Bruno Souza Silva <bruno.souza.silva@grad.ufsc.br>
	#   - Guilherme Trilha <guitrilha@icloud.com>
	#   - Lucas Tonussi <lucas.tonussi@grad.ufsc.com>

	cipherText = list()

	plainText.lower()
	key.lower()

	# print key[0 % len(key)]
	# print key[1 % len(key)]
	# print key[2 % len(key)]

	# print ord(key[0 % len(key)])
	# print ord(key[1 % len(key)])
	# print ord(key[2 % len(key)])

	j=0
	for letter in plainText:
		cipherText.append((ord(letter) - ord('a') + ord(key[j % len(key)]) - ord('a')) % 26 + ord('A'))
		j+=1

	return cipherText

def vigenereDecipher(cipherText, key):

	cipherTextUpper = list()

	plainText = ''
	plaint = ''

	for c in cipherText:
		temp = chr(c).upper()
		cipherTextUpper.append(temp)

	# print ord(key[0]) % len(key) - ord('a')
	# print ord(key[1]) % len(key) - ord('a')
	# print ord(key[2]) % len(key) - ord('a')

	key.lower()

	k=0
	for letter in cipherText:
		cipherAt = ord(chr(letter)) - ord('A')
		keyAt = ord(key[k % len(key)]) - ord('a')
		resultKey = cipherAt - keyAt

		# print resultKey

		if resultKey < 0:
			resultKey = resultKey + 26
			# print resultKey

		resultKey = resultKey % 26 + ord('a')
		plainText = plainText + chr(resultKey)

		k+=1

	return plainText

def init(p, k):
	plainText = p #"whatanunpredictableworldweliveright"
	key = k #"gandalf"

	encryptedText = vigenereCipher(plainText, key)
	decriptedText = vigenereDecipher(encryptedText, key)

	textoCriptografadoAscii = ""
	for value in encryptedText:
		textoCriptografadoAscii += chr(value)

	return "Texto decifrado: ", decriptedText,                  \
	       "Texto encriptado (inteiros): ", encryptedText,      \
	       "Texto encriptado (ascii):", textoCriptografadoAscii \

def writef(nomeArquivo, resultadosCripto):
	try:
		file = open(nomeArquivo, "w")

	except IOError:
		print "There was an error writing to", nomeArquivo
		sys.exit()

	file.write(str(resultadosCripto))
	file.write("\n")
	file.close()

def qualificaTextoPlano(arquivoTextoPlano):
	plaintext = ''
	for line in arquivoTextoPlano.readlines():
		if len(line) > 1 and line != '\n':
			plaintext += str(line)
	# print plaintext.replace('!@#$%^&*()[]{};:,./<>?\|`~-=_+', '').strip().lower()
	return plaintext.replace('!@#$%^&*()[]{};:,./<>?\|`~-=_+', '').strip().lower()

def readf(nomeArquivo):
	try:
		arquivo = open(nomeArquivo, "r")
		plaintext = qualificaTextoPlano(arquivo)
	except IOError:
		print "There was an error reading file"
		sys.exit()
	arquivo.close()
	return plaintext


def main(argv):
	inputfile = ''
	nomeArquivo = ''

	try:
		opts, args = getopt.getopt(argv,"h:i:k:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print 'test.py -i <inputfile> -o <nomeArquivo>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'Exemplo :: vigenere.py -i <textoPlano.txt> -o <cipher.txt>'
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-k", "--palavaChave"):
			palavaChave = arg
		elif opt in ("-o", "--ofile"):
			nomeArquivo = arg

	print 'Texto plano de entrada: "', inputfile
	print 'Criptografando...'

	textoPlano = readf(inputfile)
	resultadosCripto = init(textoPlano, palavaChave)

	print 'Seus resultdos em: "', nomeArquivo

	writef(nomeArquivo, resultadosCripto)

if __name__ == "__main__":
   main(sys.argv[1:])
