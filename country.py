import requests
from bs4 import BeautifulSoup
import json

URL = "http://ostranah.ru/_lists/capitals.php"
URL2 = "https://kakdobratsyado.ru/stolitsy-stran-mira-spisok-po-alfavitu-flagi-strany-stolitsy/"
HOST = 'http://ostranah.ru/'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 YaBrowser/21.3.2.193 Yowser/2.5 Safari/537.36'

}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


country_list = []
country_list2 = []


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')

    table = soup.find_all('table')[0]

    for countries in table:
        country_list.append(countries.text.strip().split(' '))

    print(country_list)

    with open("data.json", "w") as json_file:
        json.dump(country_list, json_file, indent=5, ensure_ascii=False)

    # for cousss in table:
    #     country_list2.append({
    #         'link': cousss.find('a').get('href'),
    #
    #     })
    # print(country_list2)
    #
    # films = []
    # for item in table:
    #     films.append({
    #         'link': HOST + item.find('a').get('href')
    #
    #     })
    # print(films)


def parse():
    html = get_html(URL)
    get_content(html.text)
    #print(html.text)


parse()

