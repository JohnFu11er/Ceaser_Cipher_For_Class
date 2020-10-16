# This program performs a Ceasar cypher shift once to the right: a --> b

alphabet = "abcdefghijklmnopqrstuvwxyz"
shifted = "bcdefghijklmnopqrstuvwxyza"  # change the value of this variable to change the ammount of shift
mapping = dict(zip(alphabet, shifted))
cypher_output = ""

# Read the source file plain.txt
with open('plain.txt', mode='rt') as plain:
    plain_input = plain.read()

# Apply right shift to plain.txt input and append to cypher_output
for letter in plain_input.lower():
    if letter in mapping:
        cypher_output += mapping[letter]
    else:
        cypher_output += letter

# Write cypher_output to cypher.txt file
with open('cypher.txt', mode='wt') as cypher:
    cypher.write(cypher_output)
