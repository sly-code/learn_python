import csv

with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Tomato'})

with open('names.csv', newline='') as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
        print(row)
        print(row["first_name"],row["last_name"])

with open('test.csv','w',newline='')as myFile:
    myWriter=csv.writer(myFile,delimiter='|',quoting=csv.QUOTE_NONNUMERIC)
    myWriter.writerow([7,'Ye|Shaoliang'])
    myWriter.writerow([8,'Ye Ting'])
    myList=[[1,2,3],[4,5,6]]
    myWriter.writerows(myList)

with open('test.csv', 'a', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';',quotechar='|', escapechar='\\',quoting=csv.QUOTE_NONE)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Sp|am', 'Lovely;Spam', 'Wonderful Spam'])

with open('test.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';',escapechar='\\', quotechar='|')
    print("total line number of reader is:",spamreader.line_num)
    for row in spamreader:
        for field in row:
            print(field,end=' ')
        print()
    print("total line number of reader is:",spamreader.line_num)

