import aiohttp
# import aiodns
import asyncio
import selectors
from bs4 import BeautifulSoup as bs
class MyPolicy(asyncio.DefaultEventLoopPolicy):
   def new_event_loop(self):
      selector = selectors.SelectSelector()
      return asyncio.SelectorEventLoop(selector)

async def main():

    async with aiohttp.ClientSession() as session:
        async with session.get('http://python.org') as response:

            # print("Status:", response.status)
            # print("Content-type:", response.headers['content-type'])

            html = await response.text()
            soup = bs(html,'html.parser')
            
            # print(soup.find(class_='skip-link'))
            mainnav = soup.find('nav', id='mainnav')
            # print(mainnav)
            for a in mainnav.find_all('li', class_='tier-1'):
                print(a.a.string)
                
            

asyncio.set_event_loop_policy(MyPolicy())
asyncio.run(main())

