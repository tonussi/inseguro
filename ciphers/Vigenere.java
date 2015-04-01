public class Vigenere {

	// http://www.asciitable.com/

	public static void main(String[] args) {
		String key = "gandalf";
		String plainText = "whatanunpredictableworldweliveright";

		String encryptedText = vigenereCipher(plainText, key);
		String decriptedText = vigenereDecipher(encryptedText, key);

		System.out.println(encryptedText);
		System.out.println(decriptedText);
		System.out.println((-2) % 26);

	}

	public static String vigenereCipher(String plainText, String key) {
		String cipherText = "";
		plainText.toLowerCase();
		plainText.trim();
		key.toLowerCase();
		for (int i = 0; i < plainText.length(); i++) {
			char letter = (char) (((int) plainText.charAt(i) - (int) 'a'
					+ (int) key.charAt(i % key.length()) - (int) 'a') % 26 + (int) 'A');
			cipherText = cipherText + letter;
		}
		return cipherText;
	}

	public static String vigenereDecipher(String cipherText, String key) {

		String plainText = "";
		String plaint = "";
		cipherText.toUpperCase();
		key.toLowerCase();

		for (int i = 0; i < cipherText.length(); i++) {
			int cipherAt = (int) cipherText.charAt(i) - (int) 'A';
			int keyAt = (int) key.charAt(i % key.length()) - (int) 'a';
			int resultKey = (cipherAt - keyAt);

			System.out.println(resultKey);

			if (resultKey < 0) {
				resultKey = resultKey + 26;
				System.out.println(resultKey);
			}

			resultKey = (int)resultKey % 26 + (int) 'a';
			plainText = plainText + (char) resultKey;

		}
		return plainText;
	}

}
