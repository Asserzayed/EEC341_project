from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Checkbutton, IntVar, StringVar, Tk, Canvas, Entry, Text, Button, PhotoImage,ttk
import random
import string
from tkinter.constants import FLAT
from datetime import datetime

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.title("Random Password Generator By Asser Mohamed Atef Zayed")
window.geometry("700x445")
window.configure(bg = "#FFFFFF")


# callback functions

def save_text():
   now=datetime.now()
   current_time = now.strftime("%H:%M:%S")+".txt"
   text_file = open(current_time, "w")
   text_file.write(disp_tf.get(1.0, 'end'))
   text_file.close()

def clearFn():
    save_text()
    disp_tf.config(state='normal')
    disp_tf.delete(1.0, 'end')
    disp_tf.config(state='disabled')
    

def generatePass():
    #Allows editing to the textbox
    disp_tf.config(state='normal')
    #Getting input
    choice = myCombo.get()
    password_length_val = password_length.get()
    if(choice=="All lowercase letters"):
        letters = string.ascii_lowercase
    elif(choice=="All uppercase letters"):
        letters = string.ascii_uppercase
    elif(choice=="Contains all letters"):
        letters = string.ascii_letters
    elif(choice=="Numbers only"):
        letters = string.digits
    elif(choice=="Symbols only"):
        letters = string.punctuation

    if(numbers_char.get()==1 and choice != "Numbers only"):
        letters+= string.digits
    if(symbols_char.get()==1 and choice != "Symbols only"):
        letters+= string.punctuation
    
    if(non_repeating.get()==1): 
            result_str = ''.join(random.sample(letters,int(password_length_val)))+"\n"
    else:
        result_str = ''.join(random.choice(letters) for i in range(int(password_length_val)))+"\n"
    disp_tf.insert(1.0,result_str)
    disp_tf.config(state='disabled')

#Combobox options
options=[
    "All lowercase letters",
    "All uppercase letters",
    "Contains all letters",
    "Numbers only",
    "Symbols only"
    ]



#TKINTER DESIGNER CODE

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 445,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    700.0,
    445.0,
    fill="#4D4AE2",
    outline="")

canvas.create_rectangle(
    350.0,
    0.0,
    700.0,
    445.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    27.0,
    27.0,
    anchor="nw",
    text="Please enter the length of the password",
    fill="#FFFFFF",
    font=("Nunito ExtraBold", 15 * -1)
)

canvas.create_text(
    27.0,
    44.0,
    anchor="nw",
    text="desired below",
    fill="#FFFFFF",
    font=("Nunito ExtraBold", 15 * -1)
)

canvas.create_rectangle(
    27.0,
    71.0,
    106.0,
    77.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    380.0,
    50.0,
    459.0,
    56.0,
    fill="#4D4AE2",
    outline="")

canvas.create_rectangle(
    27.0,
    175.0,
    106.0,
    181.0,
    fill="#FFFFFF",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    62.5,
    112.5,
    image=entry_image_1
)
password_length=StringVar()
entry_1 = Entry(
    bd=0,
    bg="#EBEBEB",
    highlightthickness=0,
    textvariable=password_length
)
entry_1.place(
    x=39.5,
    y=101.0,
    width=46.0,
    height=23.0
)

#Combobox styling
style = ttk.Style()

style.map('TCombobox', fieldbackground=[('readonly','#EBEBEB')])
style.map('TCombobox', selectbackground=[('readonly', '#EBEBEB')])
style.map('TCombobox', selectforeground=[('readonly', '#000000')])

combo_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
combo_bg_2 = canvas.create_image(
    151.0,
    217,
    image=combo_image_2
)
#Combobox options
myCombo = ttk.Combobox(
    window, value=options)
myCombo.current(0)
myCombo.bind(
    "<<ComboboxSelected>>",)
myCombo.place(
    x=39.5,
    y=205.5,
    width=223.0,
    height=23.0
)
#To not type into the combobox
myCombo['state'] = 'readonly'

#Checkboxes
non_repeating = IntVar()
numbers_char = IntVar()
symbols_char = IntVar()

check1 = Checkbutton(window, text="Non reapeating characters",variable=non_repeating,activebackground="#4D4AE2",activeforeground="#000000",bg="#4D4AE2",font=(("Nunito ExtraBold", 12 * -1)),fg="white",selectcolor="#4A4A4A")
check1.place(
    x=39.5,
    y=240
)
check2 = Checkbutton(window, text="+Numbers",variable=numbers_char,activebackground="#4D4AE2",activeforeground="#000000",bg="#4D4AE2",font=(("Nunito ExtraBold", 12 * -1)),fg="white",selectcolor="#4A4A4A")
check2.place(
    x=39.5,
    y=270
)
check3 = Checkbutton(window, text="+Symbols",variable=symbols_char,activebackground="#4D4AE2",activeforeground="#000000",bg="#4D4AE2",font=(("Nunito ExtraBold", 12 * -1)),fg="white",selectcolor="#4A4A4A")
check3.place(
    x=39.5,
    y=300
)
#Generate button
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=generatePass,
    relief="flat"
)
button_1.place(
    x=73.0,
    y=402.0,
    width=202.0,
    height=23
)
#Clear button
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=clearFn,
    relief="flat"
)
button_2.place(
    x=135.0,
    y=360.0,
    width=78.0,
    height=23
)

canvas.create_text(
    27.0,
    150.0,
    anchor="nw",
    text="Choose you password constraints",
    fill="#FFFFFF",
    font=("Nunito ExtraBold", 15 * -1)
)

canvas.create_text(
    380.0,
    22.0,
    anchor="nw",
    text="Your generated passwords",
    fill="#000000",
    font=("Nunito ExtraBold", 15 * -1)
)
canvas.create_rectangle(
    380.0,
    71.0,
    674.0,
    425.0,
    fill="#CECECE",
    outline="")

#Output window // Textbox
disp_tf = Text(
    window,
    height=354,
    width=294,
    bg="#CECECE",
    font=(("Nunito ExtraBold", 15 * -1))
)
#Textbox position
disp_tf.place(
    x=380,
    y=71.0,
    width=294.0,
    height=335.0
)

#Allow copying
disp_tf.ReadOnly = True
#Disclaimer
disclaimer = "'Clear' also saves your passwords!\n"
disp_tf.insert('end',disclaimer)
disp_tf.config(state='disabled')

canvas.create_text(
    615.0,
    407.0,
    anchor="nw",
    text="Asser Z.",
    fill="#000000",
    font=("Nunito ExtraBold", 12 * -1)
)


window.resizable(False, False)
window.mainloop()
