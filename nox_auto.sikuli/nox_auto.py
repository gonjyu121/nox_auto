# -*- coding:utf-8
import sys
import inspect
from sikuli import *
from datetime import datetime
Settings.UserLogs
Settings.UserLogPrefix = "#"
Settings.UserLogTime = True
Settings.ActionLogs=False #clickログなどを取らない
# pythonにはsys.exit()があるが、SikuliXの内部初期化のためにexit()を使わなくてはならない。
# sys.path.append(getBundlePath()+"\module.sikuli")
addImportPath = getBundlePath()+"\module.sikuli"
import module
from module import *
Debug.setUserLogFile(getBundlePath()+"\log.sikuli\log.py")

def appStart():
    #ピンポイントで実施したいメソッド（普段はコメントアウト）
    #valcone("1514086348155.png","1549786366152.png").quest()
    #valcone("1514086348155.png","1549786366152.png").tou()
    #valcone("1514086348155.png","1549786366152.png").eventQuest()
    #valcone("1514086348155.png","1549786366152.png").kourin()
    #valcone("1514086348155.png","1549786366152.png").attack()
    #valcone("1514086348155.png","1549786366152.png").douga()
    #for i in range(1000): valcone("1514086348155.png","1549786366152.png").raidbattle()
    #sutarira(["1540625525349.png"]).risemara()
    #sutarira(["1540625525349.png"]).quest()
    #sutarira(["1540625525349.png"]).ibeboss()
    #sutarira(["1540625525349.png"]).vsreview()
    #sutarira(["1540625525349.png"]).chareview()
    #sironeko("1513607135866.png").presentget()
    #bassa("1538056210978.png").battle_jyo()
    #bassa("1538056210978.png").kyoutou_syo()
    bassa("1538056210978.png").kyoutou_tyu()
    #bassa("1538056210978.png").kyoutoubosyu()
    #sevenknights("1514594964037.png").battle()
    #sevenknights("1514594964037.png").arena()
    #ffbe("1514095893745.png").jigen()
    #ffbe("1514095893745.png").itemget()
    #sys.exit()
    #appEnd()
    #saoif("1514598609335.png").present()
    #gurablue("1515926876498.png").battle()
    #priconne("1519560720548.png").quest()
    #priconne("1519560720548.png").request()
    #linerevo("1513555048596.png").sugoroku()
    #linerevo("1513555048596.png").slotmachine()
    #linerevo("1513555048596.png").getruun()
    #browndust("1521942265355.png").missionloop()
    #browndust("1521942265355.png").akumaloop()
    #browndust("1521942265355.png").hosi1up()
    #gansoku("1533429583435.png").battleloop()
    #unison("1513703784166.png").baikyaku()
    #sinsangokusi("1538301963645.png").risemara1()
    #sinsangokusi("1538301963645.png").risemara2()
    #musouzan("1538957758024.png").renzoku()
    #sganrowa("1514088600576.png").battle()
    #ffrk("1514089721092.png").eventloop()
    #ffrk("1514089721092.png").normalDungeon()

    #for i in range(1000):
        #wi(Pattern("1533430977054.png").targetOffset(13,83),"1533431036302.png")

    #Android5.1
    #for i in range(1000):
        #update("1514504304305.png").main()

    for i in range(1000):
        #saocr("1514098562913.png").main()
        #本編ここから
        #sansuma(["1513607283682.png","1513489998537.png"]).main()
        #hit("1533429551473.png").main()
        #gansoku("1533429583435.png").main()
        sganrowa(["1514088600576.png","1552228556493.png"]).main()
        battlegirl(["1513776003005.png","1552228600790.png"]).main()
        unison(["1513703784166.png","1552228622071.png"]).main()
        jojodr(["1539428915641.png","1539428931995.png","1552228635805.png"]).main()
        ffrk(["1514089721092.png","1542758637555.png","1552228647916.png"]).main()
        dereste(["1514097927025.png","1552228665988.png"]).main()
        bassa(["1538056210978.png","1552179387245.png"]).main()
        hosidra(["1514104334655.png","1529732868458.png","1552228691440.png"]).main()
        ffbe(["1514095893745.png","1552228706517.png"]).main()
        browndust(["1521942265355.png","1545570599470.png","1552228718341.png"]).main()
        sinoalice(["1533429571448.png","1552182491765.png"]).main()
        gurablue(["1515926876498.png","1552182820844.png","1552182840952.png"]).main()
        musouzan(["1538957758024.png","1545570633024.png","1552227127053.png"]).main()
        casipro(["1533429561894.png","1552228067876.png"]).main()
        linerevo(["1513555048596.png","1513489981954.png","1552228348497.png"]).main()
        update("1514504304305.png").main()
        sevenknights(["1514594964037.png","1552228364190.png"]).main()
        valcone(["1529732566850.png","1514086348155.png","1552228375552.png"]).main()
        sinsangokusi(["1538301963645.png","1552228399494.png"]).main()
        saoif(["1514598609335.png","1552228414559.png"]).main()
        orusaga(["1513606032856.png","1513490040130.png","1552228444510.png"]).main()
        shadowverse(["1514089340415.png","1552228576104.png"]).main()
        garupa(["1533429531697.png","1552228501232.png"]).main()
        saomd(["1514099499297.png","1552228465807.png"]).main()
        kingdom(["1514100008070.png","1552228483295.png"]).main()
        sirotennis(["1533426760265.png","1552228521105.png"]).main()
        priconne(["1519560720548.png","1552228537743.png"]).main()




class sironeko(base):
    @logging
    def presentget(self):
        wi("1513607135866.png",["1546269346276.png","1546269356055.png","1546269367697.png"],0,5000)

class ffbe(base):
    @logging
    def main(self):
        if not r.exists("1514305732355.png",0.2): self.start()
        self.present()
        self.end()
    @logging
    def start(self):
        self.title_start()
        wi("1514305732355.png",["1514096151815.png","1514096203752.png","1514096220658.png","1514096236448.png","1521604455005.png"])
    @logging
    def present(self):
        wi("1514096394503.png",[Pattern("1514096293974.png").similar(0.87),"1514096307465.png","1514305837685.png","1514305868254.png"])
    @logging
    def jigen(self):
        #wi("1517059620982.png",["1514305732355.png","1517059510918.png","1517059527489.png"],1)
        for i in range(100):
            wi("1517059620982.png",["1517059545121.png","1517059557845.png",Pattern("1517059597590.png").targetOffset(16,95)],1)
            wi("1517059545121.png",[["1517059713277.png",Pattern("1517059713277.png").targetOffset(0,-330)],Pattern("1517059789988.png").similar(0.83),"1517059820168.png","1517059926736.png","1517060015863.png","1517060022546.png"])
    @logging
    def itemget(self):
        wi("1545001907013.png",[Pattern("1545001923683.png").exact(),Pattern("1545002094202.png").exact(),"1545001950443.png","1545001960766.png"],0,100)

