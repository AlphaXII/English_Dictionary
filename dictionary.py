import json
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("data.json", "r"))          # stores the json file as a dictionary
word = str(input("Find word in dictionary: \n")).lower()    # user input for queried word

def match_word(word_in):
    global word
    holder = get_close_matches(word_in, data.keys())
    match_ratio = float(0.0)
    best_match_word = ""
    for i in holder:
        if SequenceMatcher(None, i, word).ratio() > match_ratio:
            best_match_word = i
            match_ratio = float(SequenceMatcher(None, i, word).ratio())
    if len(holder) != 0 and match_ratio != float(1.0):
        user_check = input(word + " was not found, did you mean [" + best_match_word.upper() + "] instead? Y or N\n")
        if user_check.lower() == "y":
            word = best_match_word
        else:
            word = ""


match_word(word)

'''
Passes the json file to the function
'''
def word_search(word_in):
    if word_in in data:
        return data.get(word_in)
    else:
        return 0


if word_search(word) == 0:
    print("The word was not found. Please make sure the word exists.")
else:
    for i in word_search(word):
        print(i)

