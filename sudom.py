"""
Code made by GUENASSIA Amandine, SABOT DRESSY Nathan and MAHAMAT Mastoura.

We didn't add the colors to be more accurate and more executable and understandable from every operating system and python editor. We executed Black but it didn't format anything. All the code is fully functionnal, the word to find is shown at the beginning, you can unshow it by putting the line #134 on commentary by adding "#". All functions have an help definition and a linéby line commentary. However a lot of things can be improve but it was the easiest way for us to do it.
"""


##########----- IMPORTS -----##########

# imports the random,unicodedata modules and the Path class from the pathlib module
import random, unicodedata
from pathlib import Path


##########----- FUNCTIONS -----##########


def display(lenght: int) -> None:

    """
    This function displays the first letter of the word to find, followed by underscores for the remaining letters of the word to find.

    Parameters:
        lenght(int)      : an integer representing the length of the word to find
    """

    global save

    # displays the first letter of the word
    print("", tofind[0], end="")
    # displays underscores for the rest of the letters
    for i in range(lenght - 1):

        print("_", end="")
        save += "_"

    # starts a new line
    print()


def replace(user_input: str, tofind: str) -> str:

    """
    This function replaces the underscores with the correctly placed letters entered by the user.

    Parameters:
        user_input(str)  : a string entered by the user
        tofind(str)      : a string representing the word to find

    Returns:
        save(str)        : a string representing the word with underscores replaced by correctly placed letters
    """

    global save

    save_list = []
    # creates a list of the current display of the word
    for letter in save:

        save_list.append(letter)

    # replaces underscores with correctly guessed letters
    for i in range(len(user_input)):

        if tofind[i] == user_input[i]:

            save_list[i] = tofind[i]

    save = "".join(save_list)
    return save


def letter(user_input: str, tofind: str) -> None:

    """
    This function checks if the letters entered by the user are correctly placed or not, and displays the incorrect placed letters.

    Parameters:
        user_input(str)  : a string entered by the user
        tofind(str)      : a string representing the word to find
    """

    # Initializes lists to store correct letters, incorrect letters, and letters that have been found
    good_word = []
    wrong_letter = []
    letter_find = []
    liste = zip((user_input), (tofind))

    # Populates the list of correct letters
    for letter in tofind:

        good_word.append(letter)

    # Finds the letters that match and removes them from the list of correct letters
    for element in liste:

        if element[0] == element[1]:

            letter_find.append(element[0])
            good_word.remove(element[0])

    # Checks for incorrect letters
    for letter in user_input:

        if letter in good_word and letter not in letter_find:

            wrong_letter.append(letter)
            good_word.remove(letter)

        elif letter in good_word:

            letter_find.remove(letter)

    # Prints a message if there are incorrect letters
    if wrong_letter != []:

        wrong_letter = ", ".join(wrong_letter)
        print(f" The letters {wrong_letter} are wrong placed")


##########----- MAIN CODE -----##########

# reads the contents of the file "fr.txt" and splits it into a list of words
dictionary = Path("fr.txt").read_text(encoding="utf-8").split("\n")

# selects a word randomly from the list of words
tofind = random.choice(dictionary)
# normalizes the selected word using NFD normalization form and removes non-ASCII characters
tofind = unicodedata.normalize("NFD", tofind).encode("ascii", "ignore").decode("ascii")

# stores the length of the selected word
lenght = len(tofind)
# displays the selected word and its length
print("", tofind, "\n", "Length of the word  : ", len(tofind))

# initialize the number of tries to 0
tries = 0

# initialize the word displayed to the first letter of the word to find
save = tofind[0]

# call the display function to display the first letter of the word to find and underscores for the rest
display(lenght)

# create a string to store all previous answers and add the first letter of the word to find
old_answers = f" {save}\n"

# while the number of tries is less than or equal to 10
while tries <= 10:

    # prompt the user to enter a word
    user_input = input(" Please enter a word : ")

    # check if the length of the user's input is equal to the length of the word to find
    while len(user_input) != lenght:

        # if not, prompt the user to enter a word again
        user_input = input(" Please enter a word : ")

    # update the old_answers string with the latest answer by calling the replace function and adding a newline character
    old_answers += " " + replace(user_input, tofind) + "\n"
    print(old_answers)

    # call the letter function to compare the user's input with the word to find and print the results
    letter(user_input, tofind)

    # check if the user's input is equal to the word to find
    if user_input == tofind:

        # if yes, print a message indicating the user has found the right word
        print(" Well done ! You have find the right word ")
        break

    else:

        # if not, print a message indicating the user has entered the wrong word
        print(" Oops ! Wrong word")

    # increment the number of tries
    tries += 1

    # if the number of tries is equal to 10, print the word to find
    if tries == 10:

        print(" the word was : ", tofind)
