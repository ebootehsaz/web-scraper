# Import the required libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
# import sqlite3
# from sent_analysis import performSentimentAnalysis


        

def scrape_stock_info(stock, url):
    # Start a Selenium web driver
    driver = webdriver.Chrome()

    # Retrieve the website's HTML content
    driver.get(url + stock)

    # Minimize the window
    driver.minimize_window()

    # Parse the HTML using BeautifulSoup
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

     # Extract the data from the website
    stock_data = soup.find_all("dd")

    data = []

    for item in stock_data:
        # print(item.get("data-test"))
        # print((item.get("span")), "\n")
        arr = item.find_all("span")
        if len(arr) > 1:
            data.append((arr)[1].text)


    # Close the web driver
    driver.close()

    # return data
    return data


def get_data_types(stock, url):
     # Start a Selenium web driver
    driver = webdriver.Chrome()

    # Retrieve the website's HTML content
    driver.get(url + stock)

    # Minimize the window
    driver.minimize_window()

    # Parse the HTML using BeautifulSoup
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    # Extract the data from the website
    stock_data = soup.find_all("dd")

    data = []
    for item in stock_data:
        data.append(item.get("data-test"))
    return data


def get_stock_links(url):
    # Start a Selenium web driver
    driver = webdriver.Chrome()
    
    driver.minimize_window()

    # Retrieve the website's HTML content
    driver.get(url)

    # Minimize the window
    

    html = driver.page_source

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

     # Extract the data from the website
    # stock_data = soup.find_all("div", {"class": "stock-data"})
    # stock_data = soup.find_all("td", {"class": "bold left noWrap elp plusIconTd"})
    stock_data = soup.find_all("td", {"class": "bold left noWrap elp plusIconTd"})
    data = []
    with open("stock_links.txt", "w") as file:
        for stock in stock_data:
            data.append(stock.find("a").get("href"))
            file.write(data[-1])
            file.write("\n")

    return data


def main():
    site = "https://www.investing.com"
    url = "https://www.investing.com/equities/"

    # only need to run once to put links in file
    # for stock in get_stock_links(url):
    get_stock_links(url)
    #     break

    i = 0
    with open("stock_links.txt", "r") as txtFile:
        with open("stock_data.csv", "w") as csvFile:
            writer = csv.writer(csvFile)

            stock = txtFile.readline()
            # print(stock)
            data_types = get_data_types(stock, "https://www.investing.com")
            stock_info = scrape_stock_info(stock, "https://www.investing.com")

            writer.writerow(data_types)
            writer.writerow(stock_info)


            for stock in txtFile:
                stock_info = scrape_stock_info(stock, "https://www.investing.com")
                print(stock_info)
                writer.writerow(stock_info)
                i += 1
                if i == 3:
                    return 

        


    




if __name__ == "__main__":
    print("running main.py")
    main()
