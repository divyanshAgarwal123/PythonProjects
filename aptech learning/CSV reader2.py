import csv
row_list=[["SN","Name","CONTRIBUTION"],
          [1,"arjun","linux cernel"],
          [2,"ram","WWW"],
          [4,"raju","Python programming"]
          ]
with open('my recorder.csv','w',newline='')as file:
    writer=csv.writer(file)
    writer.writerow(row_list)