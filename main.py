import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def make_code():
    try:
        word = input("Enter the word: ").upper()
        output_list = [data_dict[letter] for letter in word]
        print(output_list)

    except KeyError:
        print("Sorry, only letters in the alphabet please")
        make_code()

    finally:
        make_code()

make_code()
