
import customtkinter as ct
import math
import threading

# creating a window
app = ct.CTk()

# the window title
app.title("Le Calculator")

# making the window unresizable
app.resizable(False,False)

# the standard window of the calculator
def standard():

    # the appearance function of the window
    def appearance(choice):
        ct.set_appearance_mode(choice)
        appmode.set('Mode')
        
    # a function to erase all the current and previous inputs
    def clear():
        buttoneq.configure(state='normal')
        display1.configure(state='normal')
        display1.delete(0, "end")
        display2.configure(state="normal")
        display2.delete(0, "end")
        display2.configure(state="disable")
    
    # a function to clear the inputs in the first entry box
    def erase():
        display1.delete(0, 'end')

    # the operation function
    def operation(op):
        # this function adds up the equation into a sinfle variable
        display1.configure(state='normal')
        display2.configure(state="normal")
        check2 = display2.get()  
        entries = display1.get()
        display1.delete(0, "end")
        if (('=' in check2) == True):
            display2.delete(0, 'end')
        entries = entries + op
        display2.insert('end',entries)
        display2.configure(state='disable')
      
    # the calcuation funtions   
    def equalize():
        try:
            entries = display1.get()
            display1.delete(0, 'end')
            display2.configure(state='normal')
            display2.insert('end',entries)
            entries = display2.get()
            answer = eval(entries)
            display1.insert('end',answer)
            display2.delete(0, 'end')
            display2.insert('end', (f'{entries} = {answer}'))
            display2.configure(state='disable')

        except ZeroDivisionError:
            display1.insert('end', "Cannot divide by zero!")
 
    def trigonometric(trig):
        num = display1.get()
        num = float(num)
        degrad = degrad_var.get()
        
        def deg_to_rad(num):    
            if degrad == 'degree':
                num = math.radians(num)
            else:
                num = num
            return num
            
        angle_radians = deg_to_rad(num)
        
        def trigs_cal():
            if trig == 'sin':
                result = round((math.sin(angle_radians)), 4)
            if trig == 'cos':
                result = round((math.cos(angle_radians)), 4)
            if trig == 'tan':
                result = round((math.tan(angle_radians)), 4)
            if trig == 'arcsin':
                result = round((math.asin(angle_radians)), 4)
            if trig == 'arccos':
                result = round((math.asin(angle_radians)), 4)
            if trig == 'arctan':
                result = round((math.atan(angle_radians)), 4)
            return result
        
        result = trigs_cal()

        eq = (f'{trig}({num}) = {result}')
        display1.delete(0,'end')
        display1.insert('end', result)
        display2.configure(state='normal')
        display2.delete(0, 'end')
        display2.insert('end', eq)
        display2.configure(state='disable') 
        b_trig.set('trig')       
        
    def multiop(choice):
        b_psr.set("  % : √ : x²")
        
        if (choice == "x²"):
            num = display1.get()
            display1.delete(0, 'end')
            display1.insert('end', eval(f'{num}**2'))
        if (choice == "√"):
            num = display1.get()
            display1.delete(0, 'end')
            display1.insert('end', eval(f'{num}**0.5'))
        if (choice == "%"):
            num = display1.get()
            display1.delete(0, 'end')
            display1.insert('end', eval(f'{num}*100'))
    
    def plus_min():
        num = display1.get()
        display1.delete(0, 'end')
        display1.insert('end', eval(f'{num}*-1'))
    
    # this fuction destroys everything in the window and opens up the programmer window of the calculator   
    def to_programmer():
        for widget in app.winfo_children():
            widget.destroy()
        t = threading.Thread(target=programmer)
        t.start()
            
       
    # the function to enter the button values as buttons are clicked  
    def button_click(button_number):
        # the inputs will be added at the end inside the first entry box
        display1.insert('end', button_number)

    # creating a frame to store all the objects for the standard window
    standardframe = ct.CTkFrame(master=app)
    standardframe.pack()

    # the calculator title
    title = ct.CTkLabel(standardframe, text="  B & E Calc.", font=('goudy old style', 45))
    title.grid(pady=20, columnspan=2, sticky="w")
    
    # the menu option for the window appearance
    appmode = ct.CTkOptionMenu(master=standardframe,
                                        values=["light", "dark"],
                                        command=appearance)
    appmode.grid(padx=2, pady=2, row=0, column=2)
    appmode.set("Mode")
    
    # the standard window title 
    title1 = ct.CTkLabel(master=standardframe, text="  Standard", font=('goudy old style', 25))
    title1.grid(row=1, column=0, sticky='w')

    # a button to switch to programmer mode of the calculator
    bconvert = ct.CTkButton(master=standardframe, text="</>", font=("times new roman",20), command=to_programmer, fg_color="dimgray")
    bconvert.grid(row=1, column=2, ipadx=1, pady=1, padx=2,)
    
    # the first entry and display box
    display1 = ct.CTkEntry(standardframe, font=("times", 25))
    display1.grid(row=2, column=0, columnspan=2, padx=2, pady=2, sticky="nsew", rowspan=2)
    display1.configure(state="normal")

    # the second entry and display box
    display2 = ct.CTkEntry(standardframe, width=250)
    display2.grid(row=4, column=0, columnspan=2, padx=2, pady=2, sticky="nsew", rowspan=1)
    display2.configure(state="normal")
    
    # the delete botton#
    buttondel = ct.CTkButton(standardframe, text="←", font=("times new roman",20), command=erase, fg_color="peru")
    buttondel.grid(row=2, column=2, ipadx=1, pady=1, padx=2, sticky="ns")
    
    # the "+" operation button
    buttonadd = ct.CTkButton(standardframe, text="+", font=("times new roman",20), fg_color="teal", command=lambda: operation('+'))
    buttonadd.grid(row=3, column=2, ipadx=1, pady=1, padx=2, sticky="nsew")

    # the "-" operation button
    buttonsub = ct.CTkButton(standardframe, text="−", font=("times new roman",20), fg_color="teal", command=lambda: operation('-'))
    buttonsub.grid(row=4, column=2, ipadx=1, pady=1, padx=2, sticky="nsew")

    # the '*' operation button
    buttonmult = ct.CTkButton(standardframe, text="×", font=("times new roman",20), fg_color="teal", command=lambda: operation('*'))
    buttonmult.grid(row=5, column=2, ipadx=1, pady=1, padx=2, sticky="nsew")

    # the '/' operation button
    buttondiv = ct.CTkButton(standardframe, text="÷", font=("times new roman",20), fg_color="teal", command=lambda: operation('/'))
    buttondiv.grid(row=6, column=2, ipadx=1, pady=1, padx=2, sticky="nsew")
    
    # the '%' operation button
    psr_var = ct.StringVar()
    b_psr = ct.CTkOptionMenu(standardframe, values=['%', "√", "x²"], 
                             command=multiop,
                             font=("times new roman",20), fg_color="peru",)
    b_psr.grid(row=5, column=0, ipadx=1, pady=1, padx=2, sticky="nsew")
    b_psr.set("  % : √ : x²")

    # the square operation button
    b_pm = ct.CTkButton(standardframe, text="±", font=("times new roman",20), fg_color="peru", command=plus_min)
    b_pm.grid(row=6, column=0, ipadx=1, pady=1, padx=2, sticky="nsew")

    # the squareroot operation button
    trig_var = ct.StringVar()
    b_trig = ct.CTkOptionMenu(standardframe, values=['sin', "cos", "tan", "arcsin", "arccos", "arctan"], 
                              font=("times new roman",20), fg_color="peru", variable=trig_var, command=trigonometric)
    b_trig.grid(row=5, column=1, ipadx=1, pady=1, padx=2, sticky="nsew")
    b_trig.set("trig")

    # the plus/minus operation button
    degrad_var = ct.StringVar()
    b_deg_rad = ct.CTkOptionMenu(standardframe, values=['degree', 'radians'], font=("times new roman",18), 
                                 fg_color="peru", variable=degrad_var)
    b_deg_rad.grid(row=6, column=1, ipadx=1, pady=1, padx=2, sticky="nsew")
    b_deg_rad.set("degree")

    # Create a list of button labels and commands
    button_info = [
        {"label": "7", "command": lambda: button_click(7)},
        {"label": "8", "command": lambda: button_click(8)},
        {"label": "9", "command": lambda: button_click(9)},
        {"label": "4", "command": lambda: button_click(4)},
        {"label": "5", "command": lambda: button_click(5)},
        {"label": "6", "command": lambda: button_click(6)},
        {"label": "1", "command": lambda: button_click(1)},
        {"label": "2", "command": lambda: button_click(2)},
        {"label": "3", "command": lambda: button_click(3)},
        {"label": ".", "command": lambda: button_click('.')},
    ]

    # Create and display multiple buttons using grid system
    for i, info in enumerate(button_info):
        button = ct.CTkButton(standardframe, text=info["label"], command=info["command"])
        button.grid(row=(i+24) // 3, column=i % 3, padx=2, pady=2)
    
    # the zero button
    buttonzero = ct.CTkButton(standardframe, text="0", command= lambda: button_click(0))
    buttonzero.grid(row=11, column=1, columnspan=2, sticky="ew", pady=2, padx=2)

    # the calculation command button
    buttoneq = ct.CTkButton(standardframe, text="=", font=("times", 20, "bold"), fg_color="dimgray", command=equalize)
    buttoneq.grid(row=12, column=2, ipadx=1, pady=1, padx=2, sticky="ns", rowspan=2)

    # the clearing button
    b_clear = ct.CTkButton(master=standardframe, text="C", font=('goudy old style', 20, 'bold'), fg_color="darkred", command=clear)
    b_clear.grid(row=12, column=0, pady=2, padx=2, columnspan=2, sticky="ew")



# programmer window of the calculator
def programmer():
    
    # changing the gui appearance 
    def appearance(choice):
        ct.set_appearance_mode(choice)
        appmode.set('Mode')

    # function to return the the standard window of the calculator
    def to_standard():
        for widget in app.winfo_children():
            widget.destroy()
           
        t = threading.Thread(target=standard)
        t.start()
 
    def clear():
        display1.configure(state='normal')
        display1.delete(0, "end")
        display2.configure(state="normal")
        display2.delete(0, "end")
        display2.configure(state='disable')
 
    def conversion():
        display2.configure(state='normal')
        display2.delete(0, 'end')
        conop1 = val_conop1.get()
        conop2 = val_conop2.get()
        number = display1.get()
        
        try:
            # conversion from Decimal to Hexadecimal
            if (conop1 == "Dec") and (conop2 == "Hex"):
                decimal_number = int(number)
                hexadecimal_number = hex(decimal_number)[2:]
                hexadecimal_number = hexadecimal_number.upper()
                display2.insert('end', hexadecimal_number)
                
            # conversion from Decimal to Binary
            if (conop1 == "Dec") and (conop2 == "Bin"):
                decimo_number = int(number)
                binary_number = bin(decimo_number)[2:]
                display2.insert('end', binary_number)
                
            # conversion from Binary to Deciaml
            if (conop1 == "Bin") and (conop2 == "Dec"):
                decimal_output = int(number, 2)
                display2.insert('end', decimal_output)
        
            # conversion from Binary to Hexadecimal
            if (conop1 == "Bin") and (conop2 == "Hex"):
                decimal_number = int(number, 2)
                hexadecimal_number = hex(decimal_number)
                hex_number = hexadecimal_number[2:].upper()
                display2.insert('end', hex_number)
            
            # conversion from Hexadecimal to Binary
            if (conop1 == "Hex") and (conop2 == "Bin"):
                def hex_to_binary(hex_num):
                    # Convert hexadecimal to decimal
                    decimal_num = int(hex_num, 16)

                    # Convert decimal to binary
                    binary_num = bin(decimal_num)[2:]

                    return binary_num

                hexadecimal = number
                binary = hex_to_binary(hexadecimal)
                display2.insert("end", binary)
                
            # conversion from Hexadecimal to Decimal
            if (conop1 == "Hex") and (conop2 == "Dec"):
                hexadecimal_number = number
                decimal_number = int(hexadecimal_number, 16)
                display2.insert('end', decimal_number)
                
            # conversion from Octal to Decimal
            if (conop1 == "Oct") and (conop2 == "Dec"):
                decimal_number = int(number, 8)
                display2.insert("end", decimal_number)
            
            # conversion from Octal to Hex
            if (conop1 == "Oct") and (conop2 == "Hex"):
                decimal_number = int(number, 8)
                hexadecimal_number = hex(decimal_number)[2:]
                display2.insert("end", (hexadecimal_number.upper()))
            
            # conversion from Octal to Binary
            if (conop1 == "Oct") and (conop2 == "Bin"):
                decimal_number = int(number, 8)
                binary_output = bin(decimal_number)[2:]

                display2.insert("end", binary_output)
            
            # conversion from Decimal to Octal
            if (conop1 == "Dec") and (conop2 == "Oct"):
                decimal = int(number)
                
                # Convert decimal to octal using the built-in oct() function
                octal = oct(decimal)[2:]

                display2.insert("end", octal)
            
            # conversion from Binary to Octal
            if (conop1 == "Bin") and (conop2 == "Oct"):
                def binary_to_octal(binary):
                    # Remove any leading zeros
                    binary = binary.lstrip("0")

                    # Pad the binary number with zeros to make the length a multiple of 3
                    while len(binary) % 3 != 0:
                        binary = "0" + binary

                    octal = ""
                    # Convert the binary number to octal
                    for i in range(0, len(binary), 3):
                        # Take three digits at a time and convert them to octal
                        digits = binary[i:i+3]
                        decimal = int(digits, 2)
                        octal += str(decimal)

                    return octal

                binary_number = number
                octal_number = binary_to_octal(binary_number)
                display2.insert("end", octal_number)
            
            # conversion from Hexadecimal to Octal
            if (conop1 == "Hex") and (conop2 == "Oct"):
                def hex_to_oct(hex_num):
                    # Convert hexadecimal to decimal
                    decimal_num = int(hex_num, 16)

                    # Convert decimal to octal
                    octal_num = oct(decimal_num)

                    # Remove '0o' prefix from octal number
                    octal_num = octal_num[2:]

                    return octal_num

                # Test the function
                hexadecimal = number
                octal = hex_to_oct(hexadecimal)
                display2.insert("end", octal)
                
            # conversion from same format to the same format
            if conop1 == conop2:
                display2.insert('end', number)
        
        except:
            display2.insert('end', 'Invalid Input!')
        
        display2.configure(state='disable')  
    
    def opchange1(op):
        display1.delete(0, 'end')
        display2.configure(state='normal')
        display2.delete(0, 'end')
        display2.configure(state='disable')
    
    def opchange2(op):
        display2.configure(state='normal')
        display2.delete(0, 'end')
        display2.configure(state='disable')


    
    # creating a frame to hold the items/objects in the programmer window
    frame=ct.CTkFrame(master=app)
    frame.pack(side="top", expand=True, fill="both")
    
    # the calculator title
    title = ct.CTkLabel(frame, text="  B & E Calc.", font=('goudy old style', 45))
    title.grid(row=0, column=0, pady=20, columnspan=2, sticky="w")
    
    # the option menu for the gui appearance
    appmode = ct.CTkOptionMenu(master=frame,
                                        values=["light", "dark"],
                                        command=appearance)
    appmode.grid(row=0, column=2, padx=2, pady=2, sticky="e")
    appmode.set("Mode")
    
    # the title of the window (programmer window)   
    title1 = ct.CTkLabel(master=frame, text="Programmer", font=('goudy old style', 25))
    title1.grid(row=1, column=0)
    
    # the button to switch to the standard window of the calculator
    bconvert = ct.CTkButton(master=frame, text="STRD", font=("times new roman",14), command=to_standard, fg_color="dimgray")
    bconvert.grid(row=1, column=2, ipadx=1, pady=1, padx=2,)
    
    # the first entry and display box
    display1 = ct.CTkEntry(frame, width=250, font=('times', 25))
    display1.grid(row=2, column=0, columnspan=2, pady=2, sticky="nsew", rowspan=2)
    
    # the second entry and display box
    display2 = ct.CTkEntry(frame)
    display2.grid(row=4, columnspan=2, sticky="nsew", pady=2)
    
    # the first option menu to select the number type
    val_conop1 = ct.StringVar()
    conop1 = ct.CTkOptionMenu(master=frame, variable=val_conop1, 
                              values=["Bin", "Hex", "Dec", "Oct"],
                              command=opchange1)
    conop1.grid(row=3, column=2, padx=2, pady=2, sticky="e")
    conop1.set("Bin")
    
    # the second option menu to select the number output
    val_conop2 = ct.StringVar()
    conop2 = ct.CTkOptionMenu(master=frame, variable=val_conop2, 
                              values=["Bin", "Hex", "Dec", "Oct"],
                              command=opchange2)
    conop2.grid(row=4, column=2, padx=2, pady=2, sticky="e")
    conop2.set("Dec")
    
    # the delete button on the side to clear the entry box
    buttondel = ct.CTkButton(master=frame, text="C", font=("times new roman",20), fg_color="darkred", command=clear)
    buttondel.grid(row=2, column=2, padx=2, pady=2, sticky="e")

    # the equal button to run the convertions 
    buttoneq = ct.CTkButton(frame, text="=", font=("times new roman",20), fg_color="grey", command=conversion)
    buttoneq.grid(row=10, column=1, pady=2, padx=2, sticky="nsew", columnspan=2)

    # a function to enter the pressed buttons into the entry box
    def button_click(button_number):
        # inputs going into the first entry box
        display1.insert("end",button_number)


    # Create a list of button labels and commands
    button_info = [
        {"label": "F", "command": lambda: button_click('F')},
        {"label": "9", "command": lambda: button_click(9)},
        {"label": "8", "command": lambda: button_click(8)},
        {"label": "E", "command": lambda: button_click('E')},
        {"label": "7", "command": lambda: button_click(7)},
        {"label": "6", "command": lambda: button_click(6)},
        {"label": "D", "command": lambda: button_click('D')},
        {"label": "5", "command": lambda: button_click(5)},
        {"label": "4", "command": lambda: button_click(4)},
        {"label": "C", "command": lambda: button_click('C')},  
        {"label": "3", "command": lambda: button_click(3)},
        {"label": "2", "command": lambda: button_click(2)},
        {"label": "B", "command": lambda: button_click('B')},
        {"label": "1", "command": lambda: button_click(1)},
        {"label": "0", "command": lambda: button_click(0)},
        {"label": "A", "command": lambda: button_click('A')},
    ]

    # Create and display multiple buttons using grid system
    for i, info in enumerate(button_info):
        button = ct.CTkButton(frame, text=info["label"], fg_color="teal", command=info["command"])
        button.grid(row=(i+15) // 3, column=i % 3, padx=2, pady=2)
        # Grid.rowconfigure(0, weight=1)


# function to map keyboard events (the physical keyboard)
def key_press(event):
        key_mappings = {
            "9": 9,
            "8": 8,
            "7": 7,
            "6": 6,
            "5": 5,
            "4": 4,
            "3": 3,
            "2": 2,
            "1": 1,
            "0": 0,
            ".": "."
        }
        
        key = event.keysym
        if key in key_mappings:
            button_click(key_mappings[key])


# Bind keyboard events to the root window
app.bind("<Key>", key_press)

# running the standard window of the calculator
standard()

app.mainloop()
