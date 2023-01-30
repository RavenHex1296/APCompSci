import string
import random

string.ascii_lowercase
alphabet = list(string.ascii_lowercase)

def decode_ceaser(input_string):
    possibilities = {}

    for n in range(0, 26):
        possibilities[n] = ""

    for key in possibilities:
        for element in input_string.lower():
            if element in alphabet:
                decoded_element = (alphabet.index(element) - key) % 26
                possibilities[key] += alphabet[decoded_element]

            else:
                possibilities[key] += element

    return possibilities


def get_key_from_value(val, input_dict):
    for key, value in input_dict.items():
        if val == value:
            return key


def encode(input_string, legend):
    encoded_text = ""

    for element in input_string:
        encoded_text += legend[element]

    return encoded_text


def decode(encoded_text, legend):
    decoded_text = ""

    encoded_text_list = [element for element in encoded_text.split("0.")]

    for letter in encoded_text_list[1:]:
        letter = "0." + letter
        decoded_text += get_key_from_value(letter, legend)

    return decoded_text

    

legend = {}


alphabet_stuff = alphabet + [" ", ":", "'", "/", '"', "?", ">", "<", ".", ",", ";", "[", "]", "{", "}", "+", "=", "-", "_", "(", ")", "!", "@", "#", "$", "%", "^", "&", "*", "`", "~", "\t", "\n"] + list(string.ascii_uppercase)
random.shuffle(alphabet_stuff)
numbers = [random.random() for _ in range(len(alphabet_stuff))]

for element in alphabet_stuff:
    legend[element] = ""

for key in legend:
    encoded_letter = numbers[alphabet_stuff.index(key)]
    legend[key] += str(encoded_letter)

#coding exercise 1 below
input_string = "Heaven is all gone Empty in my arms You wanna see us be nothing nothing Where do we belong? We have to stay strong We are an army of used up freaks Standing on the battleground Standing on the front Can't see my way out Standing on the pinnacle Standing on the sun Can't see my way out One by one we turn our hands to guns One by one they fall down Kept down so long Sick of living in the middle If you stand for nothing You'll fall for anything Our time is now We won't stand down Wake up scream out We are the chosen ones Standing on the battleground Standing on the front Can't see my way out Standing on the pinnacle Standing on the sun Can't see my way out One by one we turn our hands to guns One by one they fall down (they fall down) One by one they fall down Standing on the battleground Standing on the front Can't see my way out Standing on the pinnacle Standing on the sun Can't see my way out One by one we turn our hands to guns One by one they fall down One by one they fall down One by one they fall down One by one they fall down One by one they fall down One by one they fall down One by one they fall down"
encoded_text = encode(input_string, legend)
assert encoded_text != input_string
print("Successfully encoded the song lyrics")
decoded_text = decode(encoded_text, legend)
assert decoded_text == input_string
print("Successfully decoded the song lyrics")

#coding exercise 2:
input_string = "\tDefine and test two functions to encrypt and decrypt a single word based on some sort of key that you define. Your encode function should pass in an english word and return an encoded word. Your decode function should pass in an encoded word and return an english word. Then you should call each function with at least one test word. \n\n\tHint: This can be as simple or as complicated as you want! Some simple ideas are replacing all As with Zs and all Zs with As, a pig latin encoder and decoder, a key to replace all the letters with symbols, or morse code! Or anything else you can think of!\n\n\t This exercise is to understand what python data structures will be useful when we do slightly more difficult encryption projects (where the key won't be so simple). Think about data structures like lists and dictionaries. If you get stuck check out some of these resources:"
encoded_text = encode(input_string, legend)
assert encoded_text != input_string
print("Successfully encoded the paragraphs")
decoded_text = decode(encoded_text, legend)
assert decoded_text == input_string
print("Successfully decoded the paragraphs")