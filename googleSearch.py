import requests as req
from bs4 import BeautifulSoup
import re


class Search:
    def __init__(self, links):
        for i in range(len(links)):
            links[i] = links[i][7:]
        self.links = links

    @classmethod
    def fromWebpage(cls, htmlCode):

        # htmlCode = cls.remove_tags(htmlCode)
        # print(htmlCode)
        try:
            soup = BeautifulSoup(htmlCode, 'html.parser')
            cls.remove_tags(soup)
            hs = soup.find_all('h3')
            links = []
            for i in hs:
                links.append(i.parent['href'])
            return cls(links)

        except(Exception):
            with open('out/webpage.log', 'w') as f:
                f.write(soup.prettify())

    @classmethod
    def fromSearchElement(cls, search, site):
        htmlCode = cls.googleSearchHTML(search, site)
        return cls.fromWebpage(htmlCode)

    @staticmethod
    def googleSearchHTML(search, site):
        url = f"https://www.google.com/search?q={search} site:{site}"
        return req.get(url).text

    @staticmethod
    def remove_tags(soup):
        # soup = BeautifulSoup(htmlCode, 'html.parser')
        # parse html content
        for data in soup(['style', 'script']):
            # Remove tags
            data.decompose()

        # return data by retrieving the tag content
        # return ' '.join(soup.stripped_strings)


def search_main(search):
    obj = Search.fromSearchElement(search, 'technologyreview.com')
    with open(f'out/{search}Links.txt', 'w') as f:
        for i in obj.links:
            f.writelines(i+'\n')


if __name__ == '__main__':
    search = 'amorphous metal'
    search_main(search)
