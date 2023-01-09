import pandas

user_input = str(input("Please enter a word -- ")).upper()

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index,row) in data.iterrows()}

output = [phonetic_dict[letter] for letter in user_input]
print(output)
