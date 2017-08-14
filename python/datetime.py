from datetime import datetime
datetime(2012, 5, 1)

# string to datetime
datetime.datetime.strptime('20170430',"%Y%m%d")

# add month
current = datetime.datetime(mydate.year, mydate.month, 1)
six_month_later = datetime.datetime(mydate.year - (mydate.month<6), ((mydate.month-6 ) %12 + 12*(mydate.month==6)), 1)
