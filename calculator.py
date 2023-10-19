import tkinter
from tkinter import*

mw=Tk()
mw.title("calculator")

def clear():
    db.delete(0,END)

def btn_clk(num):
    cur_num=db.get()
    clear()
    f_num=cur_num+num
    db.insert(0,f_num)

first_num=0
math=''
math_sign=''

ms_list=['+','-','*','/']

def calc(math_type,ms):
    global first_num, math,math_sign
    math_sign=ms
    math = math_type
    first_num = db.get()
    for x in ms_list:
        if x in first_num:
            first_num=first_num.replace(x,'')
    clear()
    db.insert(0,first_num+math_sign)

def equal():
    result=''
    global first_num,math,math_sign
    second_num=db.get().replace(str(first_num)+math_sign,'')
    clear()
    if math=='add':
        result=float(first_num) + float(second_num)
    elif math=='sub':
        result=float(first_num) - float(second_num)
    elif math=='mul':
        result=float(first_num) * float(second_num)
    elif math=='div':
        result=float(first_num) / float(second_num)
        result=round(result,4)
    if result == int(result):
        db.insert(0, str(int(result)))
    else:
        db.insert(0, str(result))

#creating widges
db=Entry(mw,width=14,font=('Arial',28),justify=RIGHT)

btn_0=Button(mw,text='0',padx=36,pady=10,font=('Arial',14),command=lambda:btn_clk('0')) 
btn_1=Button(mw,text='1',padx=36,pady=10,font=('Arial',14),command=lambda:btn_clk('1'))
btn_2=Button(mw,text='2',padx=36,pady=10,font=('Arial',14),command=lambda:btn_clk('2'))
btn_3=Button(mw,text='3',padx=36,pady=10,font=('Arial',14),command=lambda:btn_clk('3'))
btn_4=Button(mw,text='4',padx=36,pady=10,font=('Arial',14),command=lambda:btn_clk('4'))
btn_5=Button(mw,text='5',padx=36,pady=10,font=('Arial',14),command=lambda:btn_clk('5'))
btn_6=Button(mw,text='6',padx=36,pady=10,font=('Arial',14),command=lambda:btn_clk('6'))
btn_7=Button(mw,text='7',padx=36,pady=10,font=('Arial',14),command=lambda:btn_clk('7'))
btn_8=Button(mw,text='8',padx=36,pady=10,font=('Arial',14),command=lambda:btn_clk('8'))
btn_9=Button(mw,text='9',padx=36,pady=10,font=('Arial',14),command=lambda:btn_clk('9'))

btn_pylance=Button(mw,text='.',padx=36,pady=10,font=('Arial',14),command=lambda:btn_clk('.'))


btn_clear=Button(mw,text='clear',padx=21,pady=10,font=('Arial',14),command=clear)
btn_div=Button(mw,text='/',padx=36,pady=10,font=('Arial',14),command=lambda:calc('div','/'))
btn_mul=Button(mw,text='*',padx=36,pady=10,font=('Arial',14),command=lambda:calc('mul','*'))
btn_sub=Button(mw,text='-',padx=36,pady=10,font=('Arial',14),command=lambda:calc('sub','-'))
btn_add=Button(mw,text='+',padx=36,pady=10,font=('Arial',14),command=lambda:calc('add','+'))
btn_equal=Button(mw,text='=',padx=36,pady=40,font=('Arial',14),command=equal)

btn_div.grid(row=5,column=0,padx=2,pady=2)
btn_mul.grid(row=5,column=1,padx=2,pady=2)
btn_sub.grid(row=6,column=0,padx=2,pady=2)
btn_add.grid(row=6,column=1,padx=2,pady=2)
btn_equal.grid(row=5,column=2,rowspan=2,padx=2,pady=2)

btn_clear.grid(row=4,column=2,padx=2,pady=2)
btn_0.grid(row=4,column=0,padx=2,pady=2)

btn_1.grid(row=3,column=0,padx=2,pady=2)
btn_2.grid(row=3,column=1,padx=2,pady=2)
btn_3.grid(row=3,column=2,padx=2,pady=2)

btn_4.grid(row=2,column=0,padx=2,pady=2)
btn_5.grid(row=2,column=1,padx=2,pady=2)
btn_6.grid(row=2,column=2,padx=2,pady=2)

btn_7.grid(row=1,column=0,padx=2,pady=2)
btn_8.grid(row=1,column=1,padx=2,pady=2)
btn_9.grid(row=1,column=2,padx=2,pady=2)

btn_pylance.grid(row=4,column=1,padx=2,pady=2)

db.grid(row=0,column=0,columnspan=3,padx=10,pady=10)




mw.mainloop()