class sutarira(base):
    @logging
    def main(self):
        self.title_start()
        self.end()
    @logging
    def vsreview(self):
        wi("1513607135866.png",["1544867711181.png",Pattern("1547255309904.png").targetOffset(-4,37),"1541775319770.png",Pattern("1544867770144.png").similar(0.80),"1544868064301.png",Pattern("1547255345751.png").targetOffset(137,1),"1544868481103.png"],0,10000)
    @logging
    def chareview(self):
        wi("1513607135866.png",["1548503582437.png",Pattern("1548503609268.png").targetOffset(0,26),"1541775319770.png",Pattern("1544867770144.png").similar(0.80),"1544868064301.png",Pattern("1547255345751.png").targetOffset(137,1),"1544868481103.png"],0,1000)
    @logging
    def quest(self):
        wi("1513607135866.png",[Pattern("1541775249511.png").targetOffset(31,57),"1541775271224.png",Pattern("1541775293607.png").targetOffset(6,104),"1541775319770.png","1541775372185.png",Pattern("1541775437080.png").similar(0.80),Pattern("1557359911867.png").targetOffset(-117,-4),"1541775477972.png",Pattern("1541775558230.png").targetOffset(-290,0)],0,1000)
    @logging
    def ibeboss(self):
        wi("1513607135866.png",["1545350035294.png",Pattern("1545350056626.png").similar(0.86),"1541775271224.png",Pattern("1541775293607.png").targetOffset(6,104),"1541775319770.png","1541775372185.png",Pattern("1541775437080.png").similar(0.80),Pattern("1545468065249.png").targetOffset(-111,0),"1541775477972.png",Pattern("1541775558230.png").targetOffset(-290,0)],0,1000)
        #Pattern("1541839940579.png").similar(0.94)"1544135368817.png"
    @logging
    def risemara(self):
        cw("1540628654404.png")
        wi("1540628766054.png",[Pattern("1540628669977.png").targetOffset(284,-2),"1540628697797.png",Pattern("1540628720345.png").targetOffset(193,36),"1540628739703.png"],1)
        wi("1540626484113.png",["1540628806455.png","1540628842906.png","1540628853195.png","1540626163725.png"],1,1000)
        wi("1540625760027.png",["1540629122380.png","1540626505363.png","1540626518098.png","1540626484113.png"],1)
        wi("1540626163725.png",["1540629122380.png","1540625760027.png",Pattern("1540625691972.png").targetOffset(95,0),Pattern("1540625691972-2.png").targetOffset(-115,0)],1)
        wi("1540626468239.png",["1540629122380.png","1540625760027.png",Pattern("1540625691972.png").targetOffset(95,0),Pattern("1540625691972-2.png").targetOffset(-115,0),"1540628220401.png",Pattern("1540626218471.png").targetOffset(0,-85),Pattern("1540635726701.png").targetOffset(0,90)],1)
        wi("1540630582251.png",["1540626468239.png",Pattern("1540636404190.png").targetOffset(-1,-113),"1540626505363.png","1540626518098.png","1540627454003.png","1540625760027.png"])
        wi("1540631161058.png",["1540629122380.png","1540625760027.png",Pattern("1540625691972.png").targetOffset(95,0),Pattern("1540625691972-2.png").targetOffset(-115,0),Pattern("1540625691972.png").targetOffset(343,-2)],1)
        wi("1540626392789.png",[Pattern("1540625691972.png").targetOffset(95,0),"1540631161058.png","1540631204531.png","1540627454003.png"],1)
        wi("1540631461009.png",["1540627524622.png","1540627543380.png","1540625760027.png"])
        wi("1540626392789.png",["1540629122380.png","1540625760027.png",Pattern("1540625691972.png").targetOffset(95,0),Pattern("1540625691972-2.png").targetOffset(-115,0)],1)
        wi("1540628199651.png",["1540629122380.png","1540625760027.png",Pattern("1540625691972.png").targetOffset(95,0),Pattern("1540625691972-2.png").targetOffset(-115,0),Pattern("1540626218471.png").targetOffset(0,-85),"1540628031566.png","1540627454003.png","1540628053757.png"],1)
        wi("1540628259604.png",["1540628053757.png","1540628199651.png","1540628211576.png","1540628220401.png"])
        wi("1540628302741.png",[Pattern("1540637441913.png").targetOffset(-37,0),"1540628290187.png"])
        #sys.exit()


class sganrowa(base):
    @logging
    def main(self):
        if not r.exists(Pattern("1557138818543.png").similar(0.79),0.2): self.start()
        self.presents()
        self.end()
    @logging
    def start(self):
        self.title_start()
        wi(Pattern("1557138818543.png").similar(0.79),["1557138710610.png","1514089054121.png","1514089071531.png","1514089108565.png","1514299216376.png","1544948521272.png","1544948555208.png","1557138774922.png"])
    @logging
    def presents(self):
        wi("1514089252064.png",["1514089206217.png","1557138912912.png","1514089224604.png","1514089238732.png"])
    @logging
    def battle(self):
        wi("1513607135866.png",[Pattern("1540081677477.png").similar(0.80).targetOffset(-2,-24),Pattern("1540081713087.png").similar(0.94),"1540081755647.png","1540081773559.png",Pattern("1540081805970.png").targetOffset(17,4),"1540081835761.png",Pattern("1540081852889.png").targetOffset(-1,-18),Pattern("1540082099410.png").targetOffset(0,-22),Pattern("1540082144117.png").similar(0.72),"1540082951468.png",Pattern("1540083059587.png").similar(0.94),Pattern("1540083020221.png").similar(0.91)])



class musouzan(base):
    @logging
    def main(self):
        if not r.exists("1538910047584.png",0.2): self.start()
        self.story()
        self.end()
    @logging
    def story(self): 
        wi("1513607135866.png",["1538958176485.png","1538957916524.png","1538957962714.png","1538957980323.png","1538958022519.png"])
    @logging
    def renzoku(self): 
        wi("1513607135866.png",["1539010070414.png","1538958022519.png","1539010089079.png","1539010125777.png","1539010146637.png","1538958022519.png","1539010163979.png","1539011410036.png","1539014954295.png",Pattern("1539012944630.png").targetOffset(133,-68)],0,1000)
    @logging
    def start(self):
        self.title_start()
        wi("1552227430305.png",["1552227289269.png"],1)
        wi(Pattern("1552227905745.png").similar(0.75),[Pattern("1552227508566.png").targetOffset(49,63),"1552227540417.png",Pattern("1552227562773.png").similar(0.76).targetOffset(37,38)],0,20)
        wi(Pattern("1552227905745.png").similar(0.75),["1552227822634.png"],0)


class sinsangokusi(base):
    @logging
    def main(self):
        if not r.exists("1538910047584.png",0.2): self.start()
        for i in range(3):
            self.iroiro()
            if r.exists("1538910713092.png",0.2): self.mail()
        self.end()
    @logging
    def mail(self):
        wi("1538910939410.png",["1538910713092.png",Pattern("1538910838494.png").targetOffset(-45,-1),"1538910857158.png"])
    @logging
    def iroiro(self):
        wi("1513607135866.png",["1538911057291.png",Pattern("1538910613076.png").similar(0.85).targetOffset(3,13),"1538910560787.png","1538910435815.png",Pattern("1538301324817.png").similar(0.65).targetOffset(-17,-18),Pattern("1538302174494.png").similar(0.79).targetOffset(-32,-36),"1538301299085.png"],0,8)
    @logging
    def start(self):
        self.title_start()
        wi("1538910047584.png",["1538910188692.png","1538910198573.png","1538910207436.png","1538932440506.png"])
    @logging
    def risemara1(self):
        wi("1538301545307.png",["1538301180546.png","1538301194045.png","1538301232045.png","1538301299085.png",Pattern("1538301324817.png").similar(0.65).targetOffset(-17,-18),Pattern("1538302174494.png").similar(0.79).targetOffset(-32,-36),"1538301472455.png",Pattern("1538302075198.png").similar(0.71)])
    def risemara2(self):
        wi("1538302661854.png",["1538301299085.png",Pattern("1538301324817.png").similar(0.65).targetOffset(-17,-18),Pattern("1538302174494.png").similar(0.79).targetOffset(-32,-36),"1538301472455.png",Pattern("1538302075198.png").similar(0.71),"1538306240369.png",Pattern("1538301894555.png").targetOffset(-49,-49),"1538301194045.png"])

        
