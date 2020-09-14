from time import sleep
from random import randint
from download import search, download


with open('keywords.txt') as keywords:
    for i, keyword in enumerate(keywords):
        urls = search(keyword)
        success = 0
        for url in urls:
            if success < 1:
                success += download(f'{i+1:02}\.{success+1:02}', url)
            else:
                pass
            
