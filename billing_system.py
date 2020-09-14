from tkinter import *

window=Tk()
window.wm_title("BILL APP")

def count1():
    num1=float(e2.get())
    num2=float(e3.get())
    a1=num1*num2/100
    answer=num1+a1
    name=e1.get()
    t1.configure(text=answer)
    t2.insert(END,"Customer's Name:- ")
    t2.insert(END,name)
    t2.insert(END,"\nBilling Amount :- ")
    t2.insert(END,answer)

    
    

    
def clear_all():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
if __name__=="__main__":
    
    head_label=Label(window,text="Welcome to Bill Calculater")
    head_label.grid(row=0,column=1)
    l1=Label(window,text="Customer's Name :")
    l1.grid(row=1,column=0)

    l2=Label(window,text="Enter Cost :       ")
    l2.grid(row=2,column=0)

    l3=Label(window,text="GsT % : ")
    l3.grid(row=3,column=0)

    l4=Label(window,text="Total amount with tax: ")
    l4.grid(row=6,column=0)

    e1=Entry(window)
    e1.grid(row=1,column=1)

    e2=Entry(window)
    e2.grid(row=2,column=1)
    
    e3=Entry(window)
    e3.grid(row=3,column=1)



    b1=Button(window,text="Calculate",width=8,command=count1)
    b1.grid(row=4,column=1)
    
    b1=Button(window,text="Clear All",width=8,command=clear_all)
    b1.grid(row=5,column=1)

    t1=Label(window,height=1,width=20)
    t1.grid(row=6,column=1)

    t2=Text(window,height=4,width=40)
    t2.grid(row=2,column=4)
    window.mainloop()
    
    