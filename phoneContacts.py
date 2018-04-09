import csv

with open('contacts.csv') as csvDatafile:
    csvReader = csv.reader(csvDatafile)
    for row in csvReader:
        print (row)
        FirstName = row[1]
        LastName = row[2]
        PhoneNumber = row[3]

        print FirstName
        print LastName
        print PhoneNumber
