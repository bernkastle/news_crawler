#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 20/03/2019 13:24
# @Author : karl wang
# @Email: karl.wang.1991@gmail.com

from .Http import Http
from bs4 import BeautifulSoup
from website import *


class Crawler:
    @staticmethod
    async def get_news_163():
        async with Http(10) as http:
            data = await http.get('http://money.163.com/')
            soup = BeautifulSoup(data, 'html.parser')
            data_list = wangyi_money_parse(soup)
            print(data_list)
