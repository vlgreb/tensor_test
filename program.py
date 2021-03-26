import requests
from bs4 import BeautifulSoup

URL = 'https://lenta.ru/news/2021/03/26/molnia/'


class Client:
    pass


class Parser:

    ''' Парсер '''

    def __init__(self, url, *args, **kwargs):
        self.url = url

    def get_html(url, params=None):
        pass
        # r = requests.get(url, params=params)
        # return r

    def get_content(html):
        pass
        # soup = BeautifulSoup(html, 'html.parser')
        # items = soup.find_all('p')
        # for item in items:
        #     string = item.text
        #     link = item.find('a')
        #     print(string)
        #     if link:
        #         print(link)

            # print(item)
            # print(link)


    def parse():
        pass
        # html = get_html(URL)
        # if html.status_code == 200:
        #     get_content(html.text)


P = Parser(URL)
print(P.__doc__)