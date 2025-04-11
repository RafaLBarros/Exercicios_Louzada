import os
import time as t
import datetime as dt
import calendar as c

now = dt.datetime.now()
print("Diretório atual:",os.getcwd())
print("Mês atual:\n",c.month(now.year,now.month))
print("Data e Hora atual:",now)
print("Agora esperarei 3 segundos para dizer a data e hora de novo.")
t.sleep(3)
print("Data e Hora atual:",dt.datetime.now())