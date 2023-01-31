def xor(bit1, bit2):
    if bit1 == bit2:
        return "0"

    return "1"


def xor_on_byte(byte, key):
    encryptedByte = ""

    for n in range(len(byte)):
        encryptedByte += xor(byte[n], key[n])

    return encryptedByte


assert xor_on_byte("11011001", "01001111") == "10010110"
assert xor_on_byte("11111111", "00000000") == "11111111"
assert xor_on_byte("11001111", "00001000") == "11000111"

#print(ord("a")) #ord gives ascii number of a
#print(bin(97)) #bin converts number to binary number

def convert_word_to_binary(word):
    word_start = ""

    for n in range(len(word)):
        word_start += bin(ord(word[n]))[2:]

    return word_start


def convert_binary_to_letter(binary):
    return chr(int(binary)) #chr converts binary to number


start = "pop"
key = "cat"


print(xor_on_byte(convert_word_to_binary(start), convert_word_to_binary(key)))