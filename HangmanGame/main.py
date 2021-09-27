import tkinter as tk
import random


def read_random_word_from_file(wordFile):
    file=open(wordFile,'r')
    lines =file.readlines()
    rand_number = random.randint(1,len(lines))
    count=0
    for line in lines:
        count+=1
        if count == rand_number:
            return line

def gameplay():
    attempt_count = 0
    secret_word = read_random_word_from_file("words")
    print(secret_word)

    attempt_word = input("pogodite riječ ")





if __name__ == '__main__':
    # root = tk.Tk()
    # root.geometry("600x600")

    gameplay()



    # root.mainloop()

