def xor(bit1, bit2):
    if bit1 == bit2:
        return "0"

    return "1"


def xor_on_byte(byte, key):
    encryptedByte = ""

    for n in range(len(byte)):
        encryptedByte += xor(byte[n], key[n])

    return encryptedByte


characters = [
    # lowercase characters
'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    # uppercase characters
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    # space and symbols
    ' ',',','.','?','!','@','#','$','&','*','(',')'
]

# use this method to encode an alphabet character into a binary string
def encode(character):
    charIndex = characters.index(character)
    return '{0:06b}'.format(charIndex)

# use this method to decode a binary string into an alphabet character
def decode(binary):
    charIndex = int(binary, 2)
    return characters[charIndex]

def convert_word_to_binary(word):
    word_start = ""

    for n in range(len(word)):
        word_start += encode(word[n])

    return word_start


def xorEncryptor(input_string, key):
    input_string_num = convert_word_to_binary(input_string)
    key_num = convert_word_to_binary(key)
    encrypted_string_num = ""

    for n in range(0, len(input_string_num)):
        encrypted_string_num += xor(input_string_num[n], key_num[n])

    encrypted_string = ""

    for n in range(0, len(encrypted_string_num), 6) :
        encrypted_string += decode(encrypted_string_num[n] + encrypted_string_num[n + 1] + encrypted_string_num[n + 2] + encrypted_string_num[n + 3] + encrypted_string_num[n + 4] + encrypted_string_num[n + 5])

    return encrypted_string


assert xorEncryptor(xorEncryptor("hello", "world"), "world") == "hello"
assert xorEncryptor(xorEncryptor("hi ms. orret", "to dr. jekyl"), "to dr. jekyl") == "hi ms. orret"
assert xorEncryptor(xorEncryptor("pasadena high school", "papparazzi hide poorly"), "papparazzi hide poorly") == "pasadena high school"
assert xorEncryptor(xorEncryptor("&avrvLYpjgiWtmewbSfq bl", "Beaver believers, leave"), "Beaver believers, leave") == "&avrvLYpjgiWtmewbSfq bl"
assert xorEncryptor(xorEncryptor("aaaaaankao  )lx@EAC@?wyz", "Never lend a penguin your gown"), "Never lend a penguin your gown") == "aaaaaankao  )lx@EAC@?wyz"
assert xorEncryptor(xorEncryptor("aaaaaaaaaaaaufdInK#uaaardd!?eeejMaynC", "Never gonna frown, and roam away, adieu"), "Never gonna frown, and roam away, adieu") == "aaaaaaaaaaaaufdInK#uaaardd!?eeejMaynC"
print("PASSED")