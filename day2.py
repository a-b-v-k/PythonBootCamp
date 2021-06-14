from tkinter import*
window = Tk()
window.geometry('500x700')
window.title("Registration Form")

FN = StringVar()
LN = StringVar()
age = StringVar()
mob = StringVar()
add = StringVar()
wnum = StringVar()


label_0 = Label(window, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=20)


label_1 = Label(window, text="First Name",width=20,font=("bold", 10))
label_1.place(x=80,y=80)

entry_1 = Entry(window,textvariable = FN)
entry_1.place(x=240,y=80)

label_2 = Label(window, text="Last Name",width=20,font=("bold", 10))
label_2.place(x=80,y=130)

entry_2 = Entry(window, textvariable = LN)
entry_2.place(x=240,y=130)

label_3 = Label(window, text="Gender",width=20,font=("bold", 10))
label_3.place(x=80,y=180)

gendvar = IntVar()
Radiobutton(window, text="Male",padx = 5, variable=gendvar, value=1).place(x=235,y=180)
Radiobutton(window, text="Female",padx = 20, variable=gendvar, value=2).place(x=290,y=180)

label_4 = Label(window, text="Age:",width=20,font=("bold", 10))
label_4.place(x=80,y=230)

entry_4 = Entry(window, textvariable = age)
entry_4.place(x=240,y=230)

label_5 = Label(window, text="Mobile", width=20, font=('bold', 10))
label_5.place(x=80, y=280)

entry_5 = Entry(window, textvariable = mob)
entry_5.place(x=240, y=280)

label_6 = Label(window, text='Country', width=20, font=('bold', 10))
label_6.place(x=80, y=330)

countries = ['India' ,'US' , 'UK' ,'Germany' ,'Austria']
c = StringVar()
drop_down = OptionMenu(window, c, *countries)
c.set('Select your country')
drop_down.place(x=240, y=330)

label_7 = Label(window, text='Language', width=20, font=('bold', 10))
label_7.place(x=80, y=380)

var1 = IntVar()
var2 = IntVar()
Checkbutton(window, text='English', variable = var1).place(x=235, y=380)
Checkbutton(window, text='Hindi', variable = var2).place(x=310, y=380)

label_8 = Label(window, text='Address', width=20, font=('bold', 10))
label_8.place(x=80, y=430)

entry_8 = Entry(window, textvariable = add)
entry_8.place(x=240, y=430)

label_9 = Label(window, text='Whatsapp number', width=20, font=('bold', 10))
label_9.place(x=80, y=480)

entry_9 = Entry(window, textvariable = wnum)
entry_9.place(x=240, y=480)

label_10 = Label(window, text='Profession', width=20, font=('bold', 10))
label_10.place(x=80, y=530)

profs = ['Student', 'Graduate', 'Employee']
prof_var = StringVar()
prof_var.set('Select your profession')
OptionMenu(window, prof_var, *profs).place(x=240, y=530)

def Onclicked():
    print('Form submitted successfully....')
    display()

Button(window, text='Submit',width=20,bg='brown',fg='white', command = Onclicked).place(x=180,y=600)

def display():
    print('Entered Details are:')
    print('First name: ' + FN.get())
    print('Last name: ' + LN.get())
    print('Gender: ' + ('Male' if gendvar.get() == 1 else 'Female'))
    print('Age: ' + age.get())
    print('Mobile: ' + mob.get())
    print('Country: ' + c.get())
    lang = []
    if var1.get() == 1:
        lang.append('English')
    if var2.get() == 1:
        lang.append('Hindi')
    print('Language: ' + str(var1.get()) + str(var2.get()))
    print('Address: ' + add.get())
    print("Whatsapp number: " + wnum.get())
    print('Profession: ' + prof_var.get())

window.mainloop()