from pytube import YouTube
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


def search(keyword):
    driver_path = os.getcwd()+'/driver/chromedriver'

    options = Options()
    options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36")

    driver = webdriver.Chrome(driver_path, options=options)
    keyword = keyword[:-1] if keyword[-1] == ' ' else keyword
    keyword = (
        keyword.replace(')', '').replace('(', '').replace(',', '').replace('.', '')
        .replace(':', '').replace(';', '').replace(' ', '+'))
    print('\nBusca: ', keyword, end='')
    driver.get(f'https://www.youtube.com/results?search_query=o+que+e+{keyword}')

    user_data = driver.find_elements_by_xpath('//*[@id="video-title"]')
    urls = [i.get_attribute('href') for i in user_data]
    urls = [i for i in urls if i]
    driver.close()
    return urls


def download(order, url):
        try:
            video = YouTube(url)
            path = os.getcwd()+'/downloads'
            if (video.length < 900) and (video.rating > 4.5):
                video.streams.get_by_itag(18).download(path, filename_prefix=f'{order} - ')
                print(video.title, 'Tempo:', video.length, 'Pontuação:', video.rating)
                return 1
            else:
                print('Não atende aos critérios')
                return 0
        except:
            print('Não foi possível baixar')
            return 0