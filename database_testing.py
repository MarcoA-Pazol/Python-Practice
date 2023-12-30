import sqlite3

#Loading input data
Product = ['1L Milk Carton', 'Eggs Dozen', '1Kg Grappes', 'Cotagge Cheese 1Kg', '1Kg Suggar', '1L Oil', '1Kg Soap']
Price = [2.20, 3.85, 4.25, 3.99, 2.30, 2.49, 1.99]
Have_Discount = [1, 0, 1, 0, 0, 0, 1]
Discount = [0.10, 0.05, 0.25, 0.15, 0.07, 0.15, 0.20]

#DB Connection
conn = sqlite3.connect('Products_DB.db')
cursor = conn.cursor()

#Create Table 
cursor.execute('CREATE TABLE IF NOT EXISTS Products(ID INTEGER PRIMARY KEY AUTOINCREMENT, Product TEXT, Price REAL, Have_Discount INTEGER, Discount REAL)')
conn.commit()

#Insert Values
i = 1
for data in zip(Product, Price, Have_Discount, Discount):
    try:
        cursor.execute('INSERT INTO Products(Product, Price, Have_Discount, Discount) VALUES(?, ?, ?, ?)', data)
        i += 1
        print(f'Data #{i} inserted.')
    except Exception as e:
        print(e)
