#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 20/03/2019 18:56
# @Author : karl wang
# @Email: karl.wang.1991@gmail.com

import asyncio

from core.Crawler import Crawler

if __name__ == '__main__':
    data = Crawler.get_news_163()
    print(data)
