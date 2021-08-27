
def create_csv(dates):
    file = open("result.csv","w",encoding='utf-8')
    file.write("Name,")
    file.write("Price/Count,")
    for date in dates:
        file.write(f"{date},")
    else:
        file.write("\n")
    return file

def write_data(file,name,prices,counts):
    file.write(f"{name},")
    file.write(f"Price,")
    for price in prices:
        file.write(f"{price},")
    else:
        file.write("\n")
    file.write(f"Count,")
    for count in counts:
        file.write(f"{count},")
    else:
        file.write("\n")
            
if __name__ == "__main__":
    print("This file is not supposed to be launched by user.Press ENTER to exit")
    input()