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
        self.csvPath = r'./csv/'
        self.csvName = 'Medias.csv'

    def run(self):
        media_contents = []
        for meida in self.getMediaObjs():
            temp_content = self.getContentFromMeida(meida)
            media_contents.append(temp_content)
            self.saveContent2Csv(temp_content)


            

    def getFileList(self):
        return os.listdir(self.jsonPath)

    def getMediaObjs(self):
        mediaList = []
        for file in self.getFileList():
            for media in self.getMediaObj(self.jsonPath + file):
                mediaList.append(media)
        return mediaList
        
    def downloadContent(self,content,filename):
        try:
            print("downloading:"+ videoURL + '\n as :'+ filename +'\n') 
            urllib.request.urlretrieve(videoURL, self.downloadPath + filename)
        except Exception as e:
            print("Error occurred when downloading file from "+ videoURL + ", error message:")
            print(e)

    def saveContent2Csv(self,content):
        fullpath = self.csvPath + self.csvName
        if(not os.path.exists(fullpath)):
            f = open(fullpath,'a',encoding='UTF-8',newline="")
            header = ['Author','Duration','Describtion', 'Likes', 'Share', 'Collection', 'Comment','URL']
            csv_writer = csv.writer(f)
            csv_writer.writerow(header)
            f.close()
        f = open(fullpath,'a',encoding='UTF-8',newline="")
        csv_writer = csv.writer(f)
        line = self.getContentString(content)
        csv_writer.writerow(line)
        f.close()

    def getContentFromMeida(self,media):
        content = {}
        content['duration'] = int(media.get('video').get('duration'))/1000.0       #视频时长
        content['author']   = media.get('author').get('nickname')                  #作者昵称
        content['desc']     = media.get('desc')                                    #视频描述
        content['like']     = media.get('statistics').get('digg_count')            #点赞数
        content['share']    = media.get('statistics').get('share_count')           #分享数
        content['collect']  = media.get('statistics').get('collect_count')         #收藏数
        content['comment']  = media.get('statistics').get('comment_count')         #评论数
        content['url']      = media.get('video').get('play_addr').get('url_list')  #URL
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