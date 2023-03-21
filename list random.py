import random
from tkinter import*
root=Tk()

root.title("favourite fruit")
root.geometry("400x400")
root.configure(bg="#800237")

list=["Mango","watermelon","orange","grapes","apple"]
print(list)

label=Label(root,bg="#800237",fg="#FFD700")

def fruit():
    r=random.randint(0,4)
    print(r)
    label["text"]="My favourite fruit is: "+str(list[r])
    
btn=Button(root,bg="#FFD700",fg="#800237",command=fruit,text="favourite fruit?")
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
label.place(relx=0.5,rely=0.7,anchor=CENTER)

root.mainloop()
