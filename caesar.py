def alphabet_position(letter):
    letter = letter.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return alphabet.find(letter)

def rotate_character(char, rot):
    alphabetL = 'abcdefghijklmnopqrstuvwxyz'
    alphabetU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if char.isalpha() == False:
        return char
    else:
        rotated_index = alphabet_position(char) + rot
        if char.islower() == True:
            if rotated_index < 26:
                return alphabetL[rotated_index]
            else:
                return alphabetL[rotated_index % 26]
        else:
            if rotated_index < 26:
                return alphabetU[rotated_index]
            else:
                return alphabetU[rotated_index % 26]

def encrypt(text, rot):
    encrypted = ''
    for char in text:
        encrypted = encrypted + rotate_character(char, rot)

    return encrypted
