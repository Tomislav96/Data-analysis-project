#Projekt SPI
# -*- coding: utf-8 -*-

# Imports
import pymysql
import pandas as pd
import numpy as np
import json
import requests
import random
from sqlalchemy import create_engine
from datetime import datetime

# Import CSV Sales_Products file
CSV_FILE_PATH = r"C:\Users\Tomislav\Downloads\bikes\bikes.csv"
df = pd.read_csv(CSV_FILE_PATH, delimiter=',', encoding= 'unicode_escape')
print("CSV size: ", df.shape)


# Print leading rows of dataframe
print(df.head())


#Database connection
user = 'root'
passw = 'MyNewPass'
host = 'Localhost'
port = 3306
database = 'bikesr'

mydb = create_engine('mysql+pymysql://' + user + ':' + passw + '@' + host + ':' + str(port) + '/' + database , echo=False)
print(mydb)
connection = mydb.connect()

#DDL
customer_ddl = "CREATE TABLE bikesr.customer (id INT NOT NULL AUTO_INCREMENT , age INT NOT NULL, age_group VARCHAR(45), gender VARCHAR(45), PRIMARY KEY (id), UNIQUE INDEX id_UNIQUE (id ASC));"
connection.execute(customer_ddl)
product_type_ddl = "CREATE TABLE bikesr.product_type (id INT NOT NULL AUTO_INCREMENT, category VARCHAR(45), sub_category VARCHAR(45),PRIMARY KEY (id), UNIQUE INDEX id_UNIQUE (id ASC));"
connection.execute(product_type_ddl)
product_ddl = "CREATE TABLE bikesr.product (id INT NOT NULL AUTO_INCREMENT, product VARCHAR(200) NOT NULL, product_type_id INT NOT NULL, PRIMARY KEY (id), UNIQUE INDEX id_UNIQUE (id ASC), CONSTRAINT product_type_id FOREIGN KEY (product_type_id) REFERENCES bikesR.product_type (id));"
connection.execute(product_ddl)
location_ddl = "CREATE TABLE bikesr.location (id INT NOT NULL AUTO_INCREMENT,  state VARCHAR(45), country VARCHAR(45), PRIMARY KEY (id), UNIQUE INDEX id_UNIQUE (id ASC));"
connection.execute(location_ddl)
production_cost_ddl = "CREATE TABLE bikesr.production_cost (id INT NOT NULL AUTO_INCREMENT, unit_cost INT, cost INT, profit INT, PRIMARY KEY (id), UNIQUE INDEX id_UNIQUE (id ASC));"
connection.execute(production_cost_ddl)
order_ddl = "CREATE TABLE bikesr.order (id INT NOT NULL AUTO_INCREMENT, order_date DATETIME, order_quantity INT, unit_price INT, revenue INT, customer_id INT NOT NULL, product_id INT NOT NULL, location_id INT NOT NULL, production_cost_id INT NOT NULL, PRIMARY KEY(id), UNIQUE INDEX id_UNIQUE (id ASC),  INDEX customer_id_idx (customer_id ASC), INDEX product_id_idx (product_id ASC), INDEX location_id_idx (location_id ASC), INDEX production_cost_idx (production_cost_id ASC), CONSTRAINT customer_id    FOREIGN KEY (customer_id)    REFERENCES bikesR.customer (id), CONSTRAINT product_id    FOREIGN KEY (product_id)    REFERENCES bikesR.product (id), CONSTRAINT location_id    FOREIGN KEY (location_id)    REFERENCES bikesR.location (id), CONSTRAINT production_cost_id    FOREIGN KEY (production_cost_id)    REFERENCES bikesR.production_cost (id))"
connection.execute(order_ddl)

#DML
#CUSTOMER
customer = df['Age']
age_group, gender = [], []
for i in range (len(customer)):
    temm_df = (df['Age_Group'][i])
    age_group.append(temm_df)
    temm_df = (df['Gender'][i])
    gender.append(temm_df)
customer_data = pd.DataFrame({'id':list(range(1,len(customer)+1)), 'age':customer, 'age_group':age_group, 'gender':gender})
customer_data.to_sql(con=mydb, name='customer', if_exists='append', index=False)

#SUB CATEGORY
sub_category = []
product_type = df['Category']
for i in range (len(customer)):
    tem_df = (df['Sub_Category'][i])
    sub_category.append(tem_df)
product_type_data = pd.DataFrame({'id':list(range(1,len(product_type)+1)),'Category':product_type, 'sub_category':sub_category})
product_type_data.to_sql(con=mydb, name='product_type', if_exists='append', index=False)


#PRODUCT   
product_names = df['Product']
product_type_id=[]
for i, row in df.iterrows():
    product_type_id.append(int(product_type_data['id'].iloc[i]))
product_data = pd.DataFrame({'id':list(range(1,len(product_type_id)+1)),'product':product_names, 'product_type_id':product_type_id})
product_data.to_sql(con=mydb, name='product', if_exists='append', index=False)    

#LOCATION
location = df['State']
country = []
for i in range (len(customer)):
    temm_df = (df['Country'][i])
    country.append(temm_df)
location_data = pd.DataFrame({'id':list(range(1,len(location)+1)), 'state':location, 'country':country})
location_data.to_sql(con=mydb, name='location', if_exists='append', index=False)

#PRODUCTION COST
production_cost = df['Unit_Cost']
cost =[]
profit =[]
for i in range(len(customer)):
    tt_df = (df['Cost'][i])
    cost.append(tt_df)
    tt_df = (df['Profit'][i])
    profit.append(tt_df)
production_cost_data =  pd.DataFrame({'id':list(range(1,len(production_cost)+1)), 'unit_cost':production_cost, 'cost':cost, 'profit':profit})
production_cost_data.to_sql(con=mydb, name='production_cost', if_exists='append', index=False)

order = []
customer_id, product_id, location_id, production_cost_id= [], [], [], []
for i, row in df.iterrows():
    order_date = df['Order_Date'].iloc[i].split('-')
    order.append(datetime(int(order_date[0]), int(order_date[1]), int(order_date[2])))
    
    customer_id.append(int(customer_data['id'].iloc[i]))
    
    product_id.append(int(product_data['id'].iloc[i]))

    location_id.append(int(location_data['id'].iloc[i]))
    
    production_cost_id.append(int(production_cost_data['id'].iloc[i]))
    
    
order_data = pd.DataFrame({'id':list(range(1,len(customer_id)+1)),'order_date':order , 'order_quantity':df['Order_Quantity'], 'unit_price':df['Unit_Price'], 'revenue':df['Revenue'], 'customer_id':customer_id, 'product_id':product_id, 'location_id':location_id, 'production_cost_id':production_cost_id})
order_data.to_sql(con=mydb, name='order', if_exists='append', index=False)

