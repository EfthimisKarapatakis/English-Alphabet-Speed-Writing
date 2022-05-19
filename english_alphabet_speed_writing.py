import tkinter as tk
from string import ascii_lowercase as letters

alphabet_index = 0
won = False


root = tk.Tk()

root.config(bg='red')
root.geometry('700x450')

root.wm_title('alphabet game')

def on_key_press(event):
    global alphabet_index, won
    
    if label['text'] == 0 or won:
        return
    
    if alphabet_index == len(letters):
        won = True
        print("You won!")
        return
    
    keypressed = event.char.lower()
    if keypressed == letters[alphabet_index]:
        alphabet_index += 1

        print(letters[:alphabet_index])


def countdown(count):
    label['text'] = count
    
    if count == 0 :
        print('You lose :( ')
        return
    
    if not won and count > 0:
        root.after(1000, countdown, count-1)
    

label = tk.Label(root)
label.place(x=100, y=0)
countdown(20)

root.bind('<Key>', on_key_press)
textlabel = tk.Label(root, text='how fast can you write the alphabet?', bg='red')
textlabel.pack(side=tk.TOP)

root.mainloop()

