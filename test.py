from datetime import date, datetime, timedelta

d = date.today()
dt = datetime.today()

# delta = timedelta(days=5)
# d_final = d - delta

d_str = d.strftime("%d %b %Y")

