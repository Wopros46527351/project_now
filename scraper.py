from bs4 import BeautifulSoup
import requests

def get_info(url):
    """Gets CHIPDIP data from URL

    Args:
        url (str): url of product

    Returns:
        tuple: current price,count and name
    """
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    price = soup.find_all("span", {"class":'ordering__value'})[0]
    count = soup.find_all("span", {"class":'item__avail item__avail_available item__avail_float'})[0]
    name = soup.find("h1", itemprop='name')
    name = name.text.replace(",",".")
    count_transformed = ""
    for c in count.text:
        if c in "0123456789":
            count_transformed+=c
    count_transformed = float(count_transformed)
    price = float(price.text)
    return (price,count_transformed,name)

if __name__ == "__main__":
    print("This file is not supposed to be launched by user.Press ENTER to exit")
    input()