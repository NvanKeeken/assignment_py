import csv
from advance import get_date_Format
import datetime
from advance import get_date_yesterday

# this file contains all the functions related to the report revenue argument 
def get_revenue_per_product(row):
    revenue_per_product = float(row["sell_price"]) * int(row["amount"])
    return revenue_per_product

def get_sold_products_per_date(date):
    with open("sold.csv", "r") as soldfile:
        reader = csv.DictReader(soldfile)
        sold_products_by_date = []
        date_format= get_date_Format(date)
        for row in reader:
            row_date = datetime.datetime.strptime(row["sell_date"], "%Y-%m-%d").strftime(date_format)
            if row_date == date:
                 sold_products_by_date.append(row)
        return sold_products_by_date

def get_total_revenue(date):
        total_revenue = 0
        reader = get_sold_products_per_date(date)
        for row in reader:
             total_revenue += get_revenue_per_product(row)
        return total_revenue
print(get_sold_products_per_date(get_date_yesterday()))