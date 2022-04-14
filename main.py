from tkinter import *
window=Tk()
window.title("Mile to Km Converter")
window.config(padx=50,pady=50)
window.minsize(width=500,height=500)
window.configure(bg="white")

#entries
entry=Entry(width=10)
entry.insert(END,string="0")
entry.configure(background="pink")
entry.focus()
entry.grid(column=1,row=0)
def cli():
    num=int(entry.get())
    km=num*1.60934
    label3.config(text=km)
    
label1=Label(text="Miles")
label1.grid(column=2,row=0)
label1.configure(background="white")

label2=Label(text="is equal to")
label2.grid(column=0,row=1)
label2.configure(background="white")

label3=Label(text="0")
label3.grid(column=1,row=1)
label3.configure(background="white")

label4=Label(text="Km")
label4.grid(column=2,row=1)
label4.configure(background="white")

button=Button(text="Calculate",command=cli)
button.grid(column=1,row=2)
    
window.mainloop()   