import csv
from sell import get_file_id
from advance import get_date_file
from report import add_to_inventory

# with open('students.csv', 'w', newline='') as file:
#     writer = csv.writer(file, delimiter="|")
#     writer.writerow(["id", "product_name", "buy_date", "buy_price", "expiration_date"])

# this file contains all the functions related to the buy subparser 

"""this functions adds passed bought product to the bought.csv and calls add_to_inventory 
function to add it to inventory.csv """
def buy_product(product_name, buy_price, expiration_date, amount):
    add_to_inventory(product_name,buy_price, expiration_date, "bought", amount )
    with open("bought.csv", 'a', newline="") as file:
     writer = csv.writer(file, lineterminator='\n')
     bought_id = get_file_id("bought.csv")
     buy_date = get_date_file()
     formatted_buy_price = format(buy_price,".2f")
     product =[bought_id,product_name,buy_date,formatted_buy_price,expiration_date,amount]
     writer.writerow(product)
     file.close()
     

