import csv
import os
import codecs
import json
import urllib
import urllib.request
from bs4 import BeautifulSoup
import lxml
import time


class DangdangSpider(object):
    def __init__(self):
        pass
        self.jsonPath = r'./Jsons/dangdang'
        self.downloadPath = r'./Downloads/dangdang'
        self.csvPath = r'./csv/dangdang'
        self.csvName = 'dangdang.csv'

    def getHtmlSoup(self,url):
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html.read(),'lxml')
        return soup

    def getBookinfo(self,book):
        try:
            mybook = {}
            div = book.find_all('div',class_ = 'name')
            bookname = div[0].find_all('a')[0]['title']
            mybook['name'] = bookname
            return mybook
        except Exception as e:
            print('getBookinfo() Error:')
            print(e)
            return None 

    def printBookinfo(self,mybook):
        mystr = ''
        mystr = mystr + 'Name     :' + mybook['name'] + '\n'
        return mystr
    
    def getTotalPage(self,soup):
        try:
            divs = soup.find_all('div',class_ = 'data')
            pagestr = divs[0].find_all('span')[1].string
            pagestr = pagestr.replace('/','')
            print('Total pages  :' + pagestr)
            return int(pagestr)
        except Exception as e:
            print("Can not get page info from url.")
            print(e)
            return 0

    def run(self):
        #get total page num
        url_base = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent30-0-0-1-'
        url = url_base + '1'
        soup = self.getHtmlSoup(url)
        total_page = self.getTotalPage(soup)
        #get all books and out put
        book_found = 0
        for i in range(1,total_page):
            print('Get html from:'+ url)
            try:
                ullist = soup.find('ul',attrs = {'class':'bang_list clearfix bang_list_mode'})
                booklist = ullist.find_all('li')
                for book in booklist:
                    book_found = book_found + 1
                    try:
                        print(str(book_found) + '.' + self.printBookinfo(self.getBookinfo(book)))
                        print('*'*60)
                    except Exception as e:
                        book_found = book_found - 1
                        continue
            except Exception as e:
                print('Can not get info from soap,Error:')
                print(e)
            #go to next page
            i = i + 1
            url = url_base + str(i)
            #time.sleep(5) #aviod trigger anti-bot
            soup = self.getHtmlSoup(url)


if __name__ == '__main__':
    main = DangdangSpider()
    main.run()