class bassa(base):
    @logging
    def main(self):
        if not r.exists("1538056402203.png",0.2): self.start()
        for i in range(3):
            if r.exists("1538190728793.png",0.2): self.muryogatya()
            if r.exists("1538265424799.png",0.2): self.present()
        self.end()
    @logging
    def start(self):
        self.title_start()
        wi("1538056402203.png",[Pattern("1542966875219.png").targetOffset(416,351),"1538056694341.png","1538056709315.png","1538056739724.png","1538056502151.png","1538056523394.png","1538056562228.png","1538610849809.png","1538265896045.png","1538610882227.png","1538190681850.png","1544797863157.png"])
    @logging
    def present(self):
        wi(Pattern("1538265938119.png").similar(0.96),["1538265424799.png","1538265888776.png","1538610882227.png","1538265896045.png"])
        cw("1538265980835.png")
    @logging
    def muryogatya(self):
        cw(Pattern("1538190728793.png").targetOffset(2,18))
        wi("1538190910786.png",["1538190830308.png","1538190845214.png","1538190859587.png","1538190877152.png","1538190893235.png"])
        cw("1538190936108.png")
    @logging
    def kyoutou_syo(self):
        wi("1513607135866.png",["1538242816874.png","1555840921035.png",Pattern("1538242866408.png").similar(0.97),"1538242895851.png","1538242906915.png",Pattern("1538242944037.png").similar(0.98),"1538823085514.png"],0,10000)
    @logging
    def kyoutou_tyu(self):
        wi("1513607135866.png",["1538242816874.png","1555840921035.png",Pattern("1556618638434.png").similar(0.77).targetOffset(40,11),"1538242895851.png","1538242906915.png",Pattern("1538242944037.png").similar(0.98),Pattern("1556618739452.png").similar(0.93),"1538823085514.png",Pattern("1556618830746.png").targetOffset(-201,-36),Pattern("1558969334903.png").targetOffset(125,-15),"1558969389177.png"],0,10000)
    @logging
    def battle_jyo(self):
        wi("1513607135866.png",["1538242816874.png","1555840921035.png",Pattern("1557105770883.png").similar(0.82),Pattern("1557105828016.png").targetOffset(117,102),"1538242895851.png","1538242906915.png",Pattern("1538242944037.png").similar(0.98),Pattern("1556618739452.png").similar(0.93),"1538823085514.png",Pattern("1556618830746.png").targetOffset(-201,-36)],0,10000)
        self.end()
    @logging
    def kyoutoubosyu(self):
        wi("1513607135866.png",["1538822604549.png","1538822618321.png",Pattern("1558360240017.png").similar(0.91),"1538242816874.png",Pattern("1538242944037.png").similar(0.98),Pattern("1538822987395.png").similar(0.85).targetOffset(-314,5),Pattern("1546569283081.png").targetOffset(-7,17)],0,1000)
        #wi("1513607135866.png",["1538822604549.png","1538822618321.png",Pattern("1538822630644.png").similar(0.84),Pattern("1538822630644.png").similar(0.85),"1538242816874.png",Pattern("1538242944037.png").similar(0.98),Pattern("1538822987395.png").similar(0.85).targetOffset(-314,5),Pattern("1546569283081.png").targetOffset(-7,17)],0,1000)
        #wi("1513607135866.png",["1538822604549.png","1538822618321.png",Pattern("1551574901054.png").targetOffset(76,109),"1538242816874.png",Pattern("1538242944037.png").similar(0.93),Pattern("1538822987395.png").similar(0.85).targetOffset(-314,5),Pattern("1546569283081.png").targetOffset(-7,17)],0,1000)
        self.end()

class gansoku(base):
    @logging
    def main(self):
        if not r.exists("1518436297567.png",0.2): self.start()
        for i in range(3):
            if r.exists("1518435856170.png",0.2): self.container()
            if r.exists("1518436027120.png",0.2): self.mission()
        self.end()
    @logging
    def start(self):
        self.title_start()
        wi("1518435605719.png",["1518435505780.png","1518435551039.png","1518435587677.png","1518469684688.png","1518824714670.png","1519536552079.png"])
        cw("1518435631901.png")
    @logging
    def container(self):
        wi("1518435904631.png",["1518435856170.png","1518435887874.png"],1)
    @logging
    def mission(self):
        wi("1518436199125.png",[Pattern("1518436027120.png").targetOffset(61,16),"1518436134913.png","1518436163254.png"],0,20)
        cw("1518436215687.png")
    @logging
    def battle(self):
        wi("1518435505780.png",["1518563849857.png","1518563878805.png","1518563909402.png"])
    @logging
    def battleloop(self):
        wi("1513607135866.png",["1534647394864.png",[Pattern("1535262475524.png").targetOffset(-13,-83),Pattern("1535262475524.png").targetOffset(-17,-167)],[Pattern("1535267465460.png").targetOffset(-5,-83),Pattern("1535267465460.png").targetOffset(14,-180)],[Pattern("1535262506357.png").targetOffset(-13,-83),Pattern("1535262506357.png").targetOffset(-18,-168)],"1535262713384.png","1535282973125.png","1535282993260.png"],0,10000)

class valcone(base):
    @logging
    def main(self):
        if not r.exists("1514151006260.png",0.2): self.start()
        for i in range(self.loop):
            if r.exists("1515073775206.png",0.2): self.gacha()
            if r.exists("1515107450943.png",0.2): self.present()
            if r.exists("1515168287565.png",0.2): self.friend()
            if r.exists("1513607135866.png",0.2): self.end()
            if r.exists("1520080077400.png",0.2): self.connect()
            #self.arena()
        self.end()
        
    @logging
    def gacha(self):
        cw("1515075209479.png")
        r.dragDrop(Pattern("1514151372589.png").targetOffset(-3,455), Pattern("1514151372589.png").targetOffset(0,3))
        wi("1515074934529.png",[Pattern("1515074722401.png").similar(0.86).targetOffset(-57,31),"1515074757934.png","1515074770340.png","1515074780978.png","1515074794894.png"])
        cw("1514151372589.png")
    @logging
    def arena(self):
        wi("1514151669600.png",["1514151437868.png","1515107505344.png","1514151456642.png","1514150979786.png",Pattern("1514151475427.png").targetOffset(-50,2),"1514151500103.png","1514151519189.png","1514151569741.png","1514151850522.png"])
        wi("1514151669600.png",["1514151700210.png","1514151456642.png","1514150979786.png",Pattern("1514151475427.png").targetOffset(-50,2),"1514151500103.png","1514151519189.png","1514151569741.png","1514151850522.png","1514644983266.png"])
        cw("1514151372589.png")
    @logging
    def present(self):
        wi("1514151212197.png",["1514151143631.png","1514151155119.png","1514150979786.png"])
        cw("1514151372589.png")
    @logging
    def friend(self):
        wi(Pattern("1515073523990.png").similar(0.95),["1514151260415.png","1514151275015.png","1514151288302.png","1514151300079.png","1514150979786.png"])
        cw("1514151372589.png")
    @logging
    def start(self):
        self.title_start()
        cw(Pattern("1529733324073.png").targetOffset(72,82))
        wi("1528625275483.png",["1529733123124.png","1529733051994.png","1528624957612.png","1514150910536.png","1528624986779.png","1514150946862.png","1514150979786.png","1518908165188.png","1528625203178.png","1528625255643.png"],1)
    @logging
    def tou(self):
        wi("1513607135866.png",[Pattern("1514033164941.png").similar(0.86),Pattern("1516919159861.png").similar(0.88),Pattern("1516716357211.png").similar(0.77).targetOffset(-4,24),Pattern("1541929610343.png").targetOffset(-45,-38),"1514027256711.png",Pattern("1516908966084.png").targetOffset(-90,-7),"1514027326796.png","1514035331539.png","1514033257526.png","1514033271348.png","1514033340045.png","1514035766425.png",Pattern("1514035851633.png").similar(0.80),"1514034350990.png","1514035054005.png",Pattern("1516909537438.png").targetOffset(-112,-20),"1516919223292.png"],0,1000)
    @logging
    def eventQuest(self):
        wi("1513607135866.png",[Pattern("1514033164941.png").similar(0.83),"1514027256711.png","1514027326796.png","1514035331539.png","1514033257526.png","1514033271348.png","1514035054005.png","1514644983266.png",Pattern("1514645399009.png").targetOffset(-69,46),"1514645293676.png","1514645313447.png","1514644983266.png"],0,1000)
        self.main()
    @logging
    def quest(self):
        wi("1513607135866.png",["1514027256711.png","1514027326796.png","1514027366119.png","1514027386577.png","1514033257526.png","1514033271348.png",Pattern("1533456360127.png").similar(0.91)],0,5000)
    @logging
    def kourin(self):
        wi("1513607135866.png",["1530034331226.png","1530034358403.png","1514033257526.png","1514027366119.png","1541915336023.png","1514027326796.png"],0,5000)
    @logging
    def connect(self):
        wi("1514035331539.png",["1520080077400.png","1514033257526.png","1514027326796.png","1514027386577.png","1520087769909.png"],1)
    @logging
    def attack(self):
        wi("1513607135866.png",["1546184763541.png","1546184779018.png","1514027326796.png","1530034358403.png","1514027366119.png","1514027386577.png","1514033257526.png","1514033271348.png","1546185121047.png","1546185375658.png"],0,5000)
    @logging
    def douga(self):
        wi("1513607135866.png",["1556792237028.png","1556792247206.png",Pattern("1556979367504.png").targetOffset(66,-27),"1556792279999.png","1557240900273.png",Pattern("1556792328891.png").similar(0.90),"1556792488507.png","1556792549327.png",Pattern("1556792567612.png").similar(0.64),Pattern("1556792591897.png").targetOffset(113,87),"1556792627724.png","1557651204922.png"],10000)
    @logging
    def raidbattle(self):
        wi("1553950776493.png",["1553950865349.png","1553948157416.png","1553948190753.png","1553948208393.png",Pattern("1553948241030.png").similar(0.82),"1514027326796.png","1553948229167.png",Pattern("1553948241030.png").similar(0.82),"1553948355500.png","1553948374486.png","1514027366119.png","1554075618855.png","1553948495408.png","1554077028446.png","1554077050983.png"],0,50000)
        wi("1553948157416.png",["1553950852845.png","1553950865349.png"])


