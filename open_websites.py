from selenium import webdriver
from time import sleep
import os


def open_chromium(name):
    with open(f'out/{name}Links.txt') as f:
        for i in f:
            chrome = webdriver.Chrome()
            chrome.get(i)
            sleep(10)


def open_chrome(name):
    with open(f'out/{name}Links.txt') as f:
        for i in f:
            print(f'chrome {i}')
            os.system(f'chrome {i}')


if __name__ == '__main__':
    open_chrome('amorphous metal')
