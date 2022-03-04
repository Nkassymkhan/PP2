from datetime import timedelta, datetime

n = datetime.today()

k = datetime.today() - timedelta(days = 5)

l = (n - k).total_seconds()

print(l)