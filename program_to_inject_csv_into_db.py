import re
import csv
import sqlite3
database_connection = sqlite3.connect('assembly_performance_updated.db')
database_cursor = database_connection.cursor()
file = open('new_csv_EC_01_title.csv', 'r')
dataset_csv = csv.reader(file)
dataset_csv = list(dataset_csv)
i = 0
while i != 9563:
    data = dataset_csv[i][0]
    if re.search("^Detail", data):
        detail = data
        title = title = dataset_csv[i+1][0]
        i = i+2
    elif data == "ID":
        i = i+1
        flag = 0
    else:
        if flag == 0:
            ec = dataset_csv[i][9]
            print(dataset_csv[i])
            flag=1
        else:
            dataset_csv[i][9] = ec
            print(dataset_csv[i])
        database_cursor.execute("INSERT INTO wallsystem2 (detail,id,name,component,thickness,conductivity,nominalResistance,density,specificHeat,individualEC,totalEC,assemblyTotalEC) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", (
            detail.split(" ")[1], dataset_csv[i][0], title, dataset_csv[i][1], dataset_csv[i][2], dataset_csv[i][3], dataset_csv[i][4], dataset_csv[i][5], dataset_csv[i][6], dataset_csv[i][7], dataset_csv[i][8], dataset_csv[i][9]))
        database_connection.commit()
        i = i+1
#database_connection.close()