class priconne(base):
    @logging
    def main(self):
        if not r.exists("1520760598056.png",0.2): self.start()
        if r.exists("1521259276842.png",0.2): self.tansaku()
        #if r.exists("1521259276842.png",0.2): self.quest()
        if r.exists("1524304098836.png",0.2): self.hardquest()
        for i in range(self.loop):
            if r.exists(Pattern("1520760669937.png").similar(0.93),0.2): self.mission()
            if r.exists(Pattern("1520761106893.png").similar(0.94),0.2): self.present()
        self.end()
    @logging
    def present(self):
        wi("1520761211088.png",["1520761157288.png","1521258914831.png","1520761181833.png","1520761200918.png"],10)
        cw("1520761243796.png")
        wi("1520760598056.png",["1520761051829.png","1521260740731.png"])
    @logging
    def mission(self):
        wi(["1524303801030.png","1521275759312.png"],["1520760840935.png","1520760753921.png","1521258914831.png","1520760851505.png","1520760790888.png","1521281498172.png"],5)
        wi("1520760598056.png",["1520761051829.png","1521260740731.png"])
    @logging
    def start(self):
        self.title_start()
        wi("1520170829134.png",["1520170690395.png","1520170732701.png","1520170757531.png","1519567034494.png","1520202368549.png","1533943724615.png","1544927545799.png"])
        wi("1520760598056.png",["1520761051829.png","1521260740731.png"])
    @logging
    def tansaku(self):
        wi("1521260250864.png",["1521259276842.png","1544965367801.png"])
        wi(Pattern("1521260651394.png").similar(0.93),["1521259867626.png",Pattern("1522109830697.png").similar(0.73),"1519565572110.png","1519565657264.png","1519565681792.png","1519565691486.png","1520171665122.png","1519566967410.png","1521260040750.png","1521260064122.png","1520171219242.png"])
        wi("1521260250864.png",["1521259276842.png","1544965367801.png",Pattern("1521260349828.png").targetOffset(-40,-1)])
        wi(Pattern("1521260651394.png").similar(0.93),["1521260429935.png",Pattern("1522109830697.png").similar(0.73),"1519565572110.png","1519565657264.png","1519565681792.png","1519565691486.png","1520171665122.png","1519566967410.png","1521260040750.png","1521260064122.png","1520171219242.png"])
        wi("1520760598056.png",["1520761051829.png","1521260740731.png"])
    @logging
    def hardquest(self):
        wi(["1524304149362.png","1533943502693.png"],["1524304098836.png"])
        #1
        wi("1524312102452.png",["1544934244410.png","1524304336064.png",Pattern("1533943356996.png").similar(0.92).targetOffset(-113,-4),"1524304361991.png"])
        wi("1524310314189.png",["1519565572110.png","1519565657264.png","1519565681792.png","1519565691486.png","1520171665122.png","1519566967410.png","1520171219242.png","1524310138281.png","1524310167127.png",Pattern("1533943356996.png").similar(0.92).targetOffset(-113,-4),"1524304361991.png"])
        #1
        wi("1524312102452.png",["1524312049232.png","1524304336064.png",Pattern("1533943356996.png").similar(0.92).targetOffset(-113,-4),"1524312075096.png"])
        wi("1524310314189.png",["1519565572110.png","1519565657264.png","1519565681792.png","1519565691486.png","1520171665122.png","1519566967410.png","1520171219242.png","1524310138281.png","1524310167127.png",Pattern("1533943356996.png").similar(0.92).targetOffset(-113,-4),"1524312075096.png"])
        wi(["1524304149362.png","1533943502693.png"],["1524310342669.png","1524310355973.png","1524310381485.png","1524311934450.png"])
    @logging
    def quest(self):
        wi(["1520171038984.png","1519566967410.png","1519565572110.png"],["1521259276842.png","1521259469957.png"])
        wi("1521275759312.png",[Pattern("1520171038984.png").targetOffset(-2,61),"1519565572110.png","1519565657264.png","1519565681792.png","1519565691486.png","1520171665122.png","1519566967410.png","1520171219242.png"])
    @logging
    def request(self):
        wi("1521275759312.png",[Pattern("1520171038984.png").targetOffset(-2,61),"1519565572110.png","1519565657264.png","1519565681792.png","1519565691486.png","1520171665122.png",Pattern("1521633603551.png").targetOffset(0,610),Pattern("1521630795560.png").similar(0.77),Pattern("1521631643966.png").targetOffset(38,18),"1520171219242.png"],0,1000)
    @logging
    def resemara(self):
        #wi("1519560912673.png",["1519560870985.png","1519560884256.png"])
        #wi("1519561008726.png",["1519560912673.png","1519560959582.png"])
        #wi(Pattern("1519561321369.png").exact(),["1519561008726.png",Pattern("1513606870853.png").targetOffset(607,288),"1519561091354.png","1519561108538.png",Pattern("1520130278657.png").similar(0.91).targetOffset(-37,0),Pattern("1519561227918.png").similar(0.77).targetOffset(-32,-2)])
        #wi([Pattern("1519562997852.png").similar(0.98),"1520133788824.png"],["1519561414205.png",Pattern("1519564282898.png").similar(0.80),"1519562806096.png","1519562836833.png"])
        wi("1519564351960.png",[Pattern("1519562997852.png").similar(0.98),"1519563009828.png","1519562836833.png",Pattern("1519564282898.png").similar(0.80)],1000)
        wi("1519562806096.png",["1519564351960.png",Pattern("1519562997852.png").similar(0.98),"1519561414205.png","1519563009828.png","1519562836833.png",Pattern("1519564282898.png").similar(0.80)])
        wi("1519565459607.png",["1519564351960.png","1519562806096.png",Pattern("1519564282898.png").similar(0.80),"1519564548068.png","1519564567600.png",Pattern("1519562997852.png").similar(0.98),"1519563009828.png","1519562836833.png"])
        wi("1519566922715.png",["1519565478237.png","1519565491891.png",Pattern("1519564282898.png").similar(0.80),"1519565556385.png","1519565572110.png",Pattern("1519565608876.png").similar(0.85).targetOffset(-3,113),"1519565657264.png","1519565681792.png","1519565691486.png"])
        wi("1520135536937.png",["1519566967410.png",Pattern("1519564282898.png").similar(0.80),Pattern("1519565608876.png").similar(0.85).targetOffset(-3,113),"1519567034494.png","1519567085018.png","1520143906388.png"])
        sys.exit()


