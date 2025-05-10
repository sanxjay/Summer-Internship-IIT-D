import tkinter as tk
from tkinter import ttk
import amitsirmerged
import numpy as np
import matlab

my_amitsirmerged = amitsirmerged.initialize()

win=tk.Tk()

win.geometry("600x500+400+100") #use (x) symbol instead of * // +400 +100 
win.title('Two functions One Py')

main_fr=tk.Frame(win)
main_fr.pack(fill='both',expand=1)

body=tk.Label(main_fr,text='2 Input Fx & 1 Input Fx \n',font=('Arial',18))
body.pack()

under=tk.Label(main_fr,text='Single Input Function and Double Input Function')
under.pack()

row1=tk.Frame(main_fr)
row1.pack()

#########FILE##########
f=open('results.txt','w')

znp_list=[]
ynp_list=[]

def filestuff() :
    global znp_list,ynp_list
    f.write('Single function value(s) of L: \n \n')
    #lz=len(znp_list)//6
    for elem in znp_list:
        for ele in elem:
            f.write(f'{ele} \n')
        else:
            f.write('\n')
    else:
            f.write('\n')
        
    f.write('Double function value(s) of L: \n \n')
    #ly=len(ynp_list)//6
    for elem in ynp_list:
        for ele in elem:
            f.write(f'{ele} \n')
        else:
            f.write('\n')
    f.close()
    win.destroy()
#########FILE##########
    
def submitbtn1():
    global znp_list
    js=float(I_ojs1.get('1.0','end'))
    print(js)
    print(type(js))
    io_first=float(js)
    pIn = matlab.double([io_first], size=(1, 1))
    zOut = my_amitsirmerged.amitsirSingleInput(pIn)
    znp=np.array(zOut.noncomplex())
    znp.shape=(6,6)
    znp_list.append([znp])
    #ans=tk.Label(m2fr,text=f'Value of L: \n {znp}').pack()
    print(f'Value of L: \n {znp}')

def submitbtn2():
    global ynp_list
    js=float(I_ojs2.get('1.0','end'))
    print(js)
    print(type(js))
    nu=float(I_onu.get('1.0','end'))
    print(nu)
    print(type(nu))
    io_a=float(js)
    io_b=float(nu)
    aIn = matlab.double([io_a], size=(1, 1))
    bIn = matlab.double([io_b], size=(1, 1))
    yOut = my_amitsirmerged.IsotropiccompliancestensorDOUBLEINPUTFUNCTION(aIn, bIn)
    ynp=np.array(yOut.noncomplex())
    ynp.shape=(6,6)
    ynp_list.append([ynp])
    #ans=tk.Label(m2fr,text=f'Value of L: \n {ynp}').pack()
    print('Value of L: \n', ynp, sep='\n')

        
button1=tk.Button(row1,text='   1st   ',command=None,bg='#CBC3E3').pack(side='left')
button2=tk.Button(row1,text='   2nd   ',command=None,bg='#CBC3E3').pack(side='right',padx=(100,0))



b = tk.Label(win, bd=4) #, bg="#f5f5f5"
b.place(relx=0.5, rely=0.25, relwidth=0.47, relheight=1)


btn_js2=tk.Label(b,text='Enter the value of Js')
btn_js2.pack()
I_ojs2=tk.Text(b,height=1)
I_ojs2.pack()
btn_nu=tk.Label(b,text='Enter the value of Nu')
btn_nu.pack()
I_onu=tk.Text(b,height=1)
I_onu.pack()

row2=tk.Frame(b,bg='#000000')
row2.pack()
submitbtn=tk.Button(row2,text='   SUBMIT   ',command=submitbtn2)
submitbtn.pack()

a = tk.Label(win, bd=4) #, bg="#f5f5f5"
a.place(relx=0.05, rely=0.25, relwidth=0.45, relheight=1)

btn_js1=tk.Label(a,text='Enter the value of Js')
btn_js1.pack()
I_ojs1=tk.Text(a,height=1)
I_ojs1.pack()

submit=tk.Label(a,text='Press Submit to enter entries.')
submit.pack()
#submit button

submitbtn2=tk.Button(a,text='   SUBMIT   ',command=submitbtn1)
submitbtn2.pack()

separator = ttk.Separator(win, orient='vertical') 
separator.place(relx=0.5, rely=0.17, relwidth=0.01, relheight=0.5)


main_=tk.Frame(win)
main_.pack(fill='both',expand=1)

submitbtn=tk.Button(main_,text='   Press to submit the entries in file.   ',command=filestuff)
submitbtn.pack()

win.mainloop()
my_amitsirmerged.terminate()

