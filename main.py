import csv

f = open('target.txt', 'r')
while True:
    data = f.readline()
    data.replace("\n","")
    if data == "":
        break
    else:
        print(data)
        #вызов функции

name = "name1"
data = ['01.01.2201','02.01.2201','03.01.2201']
price = [200,250,300]
count = [100,80,120]