from tkinter import *

window=Tk()
txtfld=Entry(window)
txtfld.place(x=10,y=10,width=310,height=150)

btn7=Button(window,text="7",font=10)
btn7.place(x=10,y=170,width=70,height=70)

btn8=Button(window,text="8",font=10)
btn8.place(x=90,y=170,width=70,height=70)

btn9=Button(window,text="9",font=10)
btn9.place(x=170,y=170,width=70,height=70)

btn4=Button(window,text="4",font=10)
btn4.place(x=10,y=250,width=70,height=70)

btn5=Button(window,text="5",font=10)
btn5.place(x=90,y=250,width=70,height=70)

btn6=Button(window,text="6",font=10)
btn6.place(x=170,y=250,width=70,height=70)

btn1=Button(window,text="1",font=10)
btn1.place(x=10,y=330,width=70,height=70)

btn2=Button(window,text="2",font=10)
btn2.place(x=90,y=330,width=70,height=70)

btn3=Button(window,text="3",font=10)
btn3.place(x=170,y=330,width=70,height=70)

btn0=Button(window,text="0",font=10)
btn0.place(x=90,y=410,width=70,height=70)

btndiv=Button(window,text="/",font=10)
btndiv.place(x=250,y=170,width=70,height=70)

btnmulti=Button(window,text="X",font=10)
btnmulti.place(x=250,y=250,width=70,height=70)

btnsub=Button(window,text="-",font=10)
btnsub.place(x=250,y=330,width=70,height=70)

btnadd=Button(window,text="+",font=10)
btnadd.place(x=250,y=410,width=70,height=70)

btndot=Button(window,text=".",font=10)
btndot.place(x=10,y=410,width=70,height=70)

btnequal=Button(window,text="=",font=10)
btnequal.place(x=170,y=410,width=70,height=70)

window.title("Calculator")
window.geometry("330x500+10+10")
window.mainloop()