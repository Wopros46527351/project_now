import csvHandler
import scraper
f = open('target.txt', 'r')
while True:
    data = f.readline()
    data = data.replace("\n","")
    if data == "":
        break
    else:
        print(data)
        price,count = scraper.get_info(data)
        input(f"price:{price}\ncount:{count}\nPress ENTER")
        #вызов функции

name = "name1"
data = ['01.01.2201','02.01.2201','03.01.2201']
price = [200,250,300]
counts = [100,80,120]

file = csvHandler.create_csv(data)
csvHandler.write_data(file,name,price,counts)
file.close()