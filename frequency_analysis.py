from pprint import pprint

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def get_frequency(source_file):
    ''' RETURNS FREQUENCY ANALYSIS OF A
        SELECTED TEXT FILE''' 
    
    _temp= {}
    # Opens and reads the designated source_file
    with open(source_file, mode='rt') as text:
        data = (text.read()).lower()

    # Records the counted occurence of each letter
    for letter in data:
        if letter in _temp:
            _temp[letter] += 1
        elif letter in alphabet:
            _temp[letter] = 1
            
    # Builds, sorts, and returns results of analysis
    answer = [[_temp[key],key] for key in _temp.keys()]
    answer.sort(reverse= True)
    return answer

# Calls the frequency functions and assigns results
plain_freq = (get_frequency('plain.txt'))
cypher_freq = (get_frequency('cypher.txt'))

# Outputs the results to the terminal
print("   PLAIN          CYPHER")
for i in range(0,len(plain_freq)):
    print(f"{(str(plain_freq[i])):11} ||  {(str(cypher_freq[i])):10}")