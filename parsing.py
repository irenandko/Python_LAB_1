import requests
from bs4 import BeautifulSoup
import pandas as pd

df = {"Address": ['']}

def parsing():
    url = 'https://gorkvartira.ru/city/omsk'
    response = requests.get(url)
    print(response.status_code)

    soup = BeautifulSoup(response.text, "html.parser")
    block = soup.findAll('div', class_ = 'adv')

    for data in block:
        flat_address = data.find('a', class_="java black bigger11").text
        print(flat_address)
        df['Address'].append(flat_address)

    data_dict = pd.DataFrame(df)
    data_dict.to_excel("result.xlsx")