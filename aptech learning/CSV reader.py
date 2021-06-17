import csv
def show():
    record=[{'id':'1','firstname':'neha','lastname':'dhanu'},
            {'id':'2','firstname':'arjun','lastname':'kumar'},
            {'id':'3','firstname':'ram','lastname':'sharma'},
            {'id':'4','firstname':'raju','lastname':'sharma'}]
    csv_writer=csv.writer(open('myrecord.csv','w'),delimiter=',')
    csv_writer.writerow(['id','firstname','lastname'])
    for re in record:
        csv_writer.writerow([re['id'], re['firstname'], re['lastname']])
show()