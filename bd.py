from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("mongodb+srv://Biba_buba_13:Vgfgh4335RTF@huyaster.bi6ms.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test
# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
pprint(serverStatusResult)


def make_push(db,product_name, date, product_number, product_price, url):
    """make push into database

    Args:
        product_name (str): name of the product
        date (str): date of request
        product_number (float): quantity of the product
        product_price (float): current price
        url (str): just url

    Returns:
        Nothing
    """
    if db.product_mstator.find({'url':url}).count()==0:
        push = {
            "product_name": product_name,
            "date": [date],
            'product_number': [product_number],
            'product_price': [product_price],
            'url': url
        }
        db.product_mstator.insert_one(push)
    else:
        db.product_mstator.update_one({'url':url},{'$push': {
            'date':date,
            'product_number':product_number,
            'product_price':product_price
        }})
    return None


def make_pull(db,url):
    """make pull request from database

    Args:
        url (str): url of the product
    Returns:
        result (dict): data about the product
    """
    result = db.product_mstator.find_one({"url":url})
    return result

def push_date(db,date):
    if db.meta.find({'name':"dates"}).count()==0:
        db.meta.insert_one({'name':"dates",'dates':[date]})
    else:
        db.meta.update_one({'name':"dates"},{"$push":{'dates':date}})

def connect_db():
    client = MongoClient("mongodb+srv://admin:admin@arttechtestcluster.d7bmu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.test
    return db 
"""   
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

"""

    