class hit(base):
    @logging
    def main(self):
        if not r.exists("1538225903778.png",0.2): self.start()
        if r.exists("1523659724038.png",0.2): self.restart()
        for i in range(3):
            if r.exists("1523659724038.png",0.2): self.restart()
            if r.exists("1523143087286.png",0.2): self.gacha()
            if r.exists("1523143439772.png",0.2): self.mail()
            if not self.errflg : cw(Pattern("1515910617767.png").targetOffset(-25,385))
        self.end()
    @logging
    def mail(self):
        tc(["1523143709979.png","1523143215690.png","1523144157684.png","1523143242233.png"],["1523143439772.png","1523143506384.png","1523143513379.png","1523143524246.png","1523143535130.png","1523143629613.png"])
        cw("1523144071282.png")
    @logging
    def start(self):
        self.title_start()
        wi(["1538225903778.png","1523659724038.png"],["1514126081475.png","1514126167299.png","1523142886856.png",Pattern("1515893674215.png").targetOffset(763,-455),"1523142839250.png","1523142928557.png","1523572799669.png"])
    @logging
    def gacha(self):
        wi(Pattern("1523143355782.png").similar(0.94),["1523143087286.png","1523143163885.png","1523143200990.png","1523143215690.png","1523143242233.png"],0,20)
        cw(Pattern("1523143396397.png").targetOffset(-60,-2))
    @logging
    def restart(self):
        cw(Pattern("1523659704691.png").targetOffset(118,-1))
        self.errflg = True
        



class browndust(base):
    @logging
    def main(self):
        if not r.exists("1552180945673.png",0.2): self.start()
        for i in range(3):
            if r.exists("1522990744816.png",0.2): self.mission()
            if r.exists("1522987917944.png",0.2): self.roulette()
            if r.exists(Pattern("1522988104546.png").similar(0.80),0.2): self.guild()
            if r.exists("1522988454989.png",0.2): self.sinpi()
            if r.exists("1522988454989.png",0.2): self.battle()
            if r.exists("1523002714578.png",0.2): self.mail()
        self.end()
    @logging
    def mail(self):
        wi("1513607135866.png",["1523002714578.png","1523003201082.png","1523051512924.png"],0,5)
        wi("1552180945673.png",["1523051552505.png"])
    @logging
    def sinpi(self):
        #20回繰り返し
        wi("1513607135866.png",["1522988454989.png",Pattern("1522988473340.png").targetOffset(3,159),"1546505404960.png",Pattern("1523052086721.png").targetOffset(-24,24),"1522988522438.png",Pattern("1522988551606.png").targetOffset(69,11),Pattern("1523052266112.png").targetOffset(107,46),"1522988593556.png"],0,10)
        wi("1552180945673.png",["1522989183477.png","1546505458831.png"])
    @logging
    def battle(self):
        wi([Pattern("1522990412384.png").similar(0.75),"1523314154410.png","1523669312016.png"],["1522988454989.png",Pattern("1522989259407.png").targetOffset(2,160),"1552181126137.png","1522989303755.png","1522989317155.png","1523052803358.png","1523224950909.png",Pattern("1522988551606.png").targetOffset(69,11)])
        wi("1552180945673.png",["1522990451287.png","1522990496603.png","1523669349240.png"])
    @logging
    def guild(self):
        #10回繰り返し
        wi("1513607135866.png",["1522988160149.png","1522988179102.png",Pattern("1522988194370.png").similar(0.80)],0,5)
        cw("1522988350053.png")
    @logging
    def roulette(self):
        #10回繰り返し
        wi("1522988035598.png",["1522987983874.png","1522987995326.png","1522988014858.png","1522990556210.png"],0,5)
        cw(Pattern("1521942711364.png").similar(0.78))
    @logging
    def mission(self):
        #10回繰り返し
        wi("1513607135866.png",["1522990805222.png"],0,5)
    @logging
    def missionloop(self):
        wi("1513607135866.png",["1521945703888.png","1521945743676.png","1521945757164.png","1539475237456.png",Pattern("1539476021424.png").similar(0.95),"1521946079949.png","1539477706823.png","1521946218162.png","1521956484177.png","1521956521674.png","1521956574331.png",Pattern("1521968543059.png").similar(0.90),"1525001510768.png"],0,1000)
    @logging
    def akumaloop(self):
        wi("1513607135866.png",["1524931456068.png","1521945757164.png","1539475237456.png"],0,1000)
    @logging
    def hosi1up(self):
        for i in range(self.loop):
            wi(Pattern("1529193062060.png").similar(0.90),["1529192588217.png","1529192616909.png","1529192639931.png",Pattern("1529192677010.png").similar(0.78),"1529192761700.png","1529192790029.png","1529192810428.png","1529192865834.png","1529192943723.png","1529192960447.png","1529192982597.png","1529193009349.png","1529193020392.png","1529193032934.png"])
            wi("1529193032934.png",[Pattern("1529193062060.png").similar(0.90),Pattern("1529193071440.png").exact(),"1529193099457.png","1529193120768.png","1529193020392.png"])
            wi("1529193628943.png",["1529193032934.png",Pattern("1529193226382.png").similar(0.75)])
    @logging
    def start(self):
        self.title_start()
        wi("1552180945673.png",[Pattern("1521942711364.png").similar(0.78),Pattern("1521942741927.png").targetOffset(-83,4)])


class saoif(base):
    @logging
    def main(self):
        if not r.exists("1515932073632.png",0.2): self.start()
        for i in range(3):
            if r.exists("1515930466762.png",0.2): self.present()
        self.end()
    @logging
    def start(self):
        self.title_start()
        wi("1515932073632.png",["1514598676135.png","1521378721707.png","1516344872739.png","1514785744009.png"],0,200)
    @logging
    def present(self):
        wi(Pattern("1514785774578.png").exact(),["1515930466762.png","1523050778047.png","1515931594369.png","1514894040399.png","1514785744009.png"])
        wi("1515932073632.png",["1514785744009.png","1515931618499.png"])






class gurablue(base):
    @logging
    def main(self):
        if not r.exists("1515927142223.png",0.2): self.start()
        for i in range(3):
            if r.exists("1515927243753.png",0.2): self.present()
        self.end()
    @logging
    def start(self):
        self.title_start()
        wi("1517962201170.png",["1519382499359.png","1517962219693.png","1515926982495.png","1516344318302.png",Pattern("1516344338257.png").similar(0.94),"1516369763563.png",Pattern("1516572590119.png").similar(0.76),"1516630202645.png","1517962085076.png","1552183016669.png",Pattern("1552183110644.png").targetOffset(34,-540)])
    @logging
    def present(self):
        cw("1519382802371.png")
        wi("1515927320093.png",[Pattern("1515927283712.png").similar(0.75),"1515927295376.png","1515927307743.png"])
        cw("1515927337563.png")
    @logging
    def battle(self):
        wi("1515927337563.png",[Pattern("1515927593631.png").targetOffset(169,34),"1515927437797.png","1515927448081.png","1515927457492.png","1515927552379.png"],1)


#オルサガ
class orusaga(base):
    @logging
    def main(self):
        if not r.exists("1519164827996.png",0.2): self.start()
        for i in range(3):
            if r.exists("1514330529950.png",0.2): self.present()
            if r.exists("1519382320383.png",0.2): self.end() 
        self.end()
    @logging
    def start(self):
        self.title_start()
        wi("1519164827996.png",[Pattern("1513490072504.png").targetOffset(594,-110),Pattern("1513606870853.png").targetOffset(607,288),"1513606998107.png","1513490168322.png","1538434659625.png"])
    @logging
    def present(self):
        wi("1514330492111.png",["1514330529950.png","1513490228988.png","1513490248507.png","1514330479470.png"])
        cw("1513490329501.png")
        
        







