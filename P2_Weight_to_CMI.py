#Write a program that converts your stature and weight to IMC
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#METHODS
def get_BMI():
   
   #Debugging
    try:
        #Variables
        name.set(name.get())
        weight.set(weight.get())
        height.set(height.get())
        
        #Constants
        BMI = (weight.get()) / ((height.get())**2)
    except:
        messagebox.showerror('Data validation', 'You may fill all the spaces in blank, and it have to be the correct required datatypes (Name:String, Weight:Float, Height:Float), try again.')

    #Debugging
    try:
        #Validation
        if name.get() == "":
            messagebox.showwarning('Empty blank', 'You may fill name blank with string.')
        elif len(name.get()) <2:
            messagebox.showwarning('Invalid name', 'Name that you has introduce seems too short to be valid, please insert a valid name, please.')
        elif len(name.get()) > 16:
            messagebox.showwarning('Invalid name', 'Name that you has introduce seems too long to be valid, please insert a valid name, please.')   
        else:
            pass
        
        if weight.get() == 0:
            messagebox.showwarning('Empty blank', 'You may fill weight blank with double or integer number.')
        else:
            pass
        
        if height.get() == 0:
            messagebox.showwarning('Empty blank', 'You may fill height blank with float number.')
        else:
            pass
            
        
            
        #Comprobation
        if BMI < 18.5:
            status = 'Underweight'
        elif BMI > 18.5 and BMI < 24.9:
            status = 'Normal weight'
        elif BMI > 25 and BMI < 26.9:
            status = 'Overweight - I'
        elif BMI > 27 and BMI < 29.9:
            status = 'Overweight - II'
        elif BMI > 30 and BMI < 34.9:
            status = 'Obesity - I'
        elif BMI > 35 and BMI < 39.9:
            status = 'Obesity - II'
        elif status > 40:
            status = 'Obesity - II (Morbide obesity)'
        else:
            status = 'Error'

        #Get result
        result_label.config(text=f'Patient: {name.get()}\nBMI: {round(BMI,2)}\nStatus: {status}')
        
        #Set values to init values
        name.set(value="")
        weight.set(value=0)
        height.set(value=0)
    except:
        name.set(value='')
        weight.set(value=0)
        height.set(value=0)



#GRAPHIC INTERFACE
root = tk.Tk()
root.title('Corporal mass index')
root.geometry('500x600+450+0')
root.config(bg='Gray20')

#Field variables
name = tk.StringVar(value="")
weight = tk.DoubleVar(value=0)
height = tk.DoubleVar(value=0)

#Frames
base_frame = tk.Frame(root, bg = 'Gray30', width = 370, height = 500)
base_frame.place(x = 70, y = 80)

#Labels
bmi_title = tk.Label(base_frame, text = 'G e t   y o u r   BMI', bg = 'Gray10', fg = 'Green', font = ('Times', '20', 'bold'), width = 20)
bmi_title.place(x = 0, y = 20)

container_label = tk.Label(base_frame, bg = 'Gray60', height = 13, width = 20, font = ('Times', '20', 'bold'))
container_label.place(x = 0, y = 85)

name_label = tk.Label(container_label, bg = 'Gray60', font = ('Times', '15', 'bold'), text = 'Name:')
name_label.place(x = 10, y = 20)

weight_label = tk.Label(container_label, bg = 'Gray60', font = ('Times', '15', 'bold'), text = 'Weight:')
weight_label.place(x = 10, y = 70)

height_label = tk.Label(container_label, bg = 'Gray60', font = ('Times', '15', 'bold'), text = 'Height:')
height_label.place(x = 10, y = 120)

result_label = tk.Label(container_label, fg = 'Green', text = '', bg = 'Gray10', font = ('Times', '8', 'bold'), width = 40, height = 10)
result_label.place(x = 20, y = 235)



#Entrys
name_entry = tk.Entry(container_label, font = ('Times', '12', 'bold'), textvariable = name)
name_entry.place(x = 85, y = 20)

weight_entry = tk.Entry(container_label, font = ('Times', '12', 'bold'), textvariable = weight)
weight_entry.place(x = 85, y = 70)

height_entry = tk.Entry(container_label, font = ('Times', '12', 'bold'), textvariable = height)
height_entry.place(x = 85, y = 120)

#Buttons
submit_button = tk.Button(container_label, text = 'Submit', font = ('Couries', '14', 'bold'), fg = 'Snow', bg = 'Navy', command=lambda:get_BMI())
submit_button.place(x = 100, y = 170)

#Separators / Decorations
separator_1 = ttk.Separator(root, orient = 'horizontal')
separator_1.pack(fill='x', padx = 10, pady= 50)

root.mainloop()






    