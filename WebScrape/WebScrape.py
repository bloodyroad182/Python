import urllib.request
import bs4

# WebCont=urllib.request.urlopen("https://www.microcenter.com/search/search_results.aspx?N=4294966998&prt=clearance")
# f=WebCont.read()
# print(f)

try:
   with urllib.request.urlopen('https://www.microcenasdter.com/search/search_results.aspx?N=4294966998&prt=clearance') as f:
      print(f.read().decode('utf-8'))
except urllib.error.URLError as e:
   print(e.reason)
