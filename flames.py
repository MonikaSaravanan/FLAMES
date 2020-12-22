from tkinter import*
from tkinter.messagebox import showinfo

win  = Tk()
win.title("Calculate your love percent")
win.configure(background = "black")
win.geometry("400x180")

def calc():
  s1=entry1.get().lower()
  s2=entry2.get().lower()
  s1=s1.replace(" ","")
  s2=s2.replace(" ","")

  l1=list(s1)
  l2=list(s2)
  l3=l1+l2

  for i in l3:
     if i in l1 and i in l2:
        l1.remove(i)
        l2.remove(i)
  l3=l1+l2
  a=len(l3)
   
  l = ["Friends🤝","Love👨‍❤️‍💋‍👨","Affection👩🏼‍🤝‍🧑🏼","Marriage👩‍👩‍👦‍👦","Enemy🤼‍","Siblings👩‍👦"]
  while(len(l)>1):
    if a<len(l):
      l.remove(l[a])
    else:
      b=a%len(l)-1
      l.remove(l[b])
      l=l[b:]+l[:b]

  entry3.insert(END,l[0]) 

  
label1=Label(win,text="Your Name",font=("papyrus",12,"bold"),background="black",foreground="white")
label1.grid(row=1,column=0,sticky="w")

entry1=Entry(win,font=("papyrus",12,"bold"))
entry1.grid(row=1,column=1)

label2=Label(win,text="Partner's Name",font=("papyrus",12,"bold"),background="black",foreground="white")
label2.grid(row=2,column=0,sticky="w")

entry2=Entry(win,font=("papyrus",12,"bold"))
entry2.grid(row=2,column=1)

label3=Label(win,text="Relationship Status",font=("papyrus",12,"bold"),background="black",foreground="white")
label3.grid(row=4,column=0)

entry3=Entry(win,font=("papyrus",12,"bold"))
entry3.grid(row=4,column=1)

button = Button(win,text="Calculate Now!",font=("papyrus",12,"bold"),command=calc,fg="pink",bg="black")
button.grid(row=3,columnspan=2)

win.mainloop()