#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 20/03/2019 18:41
# @Author : karl wang
# @Email: karl.wang.1991@gmail.com

from bs4 import BeautifulSoup
from collections import defaultdict


def get_title(text, prop):
    return [item[prop] for item in text] if prop else [item.get_text() for item in text]


def wangyi_money_parse(text: BeautifulSoup, contents: dict) -> []:
    """
    网易新闻首页要闻，评论，点击榜新闻
    :return: 返回新闻列表
    """
    news_list = defaultdict()
    for news_type in contents:
        content = contents[news_type]
        parent_selector = content['p_selector']
        title_property = content['title_property']
        title_selector = content['title_selector']
        link_selector = content['link_selector']
        link_property = content['link_property']

        if title_selector == link_selector:
            # 重新组合新闻名字和title
            selector = parent_selector + ' ' + title_selector
            news = text.select(selector)
            title = get_title(news, title_property)
            link = [item[link_property] for item in news]
            news_list[news_type] = list(zip(title, link))
        else:
            # 当title和link不在同一位置时，分开抓取
            title_selector = parent_selector + ' ' + title_selector
            link_selector = parent_selector + ' ' + link_selector
            title_content = text.select(title_selector)
            link_content = text.select(link_selector)
            title = get_title(title_content, title_property)
            link = [item[link_property] for item in link_content]
            news_list[news_type] = list(zip(title, link))

    return news_list
