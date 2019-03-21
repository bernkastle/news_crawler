#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 20/03/2019 18:41
# @Author : karl wang
# @Email: karl.wang.1991@gmail.com

from bs4 import BeautifulSoup


def wangyi_money_parse(text: BeautifulSoup, contents: dict) -> [str]:
    """
    网易新闻首页要闻，评论，点击榜新闻
    :return: 返回新闻列表
    """
    news = []
    for news_type in contents:
        content = contents[news_type]
        title_selector = content['title_selector']
        prop = content['property']
        temp = [x[prop] for x in text.select(title_selector)] if prop else [x.get_text() for x in text.select(title_selector)]
        news.append({news_type: temp})

    return news
