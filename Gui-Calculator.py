import customtkinter as ct

ct.set_appearance_mode("light")
ct.set_default_color_theme("blue")

root = ct.CTk()

root.geometry("335x460")
root.title("Calculator")

# driver function
def calculator():
    calculate = textbox.get('0.0', 'end')
    result = eval(calculate)
    textbox.delete('0.0', 'end')
    textbox.insert('0.0', result)

# Text box
textbox = ct.CTkTextbox(root, text_color="black", font=("Birch Std", 36), fg_color="#acacac", width=310, height=100, wrap='word')
textbox.place(x=10,y=13)

# Buttons
button = ct.CTkButton(root, text="7", height=70, width=70, font=("Helvetica", 30), hover_color="#005884", command= lambda:textbox.insert('end', 7))
button.place(x=10,y=130)
button = ct.CTkButton(root, text="8", height=70, width=70, font=("Helvetica", 30), hover_color="#005884", command= lambda:textbox.insert('end', 8))
button.place(x=90,y=130)
button = ct.CTkButton(root, text="9", height=70, width=70, font=("Helvetica", 30), hover_color="#005884", command= lambda:textbox.insert('end', 9))
button.place(x=170,y=130)
button = ct.CTkButton(root, text="/", height=70, width=70, font=("Helvetica", 30), hover_color="#005884", command= lambda:textbox.insert('end', '/'))
button.place(x=250,y=130)
button = ct.CTkButton(root, text="4", height=70, width=70, font=("Helvetica", 30), hover_color="#005884", command= lambda:textbox.insert('end', 4))
button.place(x=10,y=210)
button = ct.CTkButton(root, text="5", height=70, width=70, font=("Helvetica", 30), hover_color="#005884", command= lambda:textbox.insert('end', 5))
button.place(x=90,y=210)
button = ct.CTkButton(root, text="6", height=70, width=70, font=("Helvetica", 30), hover_color="#005884", command= lambda:textbox.insert('end', 6))
button.place(x=170,y=210)
button = ct.CTkButton(root, text="x", height=70, width=70, font=("Helvetica", 30), hover_color="#005884", command= lambda:textbox.insert('end', '*'))
button.place(x=250,y=210)
button = ct.CTkButton(root, text="1", height=70, width=70, font=("Helvetica", 30), hover_color="#005884", command= lambda:textbox.insert('end', 1))
button.place(x=10,y=290)
button = ct.CTkButton(root, text="2", height=70, width=70, font=("Helvetica", 30), hover_color="#005884", command= lambda:textbox.insert('end', 2))
button.place(x=90,y=290)
button = ct.CTkButton(root, text="3", height=70, width=70, font=("Helvetica", 30), hover_color="#005884", command= lambda:textbox.insert('end', 3))
button.place(x=170,y=290)
button = ct.CTkButton(root, text="-", height=70, width=70, font=("Helvetica", 30), hover_color="#005884", command= lambda:textbox.insert('end', '-'))
button.place(x=250,y=290)
button = ct.CTkButton(root, text="0", height=70, width=70, font=("Helvetica", 30), hover_color="#005884", command= lambda:textbox.insert('end', 0))
button.place(x=90,y=370)
button = ct.CTkButton(root, text="+", height=70, width=70, font=("Helvetica", 30), hover_color="#005884", command= lambda:textbox.insert('end', '+'))
button.place(x=250,y=370)
button = ct.CTkButton(root, text="C", height=70, width=70, font=("Helvetica", 30), hover_color="#005884", command= lambda:textbox.delete('0.0', 'end'))
button.place(x=170,y=370)
button = ct.CTkButton(root, text="=", height=70, width=70, font=("Helvetica", 30), hover_color="#02405e", fg_color='#005884', command = calculator)
button.place(x=10,y=370)


root.mainloop()