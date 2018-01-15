#coding:utf-8

import http.cookiejar
from bs4 import BeautifulSoup
import re
import urllib.parse

class HtmlParser(object):

    def parser(self, page_url, content):

        if page_url is None or content is None:
            return

        soup = BeautifulSoup(content, "html.parser", from_encoding='utf-8')
        new_url = self._get_new_url(page_url, soup)
        new_datas = self._get_new_datas(page_url, soup)
        return new_url, new_datas

    def _get_new_url(self, page_url, soup):

        new_url = soup.find('div', id="paginator").find('a', class_="next").get('href')
        new_full_url = urllib.parse.urljoin(page_url, new_url)
        return new_full_url


    def _get_new_datas(self, page_url, soup):
        res_datas = set()
        contents = soup.find_all('div', class_="comment-item")
        for content in contents:
            res_datas.add(content.find('div', class_="comment").find('p').get_text())

        return res_datas