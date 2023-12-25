#Write a program thats apply a discount to a shopping bill.
import sqlite3
from tkinter import ttk
import tkinter
import tkinter.messagebox


"""METHODS"""

#Create Database using Sqlite3
def create_database():
    """
    DOCSTRING:
        Create a database and a table if it does not exist.
    
    Attributes:
        product (str): [Product]
        price (float): [Price]
        have_discount (boolean): [Have_Discount]
        discount (float): [Price]
    
    Returns:
        null
    """
    conn = sqlite3.connect('Products')
    cursor = conn.cursor()
    try:
        cursor.execute('CREATE TABLE IF NOT EXIST Products(ID Integer PRIMARY KEY, Product Text NOT NULL, Price Float NOT NULL, have_discount Boolean NOT NULL, discount Float NOT NULL)')
    except:
        print('There was an error creating "Products" table')
        
#Get bill acount with applied or not applied discounts.
def get_bill():
    pass

    
    
    
    