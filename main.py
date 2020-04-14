import random
from tkinter import *

MAX_LENGTH = 20

##UI class
class Window():
    def __init__(self):
        self.m = Tk()
        self.m.geometry("500x500")
        self.m.resizable = (False, False)
        self.output = Label(self.m)
        self.m.title("Password Generator")

    ##builds all widgets and adds them to the window
    def pack(self):
        def slider_handler(self, param):
            global win
            ##if the specific characters are higher than the length, raise the length to minimum valid value
            if(win.numbers.get() + win.specials.get() > win.length.get()):
                if param == "length":
                    win.length.set(win.numbers.get() + win.specials.get())
                if param == "numbers":
                    win.numbers.set(win.length.get() - win.specials.get())
                if param == "specials":
                    win.specials.set(win.length.get() - win.numbers.get())

        ##title
        title = "Password Generator"
        self.title = Message(self.m, text=title, width=400, font=("Helvitica", 24), justify=CENTER)
        self.title.grid(row=0,column=0, pady=(20,10), columnspan=3)

        ##info text
        info = "Enter the desired length of your password and the amount of numerical/special characters it should contain, then click Get Password."
        self.info = Message(self.m, text=info, width=300, justify=CENTER)
        self.info.grid(row=1, column=0, pady=(10,30), columnspan=3)

        ##sliders and labels
        self.length_label = Label(self.m, text="Length")
        self.length = Scale(self.m, from_=6, to_=MAX_LENGTH, orient=HORIZONTAL, command=lambda x: slider_handler(self, "length"))

        self.numbers_label = Label(self.m, text="Numbers")
        self.numbers = Scale(self.m, from_=0, to_=20, orient=HORIZONTAL, command=lambda x: slider_handler(self, "numbers"))

        self.specials_label = Label(self.m, text="Special Characters")
        self.specials = Scale(self.m, from_=0, to_=20, orient=HORIZONTAL, command=lambda x: slider_handler(self, "specials"))

        ##button
        self.button = Button(self.m, text="Get Password", command=self.password)

        ##grid layout of elements
        self.length_label.grid(row=2, column=0, ipadx = 30)
        self.numbers_label.grid(row=2, column=1, ipadx = 30)
        self.specials_label.grid(row=2, column=2, ipadx = 30)
        self.length.grid(row=3, column=0, ipadx = 30, sticky=E)
        self.numbers.grid(row=3, column=1, ipadx = 30)
        self.specials.grid(row=3, column=2, ipadx = 30, sticky=W)
        self.button.grid(row=4,column=1, ipadx = 30, pady=30)

    #called when user clicks the Get Password button
    def password(self):
        def copy_to_clipboard(self):
            global win
            win.m.clipboard_clear()
            win.m.clipboard_append(win.output['text'])
            win.copied = Label(win.m, text="Copied to clipboard", font=("Helvitica", 10, "italic"))
            win.copied.grid(row=6, column=1, pady=0)
            win.copied.after(2000, win.copied.destroy)

        ##create new password output box
        self.output.destroy()
        self.password = create_password(self.length.get(), self.numbers.get(), self.specials.get())
        self.output = Label(self.m, text=self.password, borderwidth=2, relief="groove", padx =20, pady=10, font=("Helvitica, 24"))
        self.output.bind("<Button-1>", copy_to_clipboard)
        self.output.grid(row=5, column=0, columnspan=3)

    ##called to build the window and control the main loop
    def run(self):
        self.pack()
        self.m.mainloop()

##password-generating function
def create_password(length, amount_numbers, amount_specials):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    specials = ['!','@', '#', '$', '%', '^', '&', '*', '?']
    password = ""
    characters = []

    ##get letters
    for i in range(0, length - amount_numbers - amount_specials):
        if random.randint(0,1) == 1:
            characters.append(random.choice(letters).upper())
        else:
            characters.append(random.choice(letters))

    ##get numbers
    for i in range(0, amount_numbers):
        characters.append(str(random.randint(0,9)))

    ##get special chars
    for i in range(0, amount_specials):
        characters.append(random.choice(specials))

    ##build password string
    while(len(characters) > 0):
        next = random.choice(characters)
        password += next
        characters.remove(next)

    return(password)

win = Window()
win.run()