#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 20/03/2019 18:41
# @Author : karl wang
# @Email: karl.wang.1991@gmail.com

from bs4 import BeautifulSoup


def wangyi_money_parse(text: BeautifulSoup) -> [str]:
    """
    网易新闻首页要闻，评论，点击榜新闻
    :return: 返回新闻列表
    """
    bbs_rank = [x['title'] for x in text.select('.bbs_ranklist a')]
    top_rank = [x['title'] for x in text.select('.top_ranklist a')]
    top_news = [x['title'] for x in text.select('.top_ranklist a')]

    return top_news + top_rank + bbs_rank
