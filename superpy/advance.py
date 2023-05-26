import datetime
import calendar

# this file contains all the functions related to teh advance subparser and date in general

# this function advances the date in the currentDate file by the number of days pased in CLI 
def advance_time(day=0):
    date_today = datetime.date.today()
    advanced_date = date_today +  datetime.timedelta(days = day)
    with open("currentDate.txt", "w") as file:
            file.write(advanced_date.strftime("%Y-%m-%d"))

# this function sets the date in currentDate file to the date of today
def set_date_today():
      with open("currentDate.txt", "w") as file:
            date_today= datetime.date.today()
            file.write(date_today.strftime("%Y-%m-%d"))

# this function fetches date of today
def get_date_now():
     return datetime.date.today().strftime("%Y-%m-%d")

# this function fetches the date of yesterday based on the date in currentDate file
def get_date_yesterday():
      current_date = get_date_file()
      yesterday_date = datetime.datetime.strptime(current_date, "%Y-%m-%d") - datetime.timedelta(days = 1)
      return yesterday_date.strftime("%Y-%m-%d")

# this function fetches the date in currentDate file
def get_date_file():
      with open("currentDate.txt", "r") as f:
            for line in f.readlines():
                return line

""" this function returns the format the passed date is in, if the passed date is 
not formatted in the allowed formats %Y-%m-%d, %Y-%m or %Y a ValueError is raised """
def get_date_Format(date):     
    try:
      if date == datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d"):
            return "%Y-%m-%d"
    except ValueError:
      try:
          if date == datetime.datetime.strptime(date, "%Y-%m").strftime("%Y-%m"):
            return "%Y-%m"
      except ValueError:
           try:
               if date == datetime.datetime.strptime(date, "%Y").strftime("%Y"):
                  return "%Y"
           except ValueError:
                raise ValueError("format must be 'YYYY-MM-DD', 'YYYY-MM' or 'YYYY'")

# this function converts month number into the written form and return for example the string "May 2023"
def get_month(date):
     date_format = get_date_Format(date)
     if date_format == "%Y-%m":
        month = int(datetime.datetime.strptime(date, "%Y-%m").strftime("%m").lstrip("0").replace(" 0", " "))
        year = datetime.datetime.strptime(date, "%Y-%m").strftime("%Y")
        return calendar.month_name[month] +" " + year
     else:
          return date
                  
        
