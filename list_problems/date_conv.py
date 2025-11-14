""" 
  
"""
from datetime import datetime
from typing import Any

def time_format_convert(datestr:Any):
    """this a 12 hour to 24 hour format convert   """
    fmt="%I:%M%p"
    date=datetime.strptime(datestr,fmt)
    print(datetime.strftime(date,"%H:%M"))

if __name__=='main':
    Date_Str:str
    Date_Str=input("get a input of 12 hour format")
    time_format_convert(Date_Str)




   

