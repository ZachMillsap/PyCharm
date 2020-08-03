from words import word_list
from string import ascii_uppercase
from tkinter import *
import random
'''Zach Millsap | zwmillsap@dmacc.edu | 7/29/2020'''
'''Purpose of this program is to take user guesses in a game of hangman;using a GUI to play.'''

window = Tk()
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
    imgLabel.config(image = stages[0])
    secret_word = random.choice(word_list)
    secret_word_blank_spaces = "_".join(secret_word)
    lblWord.set(" ".join(" " * len(secret_word)))

def guess(letter):
    global numberOfGuesses
    txt = list(word_list)
    guessed = list(lblWord.get())
    if secret_word_blank_spaces.count(letter)>0:
        for x in range(len(txt)):
            if txt[x] == letter:
                guessed[x] = letter
            lblWord.set(" ".join(guessed))
            if lblWord.get() == secret_word_blank_spaces:
                messagebox.showinfo("YOU GUESSED CORRECTLY!")
        else:
            numberOfGuesses += 1
            imgLabel.config(images = stages[numberOfGuesses])
            if numberOfGuesses == 6:
                messagebox.showinfo("GAME OVER!")

imgLabel = Label(window)
imgLabel.grid(row=0, column= 0, columnspan=3, padx = 10, pady = 40)
imgLabel.config(image = stages[0])

lblWord=StringVar()
Label(window, textvariable = lblWord, font=("Ariel 30 bold")).grid(row=0, column=3, columnspan=6, padx=10)

n = 0
for x in ascii_uppercase:
    Button(window, text = x, command = lambda x = x: guess(x), font = ("Ariel 20"), width = 4) .grid(row=1+n//9,
                                                                                                     column = n%9)
    n+=1

Button(window, text = "New Game", command = lambda:game(), font = ("Ariel 14 bold")).grid(row=3, column=8, sticky = "nesw")

game()
window.mainloop()
