from datetime import datetime, timedelta

n = datetime.today() - timedelta(5)
input(n.strftime("%d.%m.%Y"))