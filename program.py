import os
import sys

import requests
from bs4 import BeautifulSoup


MAXLENGTH = 80  # максимальная длина строки выходного файла


class Parser:

    def __init__(self, url, tag='p'):
        self.html = requests.get(url)
        self.tag = tag
        self.article = ''

    def get_content(self):
        soup = BeautifulSoup(self.html.text, 'html.parser')
        title = soup.find('h1')
        self.article = f'{Parser.convert(title.text)}\n\n'  # сохраняем заголовок
        items = soup.find_all(self.tag)  # ищем блоки по тэгам из параметов
        for item in items:
            link = item.find('a')
            if link and link.get('href')[:4] == 'http':  # проверяем, что ссылка внешняя
                item.a.replace_with(f'{link.text} [{link.get("href")}]')
            string = item.text
            self.article = f'{self.article}{Parser.convert(string)}\n\n'

    def parse(self):
        if self.html.status_code == 200:
            self.get_content()
            return self.article

    @staticmethod
    def convert(text):
        ''' Функция форматирует текст: длина строки не более MAXLENGTH,
        абзацы и заголовки отбиваются пустой строкой '''
        output_text = ''  # записываем сюда новую строку
        c = 0  # счётчик символов с строке
        for i in text.split():  # проходим по каждому слову
            c += len(i)  # прибавляем длину слова
            if c + 1 > MAXLENGTH:  # если символов больше максимума
                output_text += '\n'  # перенос строки
                c = len(i)  # счётчик равен первому слову в строке
            elif output_text != '':  # условие, чтобы не ставить пробел перед 1-м словом
                output_text += ' '  # ставим пробел после непоследнего слова в строке
                c += 1  # учитываем его в счётчике
            output_text += i  # прибавляем слово
        return output_text  # возвращаем новый текст


def make_path(url):
    path = f'{os.getcwd()}{url[7:]}'  # создаем путь, отбрасывая https:\\
    os.makedirs(path)
    return path.replace('/', '\\')


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Недостаточно параметров')
        sys.exit(1)
    URL = sys.argv[1]
    tag = sys.argv[2]
    article = Parser(URL, tag)
    with open(f'{make_path(URL)}index.txt', 'w') as f:
        f.write(article.parse())