#さんすま
class sansuma(base):
    @logging
    def main(self):
        self.title_start()
        wi("1513489340090.png",["1513607462797.png","1513607476218.png","1513607496371.png","1516341538300.png","1513607698253.png"])
        wi("1514686159746.png",["1513489340090.png","1513489356031.png","1513489372673.png","1513489388416.png","1513489404761.png","1513489428009.png","1513489442573.png","1513489459012.png","1513489494631.png"])
        cw("1513489629221.png")
        cw("1513489648232.png")
        self.end()



class ffrk(base):
    @logging
    def main(self):
        if not r.exists("1514089813357.png",0.2): self.start()
        for i in range(3):
            if r.exists("1515843732933.png",0.2): self.present()
        #self.event()
        self.end()
    @logging
    def start(self):
        self.title_start()
        wi("1514089813357.png",["1514089753839.png","1514089767128.png","1514089781700.png","1544741235372.png"])
    @logging
    def present(self):
        wi(["1514095867131.png","1515843558293.png"],["1514089848682.png","1514089864010.png","1514089878575.png"])
        cw("1515844154867.png")
    @logging
    def event(self):
        wi(Pattern("1515844627949.png").similar(0.82),["1515844188053.png",Pattern("1515844223168.png").targetOffset(117,-55),"1515844276181.png"])
        self.eventloop()
    @logging
    def eventloop(self):
        wi(["1515900836300.png","1516534971659.png"],[Pattern("1514090255836.png").similar(0.92).targetOffset(128,27),Pattern("1515850661568.png").similar(0.94).targetOffset(52,14),"1514090642613.png","1514090280528.png","1514090295654.png","1514090307956.png","1514090319634.png","1514091023554.png","1514090383692.png","1515853024210.png",Pattern("1515855907179.png").similar(0.90).targetOffset(-2,19),[Pattern("1515853185965.png").targetOffset(0,-63),Pattern("1515853241001.png").targetOffset(-85,99)]])
    @logging
    def normalDungeon(self):
        wi(["1515900836300.png","1516534971659.png"],[Pattern("1515885131972.png").targetOffset(0,-19),"1515885312205.png","1514090642613.png","1514090280528.png","1514090295654.png","1514090307956.png","1514090319634.png","1514091023554.png","1514090383692.png","1515853024210.png",Pattern("1515855907179.png").similar(0.90).targetOffset(-2,19)])

#ユニゾン
class unison(base):
    @logging
    def main(self):
        if not r.exists(Pattern("1544949500571.png").targetOffset(-356,0),0.2): self.start()
        for i in range(10):
            cw(Pattern("1544949500571.png").targetOffset(-356,0))
            if r.exists("1514856963217.png",0.2): self.mimirin()
            if r.exists("1544949612702.png",0.2): self.present()
            if r.exists("1544949940238.png",0.2): self.mission()
            if r.exists("1513607135866.png",0.2): self.start()
            if r.exists(Pattern("1516192425405.png").similar(0.76),0.2): self.restart()
            if r.exists("1517523309936.png",0.2): self.baikyaku()
        self.quest()
        self.end()
    @logging
    def baikyaku(self):
        wi(["1517523392912.png"],[Pattern("1517523309936.png").similar(0.83),"1517523325205.png","1529834154945.png"],1,50)
        wi(Pattern("1538223696227.png").exact(),["1538223287230.png","1538223304731.png","1538223434670.png","1538223447622.png","1538223629451.png"])
        wi("1513607135866.png",[Pattern("1538223487956.png").similar(0.77),Pattern("1538223884250.png").similar(0.87)],0,15)
        cw("1517523309936.png")
        cw("1517523392912.png")
        cw(Pattern("1544949500571.png").targetOffset(-356,0))
    @logging
    def apMax(self):
        cw("1515402755322.png")
        cw(Pattern("1544949500571.png").targetOffset(-356,0))
    @logging
    def start(self):
        self.title_start()
        wi(["1514418183963.png","1517018703279.png","1529760435609.png","1544236261692.png"],["1514088119959.png","1514088136830.png","1514088147554.png"],1)
        self.battleEnd()
    @logging
    def battleEnd(self):
        wi("1514852454809.png",["1514418183963.png","1517018703279.png","1544236261692.png","1517021134812.png","1514087207066.png","1513894680166.png","1513703974319.png","1513704067206.png","1513704084812.png","1513704132150.png","1513704166831.png","1513704189650.png","1514852338877.png","1544949290339.png"],1)
        cw(Pattern("1544949500571.png").targetOffset(-356,0))
    @logging
    def mission(self):
        tc(["1515068929896.png","1515068947048.png"],["1544949940238.png","1514852699408.png","1517021372272.png","1514852732465.png","1514856682564.png","1514856694948.png","1514856772163.png","1517021392140.png"])
        if r.exists("1515402575161.png",0.2):
            cw("1515402755322.png")
            cw(Pattern("1544949500571.png").targetOffset(-356,0))
            self.quest()
    @logging
    def mimirin(self):
        wi(["1544950234997.png","1514857036188.png"],["1544949707753.png","1514856963217.png","1514856976220.png","1514856987029.png","1544950234997.png","1514857021797.png","1514857036188.png"],1)
        cw(Pattern("1544949500571.png").targetOffset(-356,0))
        #"1514857007182.png"
    @logging
    def present(self):
        wi("1514857370797.png",["1544949612702.png","1514857347164.png","1514857359157.png"])
    @logging
    def quest(self):
        wi(["1514857736701.png","1517026945034.png"],["1515070666549.png","1514857565900.png","1514857584134.png",Pattern("1514857630036.png").targetOffset(125,160),"1514857667102.png","1514857680166.png","1514857702187.png","1514857716981.png"])
        wi(["1514857813945.png","1517026945034.png"],["1514857736701.png","1514857781221.png"])
        self.battleEnd()
    @logging
    def mainquest(self):
        wi("1517026945034.png",["1515070666549.png","1514857565900.png","1514857584134.png",Pattern("1514857630036.png").targetOffset(125,160),"1514857667102.png","1514857680166.png","1514857702187.png","1514857716981.png"])
    @logging
    def restart(self):
        self.end()
        self.start()

