import requests
import json

from lxml import html
from bs4 import BeautifulSoup


#url = 'https://luminus.nus.edu.sg/v2/auth/connect/authorize?client_id=verso&amp;redirect_uri=https%3A%2F%2Fluminus.nus.edu.sg%2Fauth%2Fcallback&amp;response_type=id_token%20token%20code&amp;scope=profile%20email%20role%20openid%20lms.read%20calendar.read%20lms.delete%20lms.write%20calendar.write%20gradebook.write%20offline_access&amp;state=cc64574ce9734e5a8c1f357f4e030f18&amp;nonce=783f5ae1c70c43e2b5f13c2b0fadeed3'
url = 'https://luminus.nus.edu.sg/.php' # must be php, not static html

# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    result = s.get(url)
    #print(result.text)

    tree = html.fromstring(result.text)
    #list1 = list(set(tree.xpath("//input[@name='idsrv.xsrf']/@value"))) #empty thingy
    soup = BeautifulSoup(result.text, 'lxml')
    
    print(soup.prettify())
    #print(list1)
    #authenticity_token = list1[0]
    payload = {
    #'idsrv.xsrf': authenticity_token,
    'username': 'E0309299',
    'password': 'Santafete452014'
    }

    
   #page = s.post(url, data=payload)
    
    # print the html returned or something more intelligent to see if it's a successful login page.
    #print(page.text)

    # An authorised request
  
    
    #print(r.text)
        #etc...
