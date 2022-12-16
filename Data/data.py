import datetime

d = datetime.date(2001, 9, 11)
tday = datetime.date.today()
print(tday, d)

tdelta = datetime.timedelta(hours=12)
print(tday + tdelta)