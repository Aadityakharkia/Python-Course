# Worked on Data and Files

# The aim of the project is to get the data from input and create a output

placeholder = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(placeholder,stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)