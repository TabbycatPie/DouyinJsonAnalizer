import csv
import os
import codecs
import json
import urllib
import urllib.request


def get_Json_list():
    Json_list = os.listdir('G:\\aa')
    Jsons = []
    for Json in Json_list:
      myfile = codecs.open('G:\\aa\\'+ Json,'r','UTF-8')
      myJson=myfile.read()
      myjson = json.loads(myJson)
      videojson =(myjson.get('aweme_list'))
    return videojson


def save_data(videoURL,filename):
    filepath = 'G:\\downloads\\'
    try:
      print("downloading:"+ videoURL + '\n as :'+ filename +'\n') 
      urllib.request.urlretrieve(videoURL, filepath + filename)
    except Exception as e:
      print("Error occurred when downloading file from "+ videoURL + ", error message:")
      print(e)

def get_Content(videojson,filename):
    myvideoURL = videojson.get('video').get('play_addr').get('url_list')
    if(len(myvideoURL)!=0):
        save_data(myvideoURL[2],filename)
        
    

mylist = get_Json_list()
for i in range(0,len(mylist)):
    if int(mylist[i].get('video').get('duration'))>30000:
        dur = int(mylist[i].get('video').get('duration'))/1000.0      #视频时长
        author_nickname = mylist[i].get('author').get('nickname')     #作者昵称
        desc = mylist[i].get('desc') 
        like = mylist[i].get('statistics').get('digg_count')          #点赞数
        share = mylist[i].get('statistics').get('share_count')        #分享数
        collect = mylist[i].get('statistics').get('collect_count')    #收藏数
        comment = mylist[i].get('statistics').get('comment_count')    #评论数
        video_url = mylist[i].get('video').get('play_addr').get('url_list') #URL
        print("Author     :"+ author_nickname)
        print("Describtion:"+ desc)
        print("Duration   :"+ str(dur) + 's')
        print("Likes      :"+ str(like))
        print("Share      :"+ str(share))
        print("Collection :"+ str(collect))
        print("Comment    :"+ str(comment))
        f = open('./video.csv','a',encoding='utf-8',newline="")
        csv_writer = csv.writer(f)
        #header = ['Author', 'Describtion', 'Duration', 'Likes', 'Share', 'Collection', 'Comment']
        #csv_writer.writerow(header)
        line = [author_nickname,desc,str(dur) + 's',str(like),str(share),str(collect),str(comment)]
        csv_writer.writerow(line)
        f.close()
        #get_Content(mylist[i],str(i)+'.mp4')