#リネレボ
class linerevo(base):
    @logging
    def main(self):
        if not r.exists("1515387789684.png",0.2): self.start()
        for i in range(3):
            self.returnActivities()
            self.getActivities()
            if r.exists(Pattern("1513467394054.png").targetOffset(845,21),0.2): self.gouman()
            if r.exists(Pattern("1513468836072.png").targetOffset(845,21),0.2): self.friends()
            if r.exists(Pattern("1513469250926.png").targetOffset(833,25),0.2): self.youbiDungeon()
            if r.exists(Pattern("1513484372649.png").targetOffset(840,27),0.2): self.ketumei()
            if r.exists(Pattern("1513486719699.png").targetOffset(840,19),0.2): self.kettou()
            if r.exists(Pattern("1513487543532.png").targetOffset(882,27),0.2): self.gacha()
        self.mail()
        self.end()
    @logging
    def mail(self):
        cw("1513473111992.png")
        for image in ["1515404421560.png","1515404306077.png","1515404438891.png"]:
            wi("1515404277680.png",["1515404110689.png","1515404213851.png","1515404228477.png","1513812375827.png"])
            cw(image)
    @logging
    def start(self):
        self.title_start()
        wi(["1513436735371.png","1535034933670.png"],["1513427495993.png","1513436716643.png","1513812375827.png","1543793248068.png"],1)
        tc(["1538210727364.png","1538210739538.png"],["1538210822968.png","1538210833224.png","1538210840068.png","1538210851087.png","1538210856581.png",Pattern("1544999878353.png").similar(0.82).targetOffset(-33,17)])
        wi(["1515387789684.png","1515387666628.png"],["1513436735371.png","1535034933670.png",Pattern("1538210889906.png").targetOffset(146,-4),"1538210925459.png",Pattern("1535766012231.png").targetOffset(196,-3),"1513438117134.png","1515386974720.png",Pattern("1515386974720.png").targetOffset(333,240),"1515387268549.png",Pattern("1515387268549.png").targetOffset(165,254),"1515387285841.png",Pattern("1515387285841.png").targetOffset(-135,237),Pattern("1517029410302.png").targetOffset(64,-3),Pattern("1518439497911.png").targetOffset(20,1)])
        wi("1515387789684.png",["1513812375827.png","1515387732578.png","1515387751947.png","1513438117134.png"])
    @logging
    def gouman(self):
        cw(Pattern("1513467394054.png").targetOffset(845,21))
        cw("1513467617051.png")
        cw("1513467662751.png")
        cw(Pattern("1513467694471.png").targetOffset(-68,-2))
        self.getActivities()
    @logging
    def friends(self):
        cw(Pattern("1513468836072.png").targetOffset(845,21))
        cw("1513468965420.png")
        cw("1513468990508.png")
        cw(Pattern("1513469018317.png").targetOffset(-67,-3))
        self.getActivities()
    @logging
    def youbiDungeon(self):
        cw(Pattern("1513469250926.png").targetOffset(833,25))
        cw("1513469294555.png")
        wi("1523140114152.png",["1513469313228.png","1513469586268.png","1513469471949.png"])
        cw(Pattern("1513469673956.png").targetOffset(-107,-4))
        self.returnActivities()
        self.getActivities()
    @logging
    def ketumei(self):
        cw(Pattern("1513484372649.png").targetOffset(840,27))
        if cw(Pattern("1513484622502.png").targetOffset(-58,4)):
            cw("1513484686144.png")
            cw("1513484704459.png")
        if cw(Pattern("1513484736151.png").targetOffset(-70,3)):
            cw("1513484780177.png")
            cw("1513484806569.png")
            cw("1513484704459.png")
        if cw("1513484882939.png"):
            while r.exists("1513484905273.png",1):
                cw("1513484905273.png")
            cw(Pattern("1513485341226.png").targetOffset(-62,-2))
        if cw(Pattern("1513485437177.png").targetOffset(-24,9)):
            cw("1513485478410.png")
            cw(Pattern("1513485508393.png").targetOffset(-42,-4))
            self.getActivities()
    @logging
    def kettou(self):
        cw(Pattern("1513486719699.png").targetOffset(840,19))
        cw("1513486773732.png")
        wi("1513487373586.png",[Pattern("1513486828394.png").similar(0.82).targetOffset(-3,65),"1513469471949.png","1513469586268.png"])
        cw(Pattern("1513487419688.png").targetOffset(-55,-4))
        self.returnActivities()
    @logging
    def gacha(self):
        cw(Pattern("1513487543532.png").targetOffset(882,27))
        wi("1513487810838.png",["1513487744324.png","1538866753541.png","1538866879328.png","1538866889081.png","1513487792668.png","1544829910064.png","1544829920041.png"],1)
        wi(Pattern("1513487837137.png").targetOffset(-66,0),["1513487744324.png","1538866753541.png","1513487792668.png","1513487810838.png"])
        self.getActivities()
    @logging
    def sugoroku(self):
        wi("1513607135866.png",["1521476485468.png"],0,1000)
    @logging
    def slotmachine(self):
        wi("1513607135866.png",[Pattern("1535766653841.png").targetOffset(2,-148),["1535766698013.png","1535766724856.png"]],0,1000)
    @logging
    def getruun(self):
        wi("1513607135866.png","1535880654831.png",0,10000)
    #今日の活動に戻る
    @logging
    def returnActivities(self):
        cw("1513473111992.png")
        cw("1513438117134.png")
    @logging
    def getActivities(self):
        while r.exists("1513467743212.png",1):
            cw("1513612429849.png")
            cw("1513467743212.png")


class saocr(base):
    @logging
    def main(self):
        if not r.exists("1514120935786.png",0.2): self.start()
        self.mail()
        self.scout()
        self.end()
    @logging
    def scout(self):
        wi("1514686475018.png",["1514098928108.png","1529726858890.png"])
        if r.exists("1514098991124.png",0.5):
            wi("1514099224492.png",["1514098991124.png","1514099023950.png","1514099063565.png"])
    @logging
    def mail(self):
        wi(Pattern("1514098886450.png").similar(0.79),["1514098721219.png","1514098824302.png","1514098837949.png","1514098849989.png"])
    @logging
    def start(self):
        self.title_start()
        wi("1515386423475.png",["1514098621634.png",Pattern("1514098659784.png").similar(0.80),Pattern("1514098684050.png").similar(0.80),"1514098708076.png","1514098721219.png","1514333168502.png",Pattern("1515386402442.png").targetOffset(-1,-34)])
        cw(Pattern("1515386456527.png").targetOffset(1,-32))

class sevenknights(base):
    @logging
    def main(self):
        #"1515156923778.png"
        if not r.exists("1533946829170.png",0.2): self.start()
        for i in range(3):
            self.homeBack()
            if r.exists("1533946829170.png",0.2): self.homeBack()            
            if r.exists("1515156972456.png",0.2): self.gacha()
            if r.exists("1533947734607.png",0.2): self.mail()
        #self.normalSp()
        self.eventSp()
        self.end()
    @logging
    def normalSp(self):
        self.homeBack()
        wi("1524004703227.png",["1515199558394.png",Pattern("1515199571114.png").targetOffset(4,101),Pattern("1524004798741.png").targetOffset(-1,73),Pattern("1517014633148.png").targetOffset(143,2),"1515200061859.png"])
        self.battle()
        self.homeBack()
    @logging
    def eventSp(self):
        self.homeBack()
        wi("1517957755184.png",["1515199558394.png",Pattern("1515199571114.png").targetOffset(4,101),Pattern("1515199604750.png").targetOffset(-1,73),Pattern("1517014633148.png").targetOffset(143,2),"1515200061859.png"])
        self.battle()
        self.homeBack()
    @logging
    def homeBack(self):
        wi("1533946829170.png",["1533948959273.png","1515199434786.png","1514595064266.png","1514595127137.png","1514595357675.png",Pattern("1533947207126.png").targetOffset(-50,-50),"1515203653427.png","1514597396097.png","1515204425857.png"])
    @logging
    def mail(self):
        tc(["1514595528583.png","1514595663597.png","1514595499218.png","1514595617932.png","1514595682569.png","1514595699831.png","1514595717880.png",Pattern("1533947207126.png").targetOffset(-50,-50),"1533948478974.png","1533948638341.png","1514595357675.png"],["1533947859793.png","1515156755969.png","1515156763291.png","1515156769129.png","1515156774991.png","1515156782683.png","1515156795042.png"])
        cw("1533948959273.png")
    @logging
    def start(self):
        self.title_start()
        wi("1514595247180.png",["1514595037472.png","1514595064266.png","1514595087865.png",Pattern("1514595127137.png").similar(0.72),Pattern("1514595155408.png").similar(0.65),Pattern("1514595171746.png").similar(0.64),"1519164000387.png","1534074029070.png","1515204425857.png","1533948959273.png","1538779136688.png"])
    @logging
    def gacha(self):
        wi(Pattern("1514595383452.png").similar(0.72),["1514595304782.png","1515157020016.png","1521645416808.png","1514595335329.png","1514595346963.png",Pattern("1514595357675.png").similar(0.80),Pattern("1533947207126.png").targetOffset(-50,-50)])
        cw("1533948959273.png")
    @logging
    def battle(self):
        wi(["1515207183144.png","1515205223587.png","1515203653427.png","1514597396097.png","1515204853526.png"],["1514596079553.png",Pattern("1514596088856.png").similar(0.85),Pattern("1533947207126.png").targetOffset(-50,-50),"1514596104402.png","1514596114401.png","1514596131086.png","1514596148295.png"],0,500)
    @logging
    def arena(self):
        wi("1515284632264.png",["1514596131086.png","1514596148295.png","1514596104402.png","1514596114401.png"],0,500)


