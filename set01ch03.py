hex_code = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
ascii_code = hex_code.decode('hex')

#Requires all alphanumeric combinations
available_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .\'",?!'


def execute_xor_on_chars(char1, char2):
    # chr -> return the character of one ASCII code
    # ord -> return ASCII code of a character
    char = chr(ord(char1) ^ (ord(char2)))
    return char


for available_char in available_chars:
    result = ''
    for char in ascii_code:
        result += execute_xor_on_chars(char, available_char)

    #Likely that a sentence would contain all 5 vowels
    if 'a' in str(result) and 'i' in str(result) and 'e' in str(result) and 'o' in str(result) and 'u' in str(result):
        print(result)
