#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 20/03/2019 18:44
# @Author : karl wang
# @Email: karl.wang.1991@gmail.com


import asyncio

import aiohttp


class Http:
    def __init__(self, pool):
        self.sem = asyncio.Semaphore(pool)

    async def __aenter__(self):
        self._session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, *err):
        await self._session.close()
        self._session = None

    async def get(self, url):
        async with self.sem:
            async with self._session.get(url) as resp:
                resp.raise_for_status()
                return await resp.read()
