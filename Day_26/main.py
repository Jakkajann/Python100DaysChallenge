import pandas 

nato_data = pandas.read_csv("Day_26/nato.csv")

nato_dict = {row.letter:row.code for (index, row) in nato_data.iterrows()}

word = input("Enter a word: ").upper()
output_list = [nato_dict[letter] for letter in word]
print(output_list)