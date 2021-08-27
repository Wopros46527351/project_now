import csvHandler

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
counts = [100,80,120]

file = csvHandler.create_csv(data)
csvHandler.write_data(file,name,price,counts)
file.close()