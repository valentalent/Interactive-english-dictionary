import json
from difflib import get_close_matches

#load data
data = json.load(open("data.json"))

#define function
def translate(word):
    #bring to lowercase
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[word.title()]
    elif word.upper() in data: #in case user enters words like USA or NATO
        return data[word.upper()]
    elif len (get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        yesno = input("Did you mean %s? Enter Y(Yes) or N(No)." % get_close_matches(word, data.keys())[0])
        yesno = yesno.upper()
        if yesno == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yesno == 'N':
            return "The word doesn't exist."
        else:
            return "Wrong entry."
    else:
        return "That word doesn't exist."

#user input
word = input("Enter word: ")

output= (translate(word))

if type(output) == list:
    for item in output:
        print(item)
else: 
    print(output)