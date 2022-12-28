from bs4 import BeautifulSoup as BS
import requests


URL = "https://shina.kg/category/legkovye/?ysclid=l9tps4bxe4434265291"

HEADERS = {
    'Auser_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.'
}


def get_url(url, params=''):
    req = requests.get(url=url, headers=HEADERS, params=params)
    return req


def get_data(html):
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


def parser_wheels():
    html = get_url(URL)
    data = get_data(html.text)
    return data


parser_wheels()
