#Write a program thats apply a discount to a shopping bill.
import sqlite3
from tkinter import ttk
from tkinter.ttk import Combobox
import tkinter
from tkinter import messagebox
import numpy as np
import pandas as pd

"""DATA SETS"""
#DB Data
data_set = [
    ('1 Milk Carton', 2.20, 1, 0.10),
    ('Eggs Dozen', 3.85, 0, 0.05),
    ('1Kg Grappes', 4.25, 1, 0.25),
    ('Cotagge Cheese 1Kg', 3.99, 0, 0.15),
    ('1Kg Suggar', 2.30, 0, 0.07),
    ('1L Oil 123', 2.49, 0, 0.15),
    ('1Kg Soap Roma', 1.99, 1, 0.20),
    ('Cheetos Flamin Hot 37g', 1.20, 0, 0.05)
]

#Product_Names
products_set = ['1 Milk Carton', 'Eggs Dozen', '1Kg Grappes', 'Cotagge Cheese 1Kg', '1Kg Suggar', '1L Oil 123', '1Kg Soap Roma', 'Cheetos Flamin Hot 37g']


"""METHODS"""
#Create Database using Sqlite3
def create_database():
    """
    DOCSTRING:
        Create a database and a table if it does not exist.
    
    Attributes:
        none
    
    Returns:
        null
    """
    conn = sqlite3.connect('Products')
    cursor = conn.cursor()
    try:
        cursor.execute('CREATE TABLE IF NOT EXISTS Products(ID INTEGER PRIMARY KEY AUTOINCREMENT, Product TEXT, Price REAL, Have_Discount INTEGER, Discount REAL)')
        messagebox.showinfo('Create table', 'Products table has been created succesfully!')
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)
        messagebox.showerror('Error', 'There was an error creating "Products" table')


#Insert data in Products table
def insert_data():
    """
    DOCSTRING:
        Insert data examples in DB to be used in the future.
    
    Attributes:
        none
    
    Returns: 
        null
    """
    #DB connection
    conn = sqlite3.connect('Products')
    cursor = conn.cursor()
    
    """I HAVE TO FIX THE VALIDATION AND COMPROBATION"""
    #Get DB Data
    product_comprobation = cursor.execute('SELECT * FROM Products').fetchall()
    
    #Validation: Inserting data
    try:                    
        if product_comprobation is not None:
           messagebox.showwarning('Repeated value', 'It is not posible to insert repeated values, value that you provide is in table.')
        else:
            try:
                cursor.executemany('INSERT INTO Products(Product, Price, Have_Discount, Discount) VALUES (?, ?, ?, ?)', data_set)
                messagebox.showinfo('Insert data', 'Data has inserted succesfully')
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)
        messagebox.showerror('Error', 'There was an error inserting data, this is not the correct way to insert data dictionary on table, please tell this to support at adress@developing.dev')
    conn.commit()
    conn.close()
    
    
def submmit():
    pass


        
#Get bill acount with applied or not applied discounts.
def get_bill():
    pass


"""GRAPHIC INTERFACE"""
root = tkinter.Tk()
root.title('Store Discounts')
root.geometry('600x400+400+100')
root.config(bg = 'SkyBlue')

#Field variables
product_cuantity = ttk.IntVar(value = 0)
product_selected = ttk.StringVar(value = '')
price_discounted = ttk.DoubleVar(value = 0)
normal_price = ttk.DoubleVar(value = 0)

#Frames
base_frame = ttk.Frame(root, bg = 'Blue', width = 200, height = 200)
base_frame.place(x = 50, y = 10)

principal_frame = ttk.Frame(root, bg = 'Snow', width = 190, height = 190)
principal_frame.place(x = 55, y = 15)

#Labels
discounts_text = ttk.Label(principal_frame, bg = 'Snow', fg = 'Black', text = 'D I S C O U N T S', font = ('Times', '10', 'bold'))
discounts_text.place(x = 50, y = 10)

select_product_label = ttk.Label(principal_frame, bg = 'Snow', fg = 'Black', text = 'Product: ', font = ('Times', '8', 'bold'))
select_product_label.place(x = 10, y = 20)

#Combobox
products_list = ttk.Combobox(principal_frame, values = products_set)
products_list.place(x = 50, y = 20)

#Button
submmit_button = ttk.Button(principal_frame, text = 'Submmit', command = lambda:submmit())
submmit_button.place(x = 20, y = 50)

root.mainloop()

    
    
    
    