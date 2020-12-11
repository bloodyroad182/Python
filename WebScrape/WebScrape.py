import urllib.request
import bs4

def GetWebContent (VarURL)
    WebCont=urllib.request.urlopen(VarURL)