class sirotennis(base):
    @logging
    def main(self):
        if not r.exists("1515153357118.png",0.2): self.start()
        self.dreamgacha()
        for i in range(10):
            if r.exists("1515153562898.png",0.2): self.present()
            if r.exists("1514101276154.png",0.5): self.ticketgacha()
        self.end()
    
    @logging
    def dreamgacha(self):
        wi(Pattern("1538227700603.png").exact(),["1538227814698.png","1538227632490.png","1538227651573.png","1514101683663.png"])
        cw("1515153153093.png")
    @logging
    def ticketgacha(self):
        cw("1514101276154.png")
        cw("1514101312570.png")
        r.dragDrop("1514101486605.png", "1514101569518.png")
        wi("1537791078858.png",["1514101620370.png","1514101171629.png","1514101683663.png","1537790867226.png"])
    @logging
    def present(self):
        wi("1514101185802.png",["1514101119156.png","1514101132508.png","1514101143821.png","1514101154925.png","1514101171629.png","1537790867226.png","1514101683663.png"])
        cw("1514101211572.png")
        cw("1514101223599.png")
    @logging
    def start(self):
        self.title_start()
        wi("1515153100527.png",["1514100984579.png","1514101037231.png","1514101059142.png","1515681147229.png","1537790399116.png"])
        cw("1515153153093.png")

class saomd(base):
    @logging
    def main(self):
        self.start()
        for i in range(10):
            if r.exists(Pattern("1514099601899.png").exact(),0.2): self.start()
            if r.exists(Pattern("1514767928396.png").similar(0.93),0.2): self.giftGet()            
        self.end()
    @logging
    def giftGet(self):
        cw("1514099832810.png")
        cw(Pattern("1514099846019.png").similar(0.79))
        cw("1514099863389.png")
        cw("1514099888932.png") 
        wi("1514861679770.png",["1514099931737.png","1514099944199.png","1514099958950.png"])
    @logging
    def start(self):
        self.title_start()
        wi("1515083055939.png",["1514099554382.png",Pattern("1514099601899.png").exact(),"1514099616019.png","1515083072289.png",Pattern("1543104625015.png").targetOffset(149,-179)])
        cw("1515083087846.png")
        self.comment()
    @logging
    def comment(self):
        wi("1514860850009.png",["1514099681324.png","1514099699325.png","1514099727552.png"])
        wi("1514099681324.png",["1514099616019.png"])


class dereste(base):
    @logging
    def main(self):
        self.title_start()
        wi("1514098220129.png",["1514098022154.png","1514098048370.png","1514098179449.png","1514305962982.png","1514796497817.png"])
        wi(Pattern("1514098289136.png").similar(0.84).targetOffset(6,72),["1514098237783.png","1514098251492.png","1514098263024.png"],1)
        wi("1514098404810.png",["1514098339240.png","1514098358160.png","1514098370474.png","1519472616766.png"])
        self.end()
    @logging
    def live(self):
        for i in range(1000):
            r.click(Pattern("1514961450105.png").targetOffset(0,72))



class kingdom(base):
    @logging
    def main(self):
        self.start()
        wi(["1514100091997.png","1514501231739.png"],["1514310206628.png","1514100216842.png"],1)
        self.end()
    @logging
    def start(self):
        self.title_start()
        wi("1514862129087.png",["1514100059777.png",Pattern("1514100072432.png").targetOffset(-107,254),"1514100091997.png","1514100116865.png","1514100137113.png","1514501167416.png","1514862098863.png"])
        wi("1515826351821.png",["1514862149012.png"])







class hosidra(base):
    @logging
    def main(self):
        self.start()
        for i in range(10):
            if r.exists("1513607135866.png",0.2): self.start()
            if r.exists("1514502662539.png",0.2): self.freePresent()
            if r.exists("1514104569564.png",0.2): self.freePresent()
            if r.exists("1514679463885.png",0.2): self.mail()
            cw("1514763812734.png")
            cw("1514106678162.png")
        self.end()
    @logging
    def start(self):
        self.title_start()
        wi("1514333829885.png",["1514502438115.png","1514104395782.png","1514104441735.png","1544395171380.png","1514104462786.png","1528415303028.png","1514333745001.png","1514333816500.png"])
        cw("1514106678162.png")
    @logging
    def mail(self):
        wi(Pattern("1514679897716.png").similar(0.80),["1514106705160.png","1514106718545.png",Pattern("1515824788537.png").targetOffset(-3,18)])
        cw("1514680008889.png")
    @logging
    def freePresent(self):
        wi(["1514104689475.png","1514502899099.png"],["1514104441735.png","1514502662539.png","1514104569564.png","1514104598903.png","1514502735404.png","1514104617969.png",Pattern("1514104657164.png").targetOffset(1,24),"1514502796169.png","1514502842564.png","1514502874899.png","1514502899099.png",[Pattern("1515825881533.png").targetOffset(-1,-76),Pattern("1515825915654.png").targetOffset(62,42)]],1)
        cw("1514106678162.png")



class casipro(base):
    @logging
    def main(self):
        self.title_start()
        wi("1514598050750.png",["1514597762440.png","1552228168922.png","1514597810123.png"])
        wi("1514598138210.png",["1514598107823.png","1514598178855.png"])
        r.dragDrop(Pattern("1514598223567.png").targetOffset(-3,-79), "1514598270096.png")
        cw("1514598374352.png")
        cw("1514682515553.png")
        wi("1514598435167.png",["1514598414947.png","1514598425778.png"],1)
        wi("1538228395889.png",[[Pattern("1538228232388.png").targetOffset(106,-1),Pattern("1538228258138.png").targetOffset(-60,66)],"1514598435167.png"])
        r.dragDrop(Pattern("1538228480448.png").targetOffset(25,71),Pattern("1538228513524.png").targetOffset(4,-179))
        self.end()
        

class update(base):

    @logging
    def main(self):
        if not r.exists("1528412567156.png",0.2): self.title_start()
        log('step 1')
        wi(["1514504401050.png","1533946212677.png"],["1514504371220.png","1533945867747.png","1514504383481.png","1514573055942.png","1543794472128.png","1533945895125.png","1530662620569.png","1533946072031.png"])
        log('step 2')
        wi("1514504304305.png",["1514504467513.png",Pattern("1528412915171.png").similar(0.90)])
        self.end()

class sinoalice(base):
    @logging
    def main(self):
        self.title_start()
        wi("1514500843851.png",[Pattern("1514500401722.png").targetOffset(-130,-247),"1514500805611.png","1514500817012.png"])
        wi("1514500904648.png",["1514500868979.png","1514500881155.png","1514500892299.png","1514500817012.png"])
        self.end()


class garupa(base):
    @logging
    def main(self):
        self.title_start()
        wi("1514101871469.png",["1514101803022.png","1514969808852.png","1514101824207.png","1525955068868.png","1514101858648.png","1514769309224.png","1514769335383.png","1514769348255.png","1525955188549.png","1552486766339.png"])
        wi("1514104258902.png",["1514104214558.png","1514104228893.png","1514104246514.png"])
        self.end()



class jojodr(base):
    @logging
    def main(self):
        self.title_start()
        wi(["1514310449893.png","1535869960221.png"],[Pattern("1514100501931.png").targetOffset(-927,418),"1514100545259.png","1514100569733.png","1535869889433.png","1544739808964.png"])
        wi("1514100673507.png",["1514100619444.png","1514100631835.png","1514100641272.png","1544739808964.png"])
        cw("1514100713332.png")
        wi("1514100778252.png",["1514100725837.png","1514100736872.png","1514100747443.png"])
        self.end()



class shadowverse(base):
    @logging
    def main(self):
        self.title_start()
        wi("1514089553344.png",["1514089378924.png","1523025068877.png","1514089394857.png","1514089439809.png","1514089454021.png","1514089498991.png","1514089519244.png","1552696028450.png"])
        wi("1514089622216.png",[Pattern("1514089608163.png").similar(0.95),"1514089519244.png","1514572960078.png","1514572979884.png","1514572993269.png"])
        self.end()



#バトガ
class battlegirl(base):
    @logging
    def main(self):
        self.title_start()
        wi("1513776114341.png",["1513776079816.png","1514138676901.png"])
        if cw("1513776173326.png"):
            cw("1513776192897.png")
            cw("1513776207340.png")
            cw("1513776223249.png")
        self.end()




















appStart()
