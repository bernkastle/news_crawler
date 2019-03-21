#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 20/03/2019 13:24
# @Author : karl wang
# @Email: karl.wang.1991@gmail.com

from website import *
from .Http import Http
import asyncio
from .LoadConfig import *


class Crawler:
    @staticmethod
    def get_news_163():
        configs = load_config_wangyi()
        tasks = [Crawler._get_news_163(configs[config]) for config in configs]
        loop = asyncio.get_event_loop()
        data = loop.run_until_complete(asyncio.gather(*tasks))
        return data

    @staticmethod
    async def _get_news_163(config: dict):
        name = config['name']
        url = config['url']
        contents = config['contents']
        async with Http(10) as http:
            data = await http.get(url)
            soup = BeautifulSoup(data, 'html.parser')
            data_list = wangyi_money_parse(soup, contents)
            return {name: data_list}
