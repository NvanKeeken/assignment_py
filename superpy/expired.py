from report import reset_inventory, add_to_csv, make_inventory
import datetime
from advance import get_date_file
import csv

#  Dit is allemaal een expiriment om expiration date te checkken en te zorgen dat inventory van verleden kunt opvragen
def expiration_check(row):
     current_date = datetime.datetime.strptime(get_date_file(), "%Y-%m-%d")
     row_date = datetime.datetime.strptime(row["Expiration Date"], "%Y-%m-%d")
     is_expired= False
     if row_date.date() < current_date.date():
        is_expired += True
     else:
        is_expired += False
     return is_expired

def get_expired_products():
    expired_products = []
    with open("Invent.csv", "r") as inventoryfile:
        reader = csv.DictReader(inventoryfile)
        for row in reader:
        
           if expiration_check(row):
            expired_products.append(row)
        reset_inventory()
        for line in expired_products:
           product = [line["Product Name"], line["Count"], line["Buy Price"], line["Expiration Date"]]
           print(product)
           add_to_csv("Invent.csv", product)

