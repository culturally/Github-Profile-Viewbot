import asyncio
import aiohttp
import requests
import os
import sys
from os import system
from colorama import Fore, Back, Style

attempts=0
banner = '              zeeeeee-\n            z$$$$$$"\n           d$$$$$$"\n          d$$$$$P\n         d$$$$$P\n        $$$$$$"\n      .$$$$$$"\n     .$$$$$$"\n    4$$$$$$$$$$$$$"\n   z$$$$$$$$$$$$$"\n   """""""3$$$$$"\n         z$$$$P\n        d$$$$"\n      .$$$$$"\n     z$$$$$"\n    z$$$$P\n   d$$$$$$$$$$"\n  *******$$$"\n       .$$$"\n      .$$"\n     4$P"\n    z$"\n   zP\n  z"'

if sys.version_info[0] < 3:
	pyversion = python_version()
	print("Alert! Your python version is %s. Use python version 3> to run this code" %(pyversion))
	exit(1)

async def SentViews(session):
    try: 
        system("title " + f"Sent ~ {attempts}")
        async with session.get(url=f"https://gpvc.arturio.dev/{user}", verify_ssl=False) as response:
            if response.status == 429:
                print(Fore.RED + f'Rate Limit ~ Attempts: [{attempts}]')
            elif response.status == 200:
                print(Fore.WHITE + "[" + Fore.MAGENTA + "+" + Fore.WHITE + "]" + Fore.MAGENTA + f'Sent')
            else:
                print(response.status)
    except Exception:
        system("title " + f"Attempts ~ {attempts}")
        #print(response.status)
        print(Fore.RED + 'Something Went Wrong!')


async def StartThreads(threads):
    async with aiohttp.ClientSession() as session:
        tasks = []
        global attempts
        for _ in range(threads):
            attempts+= 1
            task = asyncio.ensure_future(SentViews(session))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == "__main__":
    os.system('cls||clear')
    system("title " + "t.me/undecryptable")
    print(Fore.MAGENTA + banner)
    print(Fore.CYAN + '          User')
    print('')
    print('')
    user = input(Fore.MAGENTA+" root" + Fore.WHITE+"@" + Fore.MAGENTA +"yin" + Fore.WHITE+":" + Fore.CYAN+"~" + Fore.WHITE+" ")
    os.system('cls||clear')
    print(Fore.MAGENTA + banner)
    print(Fore.CYAN + '          Threads')
    print('')
    print('')
    threads = int(input(Fore.MAGENTA+" root" + Fore.WHITE+"@" + Fore.MAGENTA +"yin" + Fore.WHITE+":" + Fore.CYAN+"~" + Fore.WHITE+" "))
    os.system('cls||clear')
    print(Fore.MAGENTA + banner)
    print(Fore.CYAN + '          Ready?(1)')
    print('')
    print('')
    ready = int(input(Fore.MAGENTA+" root" + Fore.WHITE+"@" + Fore.MAGENTA +"yin" + Fore.WHITE+":" + Fore.CYAN+"~" + Fore.WHITE+" "))
    if int(ready) == 1:
        while True:
            asyncio.get_event_loop().run_until_complete(StartThreads(int(threads)))

