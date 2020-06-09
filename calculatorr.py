from tkinter import *
root = Tk()
root.title("Calculator using Python for user")
root.resizable(0,0)

e = Entry(root,font=("arial",20,"bold"),justify= 'right',bd=30,insertwidth=3)
e.grid(row=0, column=0 ,columnspan=5)

#onclick_function
def button_click(num):
    present = e.get()
    e.delete(0,END)
    e.insert(0,str(present) + str(num))

#clear function
def button_clear():
    e.delete(0,END)

#addfunction
def add_func():
        first_num = e.get()
        global f_num
        global math
        math = "addition"
        f_num = float(first_num)
        e.delete(0,END)

#Equalfunction()
def equal_func():
    sec_num = e.get()
    e.delete(0,END)

    if math =="addition":
        e.insert(0,(f_num) + float(sec_num))

    if math =="Substraction":
        e.insert(0,(f_num) - float(sec_num))

    if math =="multiplication":
        e.insert(0,f_num * float(sec_num))


    if math =="division":
        e.insert(0,f_num / float(sec_num))


#substractfun
def substract_func():
    first_num = e.get()
    global f_num
    global math
    math = "Substraction"
    f_num = float(first_num)
    e.delete(0,END)

#mul_function
def mul_func():
    first_num = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_num)
    e.delete(0,END)


#divisionfunction
def div_func():
    first_num = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_num)
    e.delete(0,END)

#squarefunction
def square_func():
    first_num = e.get()
    global f_num
    global math
    math = "Square"
    f_num = float(first_num)
    e.delete(0,END)
    if math =="Square":
        e.insert(0,f_num * f_num)

#cubefunction
def cube_func():
    first_num = e.get()
    global f_num
    global math
    math = "Cube"
    f_num = float(first_num)
    e.delete(0,END)
    if math =="Cube":
        e.insert(0,f_num * f_num  * f_num)


#squarerootfunction
def sqroot_func():
    first_num = e.get()
    global f_num
    global math
    math = "Squareroot"
    f_num = float(first_num)
    e.delete(0,END)
    if math =="Squareroot":
        e.insert(0,f_num ** 0.5)


#exponentialfunction
def exponential_func():
    first_num = e.get()
    global f_num
    global math
    math = "exponential"
    f_num = float(first_num)
    e.delete(0,END)
    if math == "exponential":
        e.insert(0,2.7182818285**f_num)



#buttons
button_clear = Button(root, text="Clear",padx=50,pady=20,font=("arial"), command=button_clear)
button_exponential = Button(root, text="e(x)",padx=50,pady=20,font=("arial"), command=exponential_func)
button_squareroot = Button(root, text="√x",padx=50,pady=20,font=("arial"), command=sqroot_func)
button_division = Button(root, text="/",padx=50,pady=20,font=("arial"), command=div_func)
number_7 = Button(root, text="7",padx=60,pady=20,font=("arial"), command=lambda:button_click(7))
number_8 = Button(root, text="8",padx=56,pady=20,font=("arial"), command=lambda:button_click(8))
number_9 = Button(root, text="9",padx=53,pady=20,font=("arial"), command=lambda:button_click(9))
button_mul = Button(root, text="*",padx=49,pady=20,font=("arial"), command=mul_func)
number_4 = Button(root, text="4",padx=60,pady=20,font=("arial"), command=lambda:button_click(4))
number_5 = Button(root, text="5",padx=56,pady=20,font=("arial"), command=lambda:button_click(5))
number_6 = Button(root, text="6",padx=53,pady=20,font=("arial"), command=lambda:button_click(6))
button_minus = Button(root, text="-",padx=49,pady=20,font=("arial"), command=substract_func)
number_1 = Button(root, text="1",padx=60,pady=20,font=("arial"), command=lambda:button_click(1))
number_2 = Button(root, text="2",padx=56,pady=20,font=("arial"), command=lambda:button_click(2))
number_3 = Button(root, text="3",padx=53,pady=20,font=("arial"), command=lambda:button_click(3))
button_addition = Button(root, text="+",padx=47.5,pady=20,font=("arial"), command=add_func)
number_0 = Button(root, text="0",padx=60,pady=20,font=("arial"), command=lambda:button_click(0))
button_xsq = Button(root, text="x²",padx=54,pady=20,font=("arial"), command=square_func)
button_xcub= Button(root, text="x³",padx=51,pady=20,font=("arial"), command=cube_func)
button_equal = Button(root, text="=",padx=50,pady=160,font=("arial"), command=equal_func,borderwidth=4)
button_decimal = Button(root, text=".",padx=50,pady=20,font=("arial"), command=lambda:button_click("."))



#row1
button_clear.grid(row=1,column=0)
button_exponential.grid(row=1,column=1)
button_squareroot.grid(row=1,column=2)
button_division.grid(row=1,column=3)
button_equal.grid(row=1,column=4,rowspan=5)
#row2
number_7.grid(row=2,column=0)
number_8.grid(row=2,column=1)
number_9.grid(row=2,column=2)
button_mul.grid(row=2,column=3)
#row3
number_4.grid(row=3,column=0)
number_5.grid(row=3,column=1)
number_6.grid(row=3,column=2)
button_minus.grid(row=3,column=3)
#row4
number_1.grid(row=4,column=0)
number_2.grid(row=4,column=1)
number_3.grid(row=4,column=2)
button_addition.grid(row=4,column=3)
#row4
number_0.grid(row=5,column=0)
button_xsq.grid(row=5,column=1)
button_xcub.grid(row=5,column=2)
#row5
button_decimal.grid(row=5,column=3)

root.mainloop()
