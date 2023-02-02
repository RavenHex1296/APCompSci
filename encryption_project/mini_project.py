rule1 = ['C', 'T', 'A', 'G']
rule2 = ['C', 'A', 'T', 'G']
rule3 = ['G', 'A', 'T', 'C']
rule4 = ['G', 'T', 'A', 'C']
rule5 = ['A', 'G', 'C', 'T']
rule6 = ['A', 'C', 'G', 'T']
rule7 = ['T', 'C', 'G', 'A']
rule8 = ['T', 'G', 'C', 'A']

def xor(bit1, bit2):
    if bit1 == bit2:
        return "0"

    return "1"


def encodeDNA(character, rule):
    charIndex = rule.index(character)
    return '{0:02b}'.format(charIndex)


def decodeDNA(binary, rule):
    charIndex = int(binary, 2)
    return rule[charIndex]


def convert_DNA_to_binary(DNA, rule):
    binary_DNA = ""

    for n in range(len(DNA)):
        binary_DNA += encodeDNA(DNA[n], rule)

    return binary_DNA


# finish the following function
def XOR_DNA(plainDNA, keyDNA, rule):
    plainDNA_number = convert_DNA_to_binary(plainDNA, rule)
    keyDNA_number = convert_DNA_to_binary(keyDNA, rule)

    encoded_dna_num = ""

    for n in range(0, len(plainDNA_number)):
        encoded_dna_num += xor(plainDNA_number[n], keyDNA_number[n])

    encoded_dna = ""

    for n in range(0, len(encoded_dna_num), 2) :
        encoded_dna += decodeDNA(encoded_dna_num[n] + encoded_dna_num[n + 1], rule)

    # return the encoded DNA based on the key and rule   
    return encoded_dna



  # EXTRA CREDIT


# MODIFY THE METHODS SO THAT USERS CAN CHOOSE FROM THE EIGHT POSSIBLE DNA RULES
# TRY TO FIGURE OUT THE RULES YOURSELF FIRST! IF YOU GET STUCK COME ASK ME :)
# REMEMBER WATSON CRICK SAYS A PAIRS WITH T & G PAIRS WITH C
assert XOR_DNA("ACGT", "CGTA", rule1) == "AGAG" 
assert XOR_DNA("AGAG", "CGTA", rule1) == "ACGT"
print("PASSED")