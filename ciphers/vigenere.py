#!/usr/bin/python

import sys, getopt

"""
<h>Vigenere Cipher Crypto Analysis</h>

<p>Inseguro uma vez que você sae o tamnho da palavra chave.</p>
<p>Se for n o tamanho, você pode quebrar em n cosets e atacar o
   cifrador usando analise de frequência</p>

<h>Friedman Test</h>

<p>Achando a indidência da conincidência para um ensaio do textocifrado
   podemos indicar quando ou não a substituição polialfabética foi usada para
   encriptar a mensagem. A indicência da conincidência é a probabilidade de que
   2 letras selecionadas aleatóriamente são as mesmas.</p>
<pre>I = 1/(n(n-1)) * sum from {i = 0} to {i = 25} of n_i * (n_i - 1)</pre>
<p>Onde n0, n1, n2, ..., n25 são respectivamente A, B, C, D, ..., Z</p>
<p>Para achar a estimativa do tamanho da chave:</p>
<pre>k_english = 0.0265 * n / (0.065 - I + n * (I - 0.085)</pre>

<h>Kasisike Test</h>
<p>Apenas pega o texto cifrado e busca por padrões de grupos incidência assim
   medindo a distância entre eles, consegue-se uma nossao do tamanho da chave
   que no Vigenere é uma chave duplicada para ficar do tamanho do texto.
   O Vigenere é uma ideia de que a chave recebe tratamento de segurança também
   não apenas o texto.</p>
"""
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

"""
n: numeral
arr: array
"""
def friedman(n):
    res = 0
    for letter in map(ord, ['A', 'B', 'C', 'D', 'E', 'R', 'F', 'G', 'H', 'I', 'J', 'L', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'W', 'Z']):
        res = (res + letter - 1) * letter
    res = res * (1 / (n * (n - 1)))
    return res

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
