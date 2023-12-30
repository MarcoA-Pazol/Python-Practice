#Write a program thats apply a discount to a shopping bill.
import sqlite3
from tkinter import ttk
import tkinter
from tkinter import messagebox


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
        cursor.execute('CREATE TABLE IF NOT EXISTS Products(ID INTEGER PRIMARY KEY AUTOINCREMENT, Product TEXT NOT NULL, Price REAL NOT NULL, Have_Discount INTEGER NOT NULL, Discount REAL NOT NULL)')
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
    
    #Loading input data
    Product = ('1L Milk Carton', 'Eggs Dozen', '1Kg Grappes', 'Cotagge Cheese 1Kg', '1Kg Suggar', '1L Oil', '1Kg Soap')
    Price = (2.20, 3.85, 4.25, 3.99, 2.30, 2.49, 1.99)
    Have_Discount = (1, 0, 1, 0, 0, 0, 1)
    Discount = (0.10, 0.05, 0.25, 0.15, 0.07, 0.15, 0.20)
    
    #Get DB data
    product_comprobation = cursor.execute('SELECT * FROM Products WHERE Product = ?', Product).fetchone()
    
    #Validation: Inserting data
    try:                    
        if product_comprobation is not None:
            messagebox.showwarning('Repeated value', 'It is not posible to insert repeated values, value that you provide is in table.')
        else:
            try:
                cursor.execute('INSERT INTO Products(Product, Price, Have_Discount, Discount) VALUES(?, ?, ?, ?)', (Product, Price, Have_Discount, Discount))
                messagebox.showinfo('Insert data', 'Data has inserted succesfully')
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)
        messagebox.showerror('Error', 'There was an error inserting data, this is not the correct way to insert data dictionary on table, please tell this to support at adress@developing.dev')


        
#Get bill acount with applied or not applied discounts.
def get_bill():
    pass


"""GRAPHIC INTERFACE"""
# root = tkinter.Tk()
# root.title('Store Discounts')
# root.geometry('600x400+400+100')
# root.config(bg = 'SkyBlue')

# root.mainloop()

# insert_data()

create_database()
insert_data()


    
    
    
    