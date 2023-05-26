import csv
from revenue import get_total_revenue, get_sold_products_per_date

#calculates the cost per sold product
def calculate_cost_per_product(row):
  costs_per_product = float(row["buy_price"]) * int(row["sold_amount"])
  return costs_per_product

# calclates all products bought on date
def get_bought_products_by_date(date):
 with open("bought.csv", "r") as soldfile:
        reader = csv.DictReader(soldfile)
        bought_products_by_date = []
        for row in reader:
            if row["buy_date"] == date:
                bought_products_by_date.append(row)
        return bought_products_by_date
 
# Checks if a product has already been sold one time before 
def is_product_already_sold(bought_products, id):
    product_is_already_sold = False
    if bought_products != []:
        for item in bought_products:
            if item["id"] == id:
                product_is_already_sold = True
            else:
                product_is_already_sold = False
    return product_is_already_sold

""" This function finds the sold products (by date) in the bought.csv with the bought_id. It returns these products 
in a list of dictionaries and adds the key value pair of "sold_amount" with the amount of products 
sold that they. If the same product was sold earlier that date it updates the "sold_amount".
"""
def find_sold_products(date):
    with open ("bought.csv", "r") as boughtfile:
        reader = csv.DictReader(boughtfile)
        bought_products =[]
        sold_products_by_date = get_sold_products_per_date(date)
        for row in reader:
            for product in sold_products_by_date:
                if product["bought_id"] == row["id"] :
                     if is_product_already_sold(bought_products, product["id"]):
                        row["sold_amount"] = str(int(product["amount"]) + int(row["sold_amount"]))
                     else:
                        row["sold_amount"] = product["amount"]
                        bought_products.append(row)
        return bought_products

# this function calculates the total costs of all the products sold on date 
def get_total_costs(date):
        total_costs = 0
        bought_products = find_sold_products(date)
        for row in bought_products:
             total_costs += calculate_cost_per_product(row)
        return total_costs

""" This fuction calculates the total revenue on date by subtracting the the costs of all the products 
 sold from the total revenue """
def calculate_total_profit(date):
    total_revenue = get_total_revenue(date)
    total_costs = get_total_costs(date)
    total_profit = total_revenue - total_costs
    return total_profit



