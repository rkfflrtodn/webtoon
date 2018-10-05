# parser.py
import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()

from parsed_data.models import WebtoonData


def parse_webtoon():
    req = requests.get('https://comic.naver.com/webtoon/weekday.nhn/')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.select(
        'content > div.list_area.daily_all > div > div > ul > li > div'
        )
    data = {}
    for title in my_titles:
        data[title.text] = title.get('href')
    return data


if __name__=='__main__':
    blog_data_dict = parse_webtoon()
    for t, l in blog_data_dict.items():
        WebtoonData(title=t, url_img_thumbnail=l).save()