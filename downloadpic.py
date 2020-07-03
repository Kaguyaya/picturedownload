#-*- coding:utf-8 -*-
import re
import requests
def downloadpic(html,keyword):
    i=0
    t=0  
    pic_url=re.findall('"objURL":"(.*?)",',html,re.S)
    print("找到关键字:",keyword,"的图片，现在开始下载...")
    for each in pic_url:
        print("正在下载第",str(t+1),"张图片,图片地址:"+str(each))
        t+=1
        try:
            pic=requests.get(each,timeout=5)
        except requests.exceptions.ConnectionError:
            print ('【错误】当前图片无法下载')
            continue
        string='pictures\\'+str(i)+'.jpg'
        fp=open(string,'wb')
        fp.write(pic.content)
        fp.close()
        i+=1


if __name__=='__main__':
    word=input("请输入关键字: ")
    url='https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=detail&fr=&hs=0&xthttps=111111&sf=1&fmq=1593749731382_R&pv=&ic=0&nc=1&z=&se=&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word='+word
    result=requests.get(url)
    downloadpic(result.text,word)
