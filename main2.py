import csv
import os
import codecs
import json
import urllib
import urllib.request

class Main(object):
    def __init__(self):
        pass
        self.jsonPath = r'./Jsons/'
        self.downloadPath = r'./Downloads/'
        self.csvPath = r'./csv'
        self.csvName = 'Medias.csv'

    def run(self):
        for meida in self.getMediaObjs():
            self.printMeidaContene(self.getContentFromMeida(meida))
            print()

    def getFileList(self):
        return os.listdir(self.jsonPath)

    def getMediaObjs(self):
        mediaList = []
        for file in self.getFileList():
            for media in self.getMediaObj(self.jsonPath + file):
                mediaList.append(media)
        return mediaList
        
    def saveContent2Csv(self,content):
        f = open(self.csvPath+self.csvName,'a',encoding='utf-8',newline="")
        csv_writer = csv.writer(f)
        #header = ['Author', 'Describtion', 'Duration', 'Likes', 'Share', 'Collection', 'Comment']
        #csv_writer.writerow(header)
        line = self.getContentString(content)
        csv_writer.writerow(line)
        f.close()

    def getContentFromMeida(self,media):
        content = {}
        content['duration'] = int(media.get('video').get('duration'))/1000.0      #视频时长
        content['author'] = media.get('author').get('nickname')                   #作者昵称
        content['desc'] = media.get('desc')                                       #视频描述
        content['like'] = media.get('statistics').get('digg_count')               #点赞数
        content['share'] = media.get('statistics').get('share_count')             #分享数
        content['collect'] = media.get('statistics').get('collect_count')         #收藏数
        content['comment'] = media.get('statistics').get('comment_count')         #评论数
        content['url'] = media.get('video').get('play_addr').get('url_list')      #URL
        return content

    def getContentString(self,content):
        return [
                content['author'],
                str(content['duration'])+'s',
                content['desc'],
                str(content['like']),
                str(content['share']),
                str(content['collect']),
                str(content['comment']),
                content['url'][2]
            ]
    
    def printMeidaContene(self,content):
        print("Author      :"+content['author'])
        print("Duration    :"+str(content['duration'])+"s")
        print("Description :"+content['desc'])
        print("Likes       :"+str(content['like']))
        print("Shares      :"+str(content['share']))
        print("Collections :"+str(content['collect']))
        print("Comment     :"+str(content['comment']))
        for i in range(3):
            print("URL"+ str(i) +"       :"+content['url'][i])
        

    def getMediaObj(self,fileName):
        myfile = codecs.open(fileName,'r','UTF-8')
        myJson=myfile.read()
        myjson = json.loads(myJson)
        return myjson.get('aweme_list')


if __name__ == '__main__':
    main = Main()
    main.run()