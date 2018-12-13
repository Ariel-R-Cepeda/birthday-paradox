from dateutil.parser import parse
from datetime import datetime
from random import sample

with open('anon_bdays.csv') as file:
  with open('clean_data.csv','w') as output:
    next(file)
    for row in file:
      date_str=row.split(',')[-1]
      try:
        date=parse(date_str)
      except ValueError:
        print(f'ValueError - omitting: {date_str}')
      else:
        output.write(datetime.strftime(date, '%m/%d') + '/n')

bday_list=[]
with open('clean_data.csv') as bday_file:
  for row in bday_file:
    bday_list.append(row.strip())

def sim_class(n,trials,bdays):
  match=0
  for _ in range(trials):
    chosen=sample(bdays,n)
    if len(chosen) != len(set(chosen)):
      match+= 1
return match/trials

print(sim_class(23, 10000, bday_list))
    
