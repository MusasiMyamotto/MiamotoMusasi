from bs4 import BeautifulSoup as BS
import requests

class ParserWheels:
    __URL = "https://shina.kg/category/legkovye/?ysclid=l9tps4bxe4434265291"

    __HEADERS = {
                'Auser_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.'
    }

    @classmethod
    def __get_url(cls, url=None, params=''):
        if url is not None:
            req = requests.get(url=url, headers=cls.__HEADERS, params=params)
        else:
            req = requests.get(url=cls.__URL, headers=cls.__HEADERS)
        return req

    @staticmethod
    def __get_data(html):
        soup = BS(html, "html.parser")
        items = soup.find_all("div", class_="pl-item-wrapper")
        wheels = []

        for item in items:
            title = item.find("div", class_="pl-item-info-expandable").find("a").getText().split(" ")
            wheels.append({
                "link": f"https://shina.kg{item.find('a').get('href')}",
                "size": title[1],
                "logo": title[2],
                "price": item.find("div", class_="price-wrapper").find("span").getText()

            })
        return wheels


    @classmethod
    def parser(cls):
        html = cls.__get_url()
        if html.status_code == 200:
            anime = []
            for i in range(1, 2):
                html = cls.__get_url(f"{cls.__URL}page/{i}/")
                current_page = cls.__get_data(html.text)
                anime.extend(current_page)
            return anime
        else:
            raise Exception("Bad request!")


ParserWheels()
