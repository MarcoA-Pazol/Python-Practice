#Write a program thats apply a discount to a shopping bill.
import sqlite3
from tkinter import ttk
from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import messagebox

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
#CREATE DB
def create_database():
    """
    DOCSTRING:
        Create a database and a table if it does not exist.
    
    Attributes:
        none
    
    Returns:
        null
    """
    conn = sqlite3.connect('Products_DB')
    cursor = conn.cursor()
    try:
        cursor.execute('CREATE TABLE IF NOT EXISTS Products(ID INTEGER PRIMARY KEY AUTOINCREMENT, Product TEXT, Price REAL, Have_Discount INTEGER, Discount REAL)')
        messagebox.showinfo('Create table', 'Products table has been created succesfully!')
        conn.commit()
        conn.close()
    except Exception as e:
        messagebox.showerror('Error', e)


#INSERT DATA
def insert_data():
    """
    DOCSTRING:
        Insert data examples in DB table to be used in the future.
    
    Attributes:
        none
    
    Returns: 
        null
    """
    #DB connection
    conn = sqlite3.connect('Products_DB')
    cursor = conn.cursor()
    
    """I HAVE TO FIX THE VALIDATION AND COMPROBATION"""
    #Get DB Data
    product_comprobation = cursor.execute('SELECT * FROM Products').fetchall()
    
    #Validation: Inserting data
    try:                    
        if product_comprobation is None:
           messagebox.showwarning('Repeated value', 'It is not posible to insert repeated values, value that you provide is in table.')
        else:
            try:
                cursor.executemany('INSERT INTO Products(Product, Price, Have_Discount, Discount) VALUES (?, ?, ?, ?)', data_set)
                messagebox.showinfo('Insert data', 'Data has inserted succesfully')
            except Exception as e:
                print(e)
    except Exception as e:
        messagebox.showerror('Error', e)
    conn.commit()
    conn.close()
    
    
#SUBMMIT 
def submmit():
    """
        DOCSTRING:
            Submmit data to be comprobed and return the values to be showed in GI visualization label.
        
        Attributes:
            None
            
        Returns:
            Null
    """
    #Select product from Combobox
    list_selected_product = products_list.get()
    #Connect to DB
    conn = sqlite3.connect('Products_DB')   
    cursor = conn.cursor()
    #Fetchone / Validation
    try:
        product_data = cursor.execute('SELECT * FROM Products WHERE Product = ?', (list_selected_product,)).fetchone()
        if product_data is not None:
            if product_data[3] == 1:
                price_discounted.set(product_data[2] - (product_data[2] * product_data[4]))
                discount_percentage.set(product_data[4])
            else:
                price_discounted.set(product_data[2])
                discount_percentage.set(value=0)
                
            #Getting results
            normal_price.set(product_data[2]) 
            product_selected.set(product_data[1])
            print(f'Product: {product_selected.get()}\nPrice: {normal_price.get()}\nApplied discount price: {price_discounted.get()}\nDiscount: {discount_percentage.get()}')
        else:
            messagebox.showwarning('Product selected', 'Product selected is not in existance, please use another product or tell to support if it could suppose an error.')
    except Exception as e:
        messagebox.showerror('Error', e)



"""GRAPHIC INTERFACE"""
root = tk.Tk()
root.title('Store Discounts')
root.geometry('600x400+400+100')
root.config(bg = 'SkyBlue')

#Field variables
product_cuantity = tk.IntVar(value = 0)
product_selected = tk.StringVar(value = '')
price_discounted = tk.DoubleVar(value = 0)
normal_price = tk.DoubleVar(value = 0)
discount_percentage = tk.DoubleVar(value = 0)

#Frames
base_frame = tk.Frame(root, bg = 'Blue', width = 250, height = 300)
base_frame.place(x = 50, y = 10)

principal_frame = tk.Frame(root, bg = 'Snow', width = 240, height = 290)
principal_frame.place(x = 55, y = 15)

#Labels
discounts_text = tk.Label(principal_frame, bg = 'Snow', fg = 'Black', text = 'D I S C O U N T S', font = ('Times', '12', 'bold'))
discounts_text.place(x = 40, y = 10)

select_product_label = tk.Label(principal_frame, bg = 'Snow', fg = 'Black', text = 'Product: ', font = ('Times', '10', 'bold'))
select_product_label.place(x = 10, y = 35)

horizontal_line = tk.Label(principal_frame, bg = 'Blue', fg = 'Blue', width = 240, height = 1, font=('Courier', '1', 'bold'))
horizontal_line.place(x = 0, y = 95)

#Combobox
products_list = ttk.Combobox(principal_frame, values = products_set)
products_list.place(x = 65, y = 35)

#Button
submmit_button = tk.Button(principal_frame, text = 'Submmit', command = lambda:submmit())
submmit_button.place(x = 20, y = 65)

root.mainloop()

#create_database()
#insert_data()
    
    
    
    