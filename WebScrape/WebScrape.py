import urllib.request, urllib.parse
import bs4

# WebCont=urllib.request.urlopen("https://www.microcenter.com/search/search_results.aspx?N=4294966998&prt=clearance")
# f=WebCont.read()
# print(f)

# try:
#    with urllib.request.urlopen('https://www.microcenasdter.com/search/search_results.aspx?N=4294966998&prt=clearance') as f:
#       print(f.read().decode('utf-8'))
# except urllib.error.URLError as e:
#    print(e.reason)

headers={}
headers[User-Agent] = 'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36'
