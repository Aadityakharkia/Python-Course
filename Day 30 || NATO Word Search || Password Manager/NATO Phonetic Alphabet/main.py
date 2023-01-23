# creating a programme to get the Nato words from alphabets
# Using Pandas module

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

#--------------------------------- Using list dictionary comprehension to create a disctionary -------------------

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#-------------------------------------- Generating Words list by taking inputs -----------------------------------

def generate():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate()
    else:
        print(output_list)

generate()

