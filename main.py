import csvHandler
import scraper
import bd
import datetime
f = open('target.txt', 'r')
while True:
    data = f.readline()
    data = data.replace("\n","")
    if data == "":
        break
    else:
        print(data)
        price,count,name = scraper.get_info(data)
        #input(f"name:{name}\nprice:{price}\ncount:{count}\nPress ENTER")
        #вызов функции
        db = bd.connect_db()
        print(str(datetime.datetime.now().strftime("%d-%m-%Y")))
        #bd.make_push(db, name, str(datetime.datetime.now().strftime("%d-%m-%Y"), )

name = "name1"
data = ['01.01.2201','02.01.2201','03.01.2201']
price = [200,250,300]
counts = [100,80,120]

file = csvHandler.create_csv(data)
csvHandler.write_data(file,name,price,counts)
file.close()