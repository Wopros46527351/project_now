
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("mongodb+srv://Biba_buba_13:Vgfgh4335RTF@huyaster.bi6ms.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test
# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
pprint(serverStatusResult)

#тут подтягиваем в переменные данные
product_name='rere'
date='02.07.2021'
product_number=122
product_price=202


#ниже не трогать.оно работает
result = db.product_mstator.find_one({'product_name':product_name})

if result==None:
    business = {
        'product_name': product_name,
        'date': [],
        'product_number': [],
        'product_price': []
    }
    db.product_mstator.insert_one(business)


db.product_mstator.update_one({'product_name':product_name },  {'$push': {'date' :date}})
db.product_mstator.update_one({'product_name':product_name }, {'$push': {'product_number':product_number}}) 
db.product_mstator.update_one({'product_name':product_name }, {'$push': {'product_price':product_price}})



    



