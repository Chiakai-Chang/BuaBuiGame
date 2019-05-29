import tkinter as tk
from tkinter import messagebox
import random

window = tk.Tk()
window.geometry('500x400')
window.title('★★★看你擲筊有沒有好厲害★★★')

#變數
var_listbox = tk.StringVar()
count = 0
r = ''

#大框架
frm = tk.Frame(window,width=500)
frm.pack()

#左框架
frm_l = tk.Frame(frm)
frm_l.pack(side='left',padx=30)

l_num = tk.Label(frm_l,text='',width=20,height=2,bg='white')
l_num.pack(pady=10)

listbox = tk.Listbox(frm_l,listvariable=var_listbox,height=20)
listbox.pack()

#右框架
frm_r = tk.Frame(frm)
frm_r.pack(side='right',padx=50)

l = tk.Label(frm_r,text='',width=35,height=2,bg='yellow')
l.pack()

editer =tk.Label(frm_r,text='''Chiakai亂作
2019/05/29''')
editer.pack(side='bottom',pady=50)


#按鈕
def buabui():
    global count
    listbox.delete(0,listbox.size())
    while True:
        bui1 = random.randint(0,1)
        bui2 = random.randint(0,1)
        
        if bui1 == 0:
            show1 = "正"
        else:
            show1 = "反"
            
        if bui2 == 0:
            show2 = "正"
        else:
            show2 = "反"

        if bui1 == bui2:
            count += 1
            r = '第'+str(count)+'次：笑筊('+str(show1)+","+str(show2)+')'
            listbox.insert('end',r)
        else:
            count += 1
            r = '第'+str(count)+'次：聖筊('+str(show1)+","+str(show2)+')'
            listbox.insert('end',r)
            if count == 1:
                l_num.config(text='總共擲了'+str(count)+'次')
                l.config(text="哇!您 1 次就擲到聖筊了!")
                count = 0
                break
            else:
                l_num.config(text='總共擲了'+str(count)+'次')
                l.config(text=("您一共擲了"+str(count)+"次才擲到聖筊"))
                count = 0
                break
def buabui0():
    global count
    count = 0
    listbox.delete(0,listbox.size())
    l.config(text='')
    l_num.config(text='')

b = tk.Button(frm_r,text='按我擲茭看看吧',command=buabui)
b.pack()

b0 = tk.Button(frm_r,text='重新歸零',command=buabui0)
b0.pack()

window.mainloop()



