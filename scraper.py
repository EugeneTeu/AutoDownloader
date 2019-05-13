import requests

from lxml import html
from bs4 import BeautifulSoup


url = "https://www.imdb.com/title/tt0109830/?ref_=nv_sr_1"
#"https://www.imdb.com/title/tt5977276/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=2413b25e-e3f6-4229-9efd-599bb9ab1f97&pf_rd_r=ENDEWR95YZ20BTNAR1A3&pf_rd_s=right-2&pf_rd_t=15061&pf_rd_i=homepage&ref_=hm_otw_t4"

f= open("web.txt","w+")

with requests.Session() as s:
    result = s.get(url)
    soup = BeautifulSoup(result.content,'lxml')
    #print(soup.prettify)
    #t = soup.findAll('')
    link = list(soup.children)
    #for item in link:
    #   f.write(type(item))
    f.write(str(link[1]))
    print(link[1])



