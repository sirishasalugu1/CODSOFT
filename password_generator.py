from tkinter import*
import random
import string
root=Tk()
root.title("PASSWORDGENERATOR")
def password_generator():
    try:
        length=int(c.get())
        characters=string.digits+string.ascii_letters+string.punctuation.replace('<','').replace('>','')
        password=''.join(random.choice(characters) for i in range(length))
        Label2.config(text="generated password:"+password)
        if length<=0:
            raise ValueError
    except ValueError:
        Label2.config(text="invalid entry")

Label1=Label(root,text="enter length of the password:")
Label1.pack()
c=Entry(root)
c.pack()
b_1=Button(root,text="generate paassword",command=password_generator)
b_1.pack()
Label2=Label(root,text="")
Label2.pack()
root.mainloop()