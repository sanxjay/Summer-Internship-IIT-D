#!/usr/bin/env python
"""
Sample script that uses the concreep module created using
MATLAB Compiler SDK.

Refer to the MATLAB Compiler SDK documentation for more information.
"""
#try and except is used to handle the errors.

try:
    #import matplotlib.pyplot as plt
    #import matplotlib.image as mpimg
    import numpy as np
    import io
    #import os
    #import random
    import sys
    import tkinter as tk
    from tkinter import filedialog,messagebox
except Exception as e:
    print(f'A module is missing.\n{e}\nRead Readme.txt to know necessary modules.')

try:
    import concreep
except Exception as e:
    print(f'An unexpected error occured.\n{e}')
    sys.exit(1)

# Import the matlab module only after you have imported
# MATLAB Compiler SDK generated Python modules.

print('Processing...',end='')
import matlab

my_concreep = concreep.initialize()

def open_file():
    global file_path
    file_path = filedialog.askopenfilename(
        title="Open File",
        filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))
    )
    if file_path:
        file_label.config(text=f'Selected file : {file_path}')
        #messagebox.showinfo("File Selected", f"File selected: {file_path}")
    else:
        file_label.config(text='\nNo file selected')
def submit_file():
    try:
        global f
        f=open(f'{file_path}','r')
        win.destroy()
    except NameError:
        print('\nNo file selected',end='')


win=tk.Tk()

win.geometry("400x300+400+100") #use (x) symbol instead of * // +400 +100 
win.title('Concreep.')

main_fr=tk.Frame(win)
main_fr.pack(fill='both',expand=1)

body=tk.Label(main_fr,text='Concreep Model \n',font=('Calibri',18))
body.pack()

row1=tk.Frame(main_fr)
row1.pack()

open_button = tk.Button(row1, text="Open File", command=open_file)
open_button.pack()

file_label = tk.Label(win, text="No file selected", wraplength=100)
file_label.pack(pady=20)

close_button = tk.Button(row1, text="Submit the data", command=submit_file)
close_button.pack(pady=20)

win.mainloop()

'''if file_path:
    #printpath=tk.Label(row2,text=f'Selected Path= {file_path}')
my_concreep.concreep(stdout=io.StringIO(), stderr=io.StringIO())    ...f(x),f(x),stdout=io.StringIO())
print("Rename the data file to \"data.txt\"")
f=open('data.txt','r')
'''
nums=f.read().split('\n')   #nums is a list


try:
    TstartIn = matlab.double([float(nums[0].split('=')[1])], size=(1, 1))
    TminIn = matlab.double([float(nums[1].split('=')[1])], size=(1, 1))
    TmaxIn = matlab.double([float(nums[2].split('=')[1])], size=(1, 1))
    b_powerIn = matlab.double([float(nums[3].split('=')[1])], size=(1, 1))
    b_logIn = matlab.double([float(nums[4].split('=')[1])], size=(1, 1))
    nu_matrixIn = matlab.double([float(nums[5].split('=')[1])], size=(1, 1))
    V_capillaryIn = matlab.double([float(nums[6].split('=')[1])], size=(1, 1))
    V_c3sIn = matlab.double([float(nums[7].split('=')[1])], size=(1, 1))
    V_c2sIn = matlab.double([float(nums[8].split('=')[1])], size=(1, 1))
    V_c3aIn = matlab.double([float(nums[9].split('=')[1])], size=(1, 1))
    V_c4afIn = matlab.double([float(nums[10].split('=')[1])], size=(1, 1))
    V_gypsumIn = matlab.double([float(nums[11].split('=')[1])], size=(1, 1))
    V_portIn = matlab.double([float(nums[12].split('=')[1])], size=(1, 1))
    V_ettrIn = matlab.double([float(nums[13].split('=')[1])], size=(1, 1))
    V_msIn = matlab.double([float(nums[14].split('=')[1])], size=(1, 1))
    V_FH3In = matlab.double([float(nums[15].split('=')[1])], size=(1, 1))
    V_hydrogarnetIn = matlab.double([float(nums[16].split('=')[1])], size=(1, 1))
    V_hcIn = matlab.double([float(nums[17].split('=')[1])], size=(1, 1))
    V_mcIn = matlab.double([float(nums[18].split('=')[1])], size=(1, 1))
    V_calciteIn = matlab.double([float(nums[19].split('=')[1])], size=(1, 1))
    V_AS2In = matlab.double([float(nums[20].split('=')[1])], size=(1, 1))
    V_cshIn = matlab.double([float(nums[21].split('=')[1])], size=(1, 1))
    
except ValueError as e:
    print(f'\nError : {e}\nFormat of file is not correct.')
    sys.exit(1)
    #goto :42
except IndexError as e:
    print(f'\nError : {e}\nFormat of file is not correct.')
    sys.exit(1)
except NameError as e:
    print(f'\nError : {e}\nTotal number of variables are 22. Make sure that all the values are there in the file.')
    sys.exit(1)
    
try:
    pOut = my_concreep.concreep(TstartIn, TminIn, TmaxIn, b_powerIn, b_logIn, nu_matrixIn, V_capillaryIn, V_c3sIn, V_c2sIn, V_c3aIn, V_c4afIn, V_gypsumIn, V_portIn, V_ettrIn, V_msIn, V_FH3In, V_hydrogarnetIn, V_hcIn, V_mcIn, V_calciteIn, V_AS2In, V_cshIn,stdout=io.StringIO())
except Exception as e:
    print(f'\nError : {e}\nTotal number of variables are 22. Make sure that all the values are there in the file.')
    sys.exit(1)


exitconsole=input(f'\nImage saved to the same directory.\nPress enter to exit console')

my_concreep.terminate()


graph_array=np.array(pOut)

graph_array.shape=(30,1)    #this lines make the array of order (30,1) which was (1,30).

file='graph_points.csv'


try:
    np.savetxt(file,graph_array,delimiter=',',fmt='%f')
except Exception as e:
    print(f'Error Occurred :{e}')
    sys.exit(1)
    
print(f'Graph Values saved to {file}')


'''
oldimg=input('Enter the previous image name to overlay the graphs. Make sure to rename the previous image.')
try:    
    img1=mpimg.imread('ConcreeEp.png')
    img2=mpimg.imread(oldimg)
except Exception as e:
    print(f'Error occurred.{e}')
    sys.exit(1)
# Create a figure and axis
fig, ax = plt.subplots()

# Display the first image
ax.imshow(img1, extent=[0, 1, 0, 1], aspect='auto', alpha=0.5)

# Display the second image on top
ax.imshow(img2, extent=[0, 1, 0, 1], aspect='auto', alpha=0.5)

# Adjust plot limits and display
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
plt.show()
'''
