import customtkinter

def button_callback():
    print("button pressed")

def checkbox1():
    print("Checkbox 1 selected")

def checkbox2():
    print("Checkbox 2 selected")

app = customtkinter.CTk()
app.title("my app")
app.geometry("400x150")
app.grid_columnconfigure((0,1), weight=1) #makes the button centered


button = customtkinter.CTkButton(app, text="my button", command=button_callback)
button.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2) # makes the button span the full area 

checkbox_1 = customtkinter.CTkCheckBox(app, text="checkbox 1")
checkbox_1.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w", command=checkbox1)
checkbox_2 = customtkinter.CTkCheckBox(app, text="checkbox 2")
checkbox_2.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w",command=checkbox2)

app.mainloop()