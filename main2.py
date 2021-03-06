import csv
import os
import codecs
import json
import urllib
import urllib.request

class DouyinJsonAnalizer(object):
    def __init__(self):
        pass
        self.jsonPath = r'./Jsons/douyin'
        self.downloadPath = r'./Downloads/douyin'
        self.csvPath = r'./csv/douyin'
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
            medias = self.getMediaObj(self.jsonPath + file)
            if(len(medias) == 0):
                pass
            else:
                for media in medias:
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
        content['duration'] = int(media.get('video').get('duration'))/1000.0       #????????????
        content['author']   = media.get('author').get('nickname')                  #????????????
        content['desc']     = media.get('desc')                                    #????????????
        content['like']     = media.get('statistics').get('digg_count')            #?????????
        content['share']    = media.get('statistics').get('share_count')           #?????????
        content['collect']  = media.get('statistics').get('collect_count')         #?????????
        content['comment']  = media.get('statistics').get('comment_count')         #?????????
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
        myfile = codecs.open(fileName,'r','utf-8-sig')
        myJson=myfile.read()
        try:
            myjson = json.loads(myJson)
        except Exception as e:
            print("Error when parsing json:" + fileName)
            return []
        return myjson.get('aweme_list')


if __name__ == '__main__':
    main = DouyinJsonAnalizer()
    main.run()