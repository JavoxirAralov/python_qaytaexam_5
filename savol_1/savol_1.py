import asyncio
import json
import time
import requests
from celery import Celery

info = Celery(broker='pyamqp://guest@localhost/')

async def send(url: str):
    with open(url + ".json", "w") as f:
        url = requests.get("https://jsonplaceholder.typicode.com/" + url)
        json.dump(url.json(), f, indent=3)
        print(f"{url} done : ")


async def Yild(l: list):
    for i in l:
        yield i


async def main():
    data = [ "photos", "albums", "todos", "posts", "comments","users",]
    async for url in Yild(data):
        time.sleep(1)
        await send(url)

start = time.time()
asyncio.run(main())
print(time.time() - start)