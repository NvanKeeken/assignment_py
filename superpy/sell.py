import csv
from advance import get_date_file
import math

# this file contains all the functions related to the sell subparser 

# this function calculates the id of a product in csv file 
def get_file_id(csv_path):
   with open(csv_path, 'r') as file:
       csvreader = csv.reader(file)
       next(csvreader)
       count = 0
       for row in csvreader:
           count += 1
       return count +1
   
# this function finds sold product in bought.csv and returns the id it has in that file as the bought_id
def get_bought_id(product_name, expiration_date):
   with open("bought.csv", "r") as boughtfile:
      reader = csv.DictReader(boughtfile)
      bought_id = ""
      for row in reader:
       if row["product_name"] == product_name and row["expiration_date"] == expiration_date:
          print(row["product_name"], product_name, row["expiration_date"], expiration_date)
          bought_id += row["id"]
          print(bought_id)
          return bought_id
   
# this function adds sold product to sold.csv file 
def add_sold_product(product_name, sell_price, amount, expiration_date):
    with open("sold.csv", 'a', newline="") as soldfile:
     writer = csv.writer(soldfile, lineterminator='\n')
     sell_date = get_date_file()
     sold_id = get_file_id("sold.csv")
     bought_id = get_bought_id(product_name, expiration_date)
     formatted_sell_price = format(sell_price,".2f")
     product =[sold_id,bought_id,product_name,amount,sell_date, formatted_sell_price]
     writer.writerow(product)
     soldfile.close()



