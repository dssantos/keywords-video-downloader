from time import sleep
from random import randint
from download import search, download


with open('keywords.txt') as keywords:
    for i, keyword in enumerate(keywords):
        urls = search(keyword)
        success = 0
        for url in urls:
            if success < 2:
                success += download(f'00{i+1}{success+1}', url)
            else:
                pass
            
