import random,unicodedata # it imports the random library and the unicodedata library to find a random word and to remove accents
from pathlib import Path # to import a file from the computer

dictionnary = Path("fr.txt").read_text(encoding="utf-8").split("\n") # pathlib opens a text file (fr.txt). The read_text reads the contents of the file and store it as a string. The encoding parameter is "utf-8" to make sure that any special characters in the file are read correctly. The string is split by newline characters ("\n") = a list of strings where each element is a line from the file.

tofind = random.choice(dictionnary) #
tofind = unicodedata.normalize("NFD", tofind).encode("ascii", "ignore").decode("ascii")

lenght = len(tofind)
print("", tofind, "\n", "Length of the word  : ", len(tofind))

def display(lenght):
    global truc
    print("" ,tofind[0], end="")
    for i in range(lenght - 1):
        print("_", end="")
        truc += "_"
    print()

def replace(user_input, tofind):
    global truc
    truc_list = []
    for letter in truc:
        truc_list.append(letter)
    for i in range(len(user_input)):
        if tofind[i] == user_input[i]:truc_list[i] = tofind[i]
    truc = "".join(truc_list)
    return truc

def letter(user_input, tofind):

    good_word = []
    wrong_letter = []
    letter_find = []
    liste = zip((user_input), (tofind))

    for letter in tofind:
        good_word.append(letter)
    for element in liste:
        if element[0] == element[1] :
            letter_find.append(element[0])
            good_word.remove(element[0])
    for letter in user_input:
        if letter in good_word and letter not in letter_find:
            wrong_letter.append(letter)
            good_word.remove(letter)
        elif letter in good_word:
            letter_find.remove(letter)
    if wrong_letter != []:
        wrong_letter = ", ".join(wrong_letter)
        print(f" The letters {wrong_letter} are wrong placed")
    if wrong_letter != []:
        wrong_letter = ", ".join(wrong_letter)
        print(f" The letters {wrong_letter} are wrong placed")

tries = 0
truc = tofind[0]

display(lenght)

old_answers = f" {truc}\n"

while tries <= 10:
    user_input = input(" Please enter a word : ")
    while len(user_input) != lenght:
        user_input = input(" Please enter a word : ")
    old_answers += " " + replace(user_input, tofind) + "\n"
    print(old_answers)
    letter(user_input, tofind)
    if user_input == tofind:
        print(" Well done ! You have find the right word ")
        break
    else:
        print(" Oops ! Wrong word")
    tries += 1
    if tries == 10:
        print(" the word was : ", tofind)