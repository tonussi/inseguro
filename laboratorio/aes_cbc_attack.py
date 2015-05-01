lastPlaintextBlock = 'user=joao;\x06\x06\x06\x06\x06\x06'
ciphertextBlock = 'B\xd9\xf7\xe5Y\xbd{n\xdczntwl\xe4\xe8'

plaintextByteList = list(bytearray(lastPlaintextBlock))
ciphertextByteList = list(bytearray(ciphertextBlock))

aes = []

for i in range(len(plaintextByteList)):
	aes.append(plaintextByteList[i] ^ ciphertextByteList[i])

ciphertextByteList[5] = ciphertextByteList[5] ^ (ord('a') ^ ord(chr(plaintextByteList[5])))
ciphertextByteList[6] = ciphertextByteList[6] ^ (ord('d') ^ ord(chr(plaintextByteList[6])))
ciphertextByteList[7] = ciphertextByteList[7] ^ (ord('m') ^ ord(chr(plaintextByteList[7])))
ciphertextByteList[8] = ciphertextByteList[8] ^ (ord('i') ^ ord(chr(plaintextByteList[8])))
ciphertextByteList[9] = ciphertextByteList[9] ^ (ord('n') ^ ord(chr(plaintextByteList[9])))
ciphertextByteList[10] = ciphertextByteList[10] ^ 6 ^ 5
ciphertextByteList[11] = ciphertextByteList[11] ^ 6 ^ 5
ciphertextByteList[12] = ciphertextByteList[12] ^ 6 ^ 5
ciphertextByteList[13] = ciphertextByteList[13] ^ 6 ^ 5
ciphertextByteList[14] = ciphertextByteList[14] ^ 6 ^ 5
ciphertextByteList[15] = ciphertextByteList[15] ^ 6 ^ 5

newPlainTextBlock = []

for i in range(len(ciphertextByteList)):
	newPlainTextBlock.append(aes[i] ^ ciphertextByteList[i])

for i in range(0, 16):
	print chr(newPlainTextBlock[i])
