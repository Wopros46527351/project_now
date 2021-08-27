from bs4 import BeautifulSoup
import requests

def get_info(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    price = soup.find_all("span", {"class":'ordering__value'})[0]
    count = soup.find_all("span", {"class":'item__avail item__avail_available item__avail_float'})[0]
    count_transformed = ""
    for c in count.text:
        if c in "0123456789":
            count_transformed+=c
    print(type(count_transformed))
    count_transformed = float(count_transformed)
    price = float(price.text)
    #print(f"price:{price}")
    #print(f"count:{count_transformed}")
    return (price,count_transformed)

if __name__ == "__main__":
    print("This file is not supposed to be launched by user.Press ENTER to exit")
    input()