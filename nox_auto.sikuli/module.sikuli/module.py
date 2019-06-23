# -*- coding: utf-8
import sys
import inspect
from sikuli import *
from datetime import datetime

addImagePath(getBundlePath()+"\module.sikuli")
     
logView = 1

# %Y/%m/%d %H:%M:%S.%f
def logging(func):
    def wrapper(obj, *args, **kwds):
        log("class:{} def:{} {} args={} kwds={}".format(
            obj.__class__.__name__, func.__name__, "START", args, kwds))
        rtn = func(obj, *args, **kwds)
        log("class:{} def:{} {} return {}".format(
            obj.__class__.__name__, func.__name__, "END", rtn))
        return rtn
    return wrapper

class base():

    def __init__(self,title,loop=10):
        self.title = title
        self.loop = loop
        self.errflg = False

    @logging
    def end(self):
        appEnd()

    @logging
    def title_start(self):
        title_cw(self.title)

#log出力
def log(str):
    #print('{0} {1}'.format(datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f"),str))
    lognew = datetime.now()
    print("{} {}".format(lognew.strftime("%Y/%m/%d %H:%M:%S.%f"),str))
    #Debug.user("{} {}".format(lognew.strftime("%f"),str))


#領域は左上のみとしておく。
r = Region(0,0,1487,865)
#FindFailed例外を発生させない。
r.setThrowException(False)


#タイトルクリック用
def title_cw(images):
    if not cw(images,5):
        cw("1515168050107.png")
        if not cw(images,5):
            wi("1513607135866.png",["1552182330992.png",[Pattern("1515168050107.png").targetOffset(-91,-185),Pattern("1515168050107.png").targetOffset(-999,-189)],"1552182330992.png"],1,10)
            if not cw(images,10):
                wi(Pattern("1542337280094.png").similar(0.98).targetOffset(-37,2),["1542337258475.png","1542337269951.png",Pattern("1542337280094.png").targetOffset(-37,2)],1,10)
                wi("1542337378450.png",["1515168050107.png","1542337973144.png"],0,10)
                cw(images,10)
    if cw("1543123027844.png",2):
        cw(Pattern("1543123053931.png").targetOffset(-136,-13))
        cw("1543123096558.png")

def restart():
    log('restart in')
    cw(Pattern("1548374567129.png").targetOffset(97,1))
    cw(Pattern("1552150350557.png").targetOffset(77,1))
    cw(Pattern("1515167921682.png").similar(0.71))
    cw("1544975857496.png")
    cw(Pattern("1552226712677.png").targetOffset(0,-15),clicktype='double')
    wi(["1513607135866-1.png","1530983251892.png"],[Pattern("1526772178429.png").exact().targetOffset(425,-10),"1513488863086.png","1544950061895.png","1515168050107-1.png","1529968849204.png","1530983202901.png",Pattern("1531532220851.png").targetOffset(111,-87),Pattern("1541335375215.png").targetOffset(-83,39)],0,500)
    cw(Pattern("1552226712677.png").targetOffset(0,-15),clicktype='double')
    log('restart out')

def appEnd():
    cw("1544950061895.png")
    cw("1515168050107-1.png")
    if cw("1513607135866-1.png"):
        r.wait("1513775028471.png")
    else:
        #固まってる場合はnox再起動
        if not r.exists("1513775028471.png",0.2): restart()

#指定された画像が出たらクリック（click ＆ wait なのでcwだが、意味合い変わってきたな・・・）
#images:list or image
#count:何回繰り返すか。デフォルトは5回なので、5回で見つからなかったらfalseで返す。時間がかかるのが分かってる場合はこの回数を増やすこと。
#delay:1回のループあたりの間隔。繰り返しの負荷を下げたい場合は多くする。デフォルトは0.5秒。
def cw(images,count=5,delay=0.5,clicktype='single'):
    #list型でなければlistに格納
    images = castList(images)
    #配列数分画像をチェック
    for image in images:
        for i in range(count):
            if r.exists(image,delay):
                if clicktype=='single': r.click(image)
                else: r.doubleClick(image)
                if logView == 1 : log('cw img click! image:{0}'.format(image))
                return True
    #最終的に見つからなければFalseを返す
    log('cw unknown! wait:{0}:image:{1}'.format(i,image))
    return False

#タブ形式のプレゼントをまんべんなく取得して終わる処理（よく使うので二文字。tab clickの略）
def tc(getimages,tabimages,count=3):
    #list型でなければlistに格納
    tabimages = castList(tabimages)
    getimages = castList(getimages)
    #配列数分画像をチェック（一周で終わり）
    for tabimage in tabimages:
        #配列側の画像をclick
        if r.exists(tabimage,0.2):
            r.click(tabimage)
            if logView == 1 : log('tc tab click! image:{0}'.format(tabimage))
        #毎タブ画像終了後に受取り画像があるかcount回チェック。毎日やってたら通常3回もやれば十分。
        for i in range(count):
            for getimage in getimages:
                if r.exists(getimage,0.2):
                    r.click(getimage)
                    if logView == 1 : log('tc get click! image:{0}'.format(getimage))
    #基本的に1周するだけなので常にTrueを返す
    return True

#特定の画像が出るまで指定されたclickを繰り返す処理（よく使うので二文字。while imageの略）
#imagesが2つの配列型であればdrag & drop
def wi(baseimages,images,lastclick=0,count=100):
    #list型でなければlistに格納
    #if logView == 1 : log('wi in')
    images = castList(images)
    baseimages = castList(baseimages)
    #繰り返し数。予期せぬ事になっても最悪○回で抜け出して次にスキップするようにする
    for i in range(count):
        #if logView == 1 : log('for in list count')
        #配列数分画像をチェック
        for image in images:
            #if logView == 1 : log('for in images count')
            #配列型であればdrag & drop
            if isinstance(image, list) == True:
                #if logView == 1 : log('image is list')
                if len(image) == 2:
                    r.dragDrop(image[0], image[1])
            else:
                #配列側の画像をclick
                if r.exists(image,0.2):
                    #if logView == 1 : log('image exists')
                    r.click(image)
                    if logView == 1 : log('wi img click! image:{0}'.format(image))
                    #log('debug:wait{0}:image:{1}'.format(i,image))
                    #毎画像終了後に終了画像が出てるかチェック
                #else:
                     #if logView == 1 : log('wi img not find image:{0}'.format(image))
            for baseimage in baseimages:
                if r.exists(baseimage,0.2):
                    #if logView == 1 : log('baseimage is find')
                    #見つかっても一瞬の可能性があるので、1秒置いてもう一回確認
                    sleep(1)
                    if r.exists(baseimage,0.5):
                        #lastclickが1なら最後にclickして処理を戻る
                        if lastclick == 1:
                            r.click(baseimage)
                            if logView == 1 : log('wi baseclick! image:{0}'.format(baseimage))
                        return True
    #最終的に見つからなければFalseを返す
    log('wi unknown! wait:{0}:baseimage:{1}'.format(i,baseimage))
    return False


def castList(images):
    #list型でなければlistに格納（1つ目の階層のみ）
    if isinstance(images, list) == False:
        images = [images]
    return images


def appStop():
    print("stop")


#setAutoWaitTimeout(1)
#r.setWaitScanRate(100)



#Nox起動の部分はまた今度。
    #import sys
    #App.open("C:\Program Files (x86)\Nox\bin\Nox.exe") #動かない
    #App.close("Nox.exe") #動いた
    #App.open("notepad.exe") #動いた

#無限ループになったときは、alt ＋ shift ＋ c

