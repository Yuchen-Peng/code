from datetime import datetime
datetime(2012, 5, 1)

# string to datetime
datetime.datetime.strptime('20170430',"%Y%m%d")

# datetime to string
current = datetime.datetime(2017, 7, 31, 0, 0)
current_str = current.strftime("%Y-%m-%d") 

# add month
current = datetime.datetime(mydate.year, mydate.month, 1)
six_month_before = datetime.datetime(mydate.year - (mydate.month<6), ((mydate.month-6 ) %12 + 12*(mydate.month==6)), 1)
