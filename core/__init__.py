#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 20/03/2019 13:24
# @Author : karl wang
# @Email: karl.wang.1991@gmail.com

import aiohttp
import asyncio


class Http:
    def __init__(self, pool):
        self.sem = asyncio.Semaphore(pool)

    async def __aenter__(self):
        self._session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, *err):
        await self._session.close()
        self._session = None

    async def fetch(self, url):
        async with self.sem:
            async with self._session.get(url) as resp:
                resp.raise_for_status()
                return await resp.read()


class CrawlerFactory:
    @staticmethod
    def get_crawler(website: str):
        pass


async def main():
    async with Http(2) as http:
        print(await asyncio.gather(http.fetch('http://www.qq.com'), http.fetch('http://www.baidu.com')))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
