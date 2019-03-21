#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 21/03/2019 16:25
# @Author : karl wang
# @Email: karl.wang.1991@gmail.com

from functools import partial
import yaml


def _load_config(website: str):
    with open(f'config/{website}.yaml', 'r', encoding='utf-8') as configs:
        return yaml.load(configs)['news']


load_config_wangyi = partial(_load_config, website='wangyi')
