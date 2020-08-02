from words import word_list
from tkinter import tk
import random
'''Zach Millsap | zwmillsap@dmacc.edu | 7/29/2020'''
'''Purpose of this program is to take user guesses in a game of hangman;using a GUI to play.'''

window = tk()
window.title("Hangman")

'''Images to input into the gui to show progression of game.'''
stages = [PhotoImage(file="images/hang0.png"), PhotoImage(file="images/hang1.png"), PhotoImage(file="images/hang2.png"),
          PhotoImage(file="images/hang3.png"), PhotoImage(file="images/hang4.png"), PhotoImage(file="images/hang5.png"),
          PhotoImage(file="images/hang6.png")]

'''Main game function'''
def game():
    global secret_word_blank_spaces         #placeholder
    global numberOfGuesses          #number of guesses
    numberOfGuesses = 0         #numberOfGuesses placeholder/starts at 0
    imgLabel.congfig(image = stages[0])
    secret_word = random.choice(word_list)
    secret_word_blank_spaces = "_".join(secret_word)
    lblWord.set(" ".join(" " * len(secret_word)))



imgLabel = Label(window)
imgLabel.grid(row=0, column= 0, columnspan=3, padx = 10, pady = 40)
imgLabel.config(image = stages[0])

lblWord=StringVar()
label (Window, textvariable = lblWord, font=("Comic Sans 30 bold")).grid(row=0, column=0, columnspan=3, padx=10, pady=40)


