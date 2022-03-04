from datetime import datetime, timedelta


n = datetime.today() 
k = datetime.today() - timedelta(days = 1)
l = datetime.today() + timedelta(days = 1)

print('\nYesterday:', k.strftime("%x"), "\nToday:",n.strftime("%x"), '\nTomorrow:', l.strftime("%x")) 