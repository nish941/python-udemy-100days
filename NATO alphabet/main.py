#Looping through dictionaries:
#for (key, value) in student_dict.items():
#Loop through rows of a data frame
#for (index, row) in student_data_frame.iterrows():

import pandas
data = pandas.read_csv("nato_alphabet.csv")
data_frame = pandas.DataFrame(data)

#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo", .....}

new_dict = {row.letter:row.code for (index,row) in data_frame.iterrows() }
print(new_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate():
    word = input("Please input a word.\n").upper()  # all letters are capitalized
    try:
        result = [ new_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters please")
        generate()
    else:
        print(result)

generate()