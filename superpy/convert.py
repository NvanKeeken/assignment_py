import pandas as pd
import pdfkit
import rich_cli
from rich.table import Table
from rich.console import Console
import csv
console = Console()
# def convert_csv_to_pdf():
#     csv_reader = pd.read_csv("inventory.csv")
#     hello = csv_reader.to_html("inventory.html")
#     print(hello)

# convert_csv_to_pdf()

def make_table_from_csv():
    table = Table(title="Superpy Inventory", expand=True, title_style="bold deep_pink2", header_style="pale_turquoise1")
    with open("Invent.csv", "r") as inventoryfile:
        reader = csv.DictReader(inventoryfile)
        table.add_column("Product Name", justify="center", style="yellow", no_wrap=True)
        table.add_column("Count", justify="center", style="dark_violet", no_wrap=True)
        table.add_column("Buy Price", justify="center", style="orange3", no_wrap=True)
        table.add_column("Expiration Date", justify="center", style="deep_sky_blue1", no_wrap=True)
        for row in reader:
           table.add_row(row["Product Name"], row["Count"], f'€ {row["Buy Price"]}', row["Expiration Date"])
        if table.rows:
           console.print(table)
        else:
            console.print("[i]No data known for this date[/i]") 

def make_table_from_sold_csv():
    table = Table(title="Superpy Sold Products", expand=True, title_style="bold deep_pink2", header_style="pale_turquoise1")
    with open("sold.csv", "r") as inventoryfile:
        reader = csv.DictReader(inventoryfile)
        table.add_column("Id", justify="center", style="yellow", no_wrap=True)
        table.add_column("Bought Id", justify="center", style="dark_violet", no_wrap=True)
        table.add_column("Product Name", justify="center", style="orange3", no_wrap=True)
        table.add_column("Amount", justify="center", style="deep_sky_blue1", no_wrap=True)
        table.add_column("Sell date", justify="center", style="deep_sky_blue1", no_wrap=True)
        table.add_column("Sell price", justify="center", style="deep_sky_blue1", no_wrap=True)
        for row in reader:
           table.add_row(row["id"], row["bought_id"], row["product_name"], row["amount"], row["sell_date"], f'€ {row["sell_price"]}')
        if table.rows:
           console.print(table)
        else:
            console.print("[i]No data known for this date[/i]") 

def make_table_from_bought_csv():
    table = Table(title="Superpy Bought Products", expand=True, title_style="bold deep_pink2", header_style="pale_turquoise1")
    with open("bought.csv", "r") as inventoryfile:
        reader = csv.DictReader(inventoryfile)
        table.add_column("Id", justify="center", style="yellow", no_wrap=True)
        table.add_column("Product Name", justify="center", style="orange3", no_wrap=True)
        table.add_column("Buy Date", justify="center", style="dark_violet", no_wrap=True)
        table.add_column("Buy price", justify="center", style="deep_sky_blue1", no_wrap=True)
        table.add_column("Expiration Date", justify="center", style="deep_sky_blue1", no_wrap=True)
        table.add_column("Amount", justify="center", style="deep_sky_blue1", no_wrap=True)
        
        for row in reader:
           table.add_row(row["id"],
                         row["product_name"], 
                         row["buy_date"],
                         f'€ {row["buy_price"]}', 
                         row["expiration_date"], 
                         row["amount"])
        if table.rows:
           console.print(table)
        else:
            console.print("[i]No data known for this date[/i]") 
make_table_from_bought_csv()








    
