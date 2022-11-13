student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)
alpha_data = pandas.read_csv("nato_phonetic_alphabet.csv")

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
alpha_dict = {row.letter:row.code for (index, row) in alpha_data.iterrows()}

# alpha_dic = {alpha, word for (alpha,word) in }
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():

    word = input("Enter a word: ").upper()

    try:
        final_list = [alpha_dict[char] for char in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(final_list)


generate_phonetic()

# final_list = []
# for char in word:
#     for (key1, word1) in alpha_dict.items():
#         if key1 == char:
#             final_list.append(word1)
