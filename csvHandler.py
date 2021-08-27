def create_csv(dates):
    """Creates csv file with set data string on top

    Args:
        dates (array): array of dates in file

    Returns:
        file: csv text file
    """
    file = open("result.csv","w",encoding='utf-8')
    file.write("Name,")
    file.write("Price/Count,")
    for date in dates:
        file.write(f"{date},")
    else:
        file.write("\n")
    return file

def write_data(file,name,prices,counts,dates_all,dates_product):
    """writes data to file

    Args:
        file (file): csv file to write to
        name (str): name of product
        prices (array): int array of prices
        counts (array): int array of counts
    """
    name = name.replace(',', '.')
    file.write(f"{name},")
    file.write(f"Price,")
    index =0
    for date in dates_all:
        if dates_product[index] == date:
            file.write(f"{prices[index]},")
            index+=1
    else:
        file.write("\n")
    file.write(f",")
    file.write(f"Count,")
    index =0
    for date in dates_all:
        if dates_product[index] == date:
            file.write(f"{counts[index]},")
            index+=1
    else:
        file.write("\n")    
            
if __name__ == "__main__":
    print("This file is not supposed to be launched by user.Press ENTER to exit")
    input()