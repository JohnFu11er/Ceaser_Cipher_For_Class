# This program looks through all possible Caesar cipher mappings
# to find one that has text matching your search criteria. The word
# "the" is very common and can usually be found in a block of text.

import os

# Defining variables - probably an easier way to make the alph_list
alphabet = "abcdefghijklmnopqrstuvwxyz"
alph_list = {
    '0': "bcdefghijklmnopqrstuvwxyza",
    '1': "cdefghijklmnopqrstuvwxyzab",
    '2': "defghijklmnopqrstuvwxyzabc",
    '3': "fghijklmnopqrstuvwxyzabcde",
    '4': "fghijklmnopqrstuvwxyzabcde",
    '5': "ghijklmnopqrstuvwxyzabcdef",
    '6': "hijklmnopqrstuvwxyzabcdefg",
    '7': "ijklmnopqrstuvwxyzabcdefgh",
    '8': "jklmnopqrstuvwxyzabcdefghi",
    '9' : "klmnopqrstuvwxyzabcdefghij",
    '10' : "lmnopqrstuvwxyzabcdefghijk",
    '11' : "mnopqrstuvwxyzabcdefghijkl",
    '12' : "nopqrstuvwxyzabcdefghijklm",
    '13' : "opqrstuvwxyzabcdefghijklmn",
    '14' : "pqrstuvwxyzabcdefghijklmno",
    '15' : "qrstuvwxyzabcdefghijklmnop",
    '16' : "rstuvwxyzabcdefghijklmnopq",
    '17' : "stuvwxyzabcdefghijklmnopqr",
    '18' : "tuvwxyzabcdefghijklmnopqrs",
    '19' : "uvwxyzabcdefghijklmnopqrst",
    '20' : "vwxyzabcdefghijklmnopqrstu",
    '21' : "wxyzabcdefghijklmnopqrstuv",
    '22' : "xyzabcdefghijklmnopqrstuvw",
    '23' : "yzabcdefghijklmnopqrstuvwx",
    '24' : "zabcdefghijklmnopqrstuvwxy"
}

# Gather user input
os.system('cls')
cypher_text = (input("Enter the encrypted text: ")).lower()
search_word = (input("Enter one word that may be in the message: ")).lower()

# Decodes encryptoed message with every possible mapping
for key in alph_list.keys():
    _temp = ""
    local_dict = (dict(zip(alphabet,alph_list[key])))
    for letter in cypher_text:
        if letter in local_dict.keys():
            _temp += local_dict[letter]
        else:
            _temp += letter
    
    # Prints the mapping that has a match for the searched word
    if search_word in _temp:
        print(f"{_temp}  ||  Mapping = a:{local_dict['a']}")