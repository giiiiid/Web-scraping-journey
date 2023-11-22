import requests
from bs4 import BeautifulSoup

def name_and_price():
    products = []
    price_list = []

    store_url = 'https://www.wilkinsonsword.com/'
    response = requests.get(store_url)

    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    product_name = soup.find_all('div', class_='ProductItem__Info ProductItem__Info--center')
    for i in product_name:
        products.append(i.h2.a.text)

    ## Pricing ##
    try:
        first_product = product_name[0]
        main_div = first_product.find('div', class_='ProductItem__PriceList Heading')
        first_product_price = main_div.find('span', class_='ProductItem__Price Price')
        price_list.append(first_product_price.text)

        second_product = product_name[1]
        main_div = second_product.find('div', class_='ProductItem__PriceList Heading')
        second_product_price = main_div.find('span', class_='ProductItem__Price Price')
        price_list.append(second_product_price.text)

        third_product = product_name[2]
        main_div = third_product.find('div', class_='ProductItem__PriceList Heading')
        third_product_price = main_div.find('span', class_='ProductItem__Price Price')
        price_list.append(third_product_price.text)

        fourth_product = product_name[3]
        main_div = fourth_product.find('div', class_='ProductItem__PriceList Heading')
        fourth_product_price = main_div.find('span', class_='ProductItem__Price Price')
        price_list.append(fourth_product_price.text)

    except IndexError:
        print('No more products')
    
    
    # if __name__ == '__main__':
    #     name_and_price()

    arr = {}
    for i in products:
        for j in price_list:
            arr[i] = j
    print(arr)

name_and_price()
