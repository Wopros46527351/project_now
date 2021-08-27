import csvHandler
import scraper
import bd
import datetime
f = open('target.txt', 'r')
db = bd.connect_db()
date = str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
while True:
    data = f.readline()
    data = data.replace("\n","")
    if data == "":
        break
    else:
        print(data)
        price,count,name = scraper.get_info(data)
        #вызов функции
        bd.make_push(db, name, date, count, price, data)
        print(f"name:{name}\nprice:{price}\ncount:{count}\nPress ENTER")
bd.push_meta(db, date)
dates = bd.get_dates(db)
urls = bd.get_urls(db)
print(dates, urls)



file = csvHandler.create_csv(dates)
for url in urls:
    result = bd.make_pull(db, url)
    csvHandler.write_data(file, result["product_name"], result["product_price"], result["product_number"],dates,result['date'])
#csvHandler.write_data(file,name,price,count)
file.close()