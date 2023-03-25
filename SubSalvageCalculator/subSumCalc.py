import tkinter
import customtkinter
import re

customtkinter.set_appearance_mode("System")  # follow system prefs
customtkinter.set_default_color_theme("dark-blue")

# dictionary block
sn = "necklaces"
se = "earrings"
sb = "bracelets"
sr = "rings"

# vals block
esnv = 34500
esev = 30000
esbv = 28500
esrv = 27000

snv = 13000
sev = 10000
sbv = 9000
srv = 8000

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.resizable(False,False)  # forces resolution

app.title('Submarine Salvage Caclulator')
app.iconbitmap('icon.ico')
app.geometry("750x200")

def button_function():
    user_input = entry.get()  # retrieves input from entrybox
    trim_input(user_input)

def trim_input(user_input):
    # regex = "[\da]+ (?:Extravagant )?Salvaged (?:Ring|Bracelet|Necklace|Earring)"  # Cuts all non-salvaged goods from input

    regex = "[\da]+ (?:extravagant )??salvaged (?:rings|bracelets|necklaces|earrings)"
    sought_inputs = re.findall(regex, user_input)   

    stringcoverter = ""  # declares empty string to be filled with the salvaged goods
    count = 0
    for i in sought_inputs:
        count += 1  # iterator variable to circumvent initalizing with a space
        temp = str()
        temp += i
        
        if(temp.isdigit and count > 1):  # checks to see if there is a number, signaling a new item in the list. adds space for easy parsing
            stringcoverter += ' ' + i
        else:
            stringcoverter += i

    regex2 = ""
    removed_uni = re.sub(regex2, "", stringcoverter)

    regex3 ="\ "  # creates a list of strings, seperator = ' ' 
    cleaned_inputs = re.split(regex3, removed_uni)

    calculate_vals(cleaned_inputs)

def calculate_vals(cleaned_inputs):
    dum = 0 
    for i in range(len(cleaned_inputs)):
        if(cleaned_inputs[i].isdigit()):
            if(cleaned_inputs[i+1] == "salvaged"):
                if(cleaned_inputs[i+2] == sn):
                    dum += snv * int(cleaned_inputs[i])
                elif(cleaned_inputs[i+2] == se):
                    dum += sev * int(cleaned_inputs[i])
                elif(cleaned_inputs[i+2] == sb):
                    dum += sbv * int(cleaned_inputs[i])
                elif(cleaned_inputs[i+2] == sr):
                    dum += srv * int(cleaned_inputs[i])
            elif(cleaned_inputs[i+1] == "extravagant"):
                if(cleaned_inputs[i+3] == sn):
                    dum += esnv * int(cleaned_inputs[i])
                elif(cleaned_inputs[i+3] == se):
                    dum += esev * int(cleaned_inputs[i])
                elif(cleaned_inputs[i+3] == sb):
                    dum += esbv * int(cleaned_inputs[i])
                elif(cleaned_inputs[i+3] == sr):
                    dum += esrv * int(cleaned_inputs[i])
    # textbox.delete(0, any)
    textbox.insert("0.0", f"Total Gil: {dum:,}\n")
    # label.configure(text=f"Total Gil: {dum:,}")
    
# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="Calculate raw gil", command=button_function)
button.place(relx=0.74, rely=0.2, anchor=tkinter.CENTER)

entry = customtkinter.CTkEntry(master=app, placeholder_text="Paste chatlog here...", width = 350)
entry.place(relx=0.4, rely=0.2, anchor=tkinter.CENTER)

textbox = customtkinter.CTkTextbox(master=app, height=100, width = 500)
textbox.grid(row=0, column=0)
textbox.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

# label = customtkinter.CTkLabel(master=app, text="Total Gil:", width=500, anchor="w")
# label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

app.mainloop()