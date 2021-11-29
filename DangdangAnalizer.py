import csv
import os
import codecs
import json
import urllib
import urllib.request

class DangdangSpider(object):
    def __init__(self):
        pass
        self.jsonPath = r'./Jsons/dangdang'
        self.downloadPath = r'./Downloads/dangdang'
        self.csvPath = r'./csv/dangdang'
        self.csvName = 'dangdang.csv'


if __name__ == '__main__':
    main = DouyinJsonAnalizer()
    main.run()