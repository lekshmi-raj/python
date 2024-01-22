import csv
with open('dipr.csv',newline='')as csvfile:
   data=csv.DictReader(csvfile)
   print("ID Department Name")
   print("___________________")
   for row in data:
    print(row['department_id'],row['department_name'])
