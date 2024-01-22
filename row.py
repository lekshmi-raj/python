import csv
with open('emp.csv',newline='')as csvfile:
   data=csv.reader(csvfile, delimiter=' ',quotechar='|')
   for row in data:
       print(','.join(row))
