"""
Author: Lame MAphuru
The ambition of this project is to act as a mini engine for searching through Botswana Government website and it's parastatals 
for Job postings so that job search is not a tedious manual navigation of government websites. The goals is to eventually have 
robust code that can be used for general purpose search of the BW government website.
"""

# Import all necessary libraries 
from urllib.request import urlopen
import ssl
from bs4 import BeautifulSoup

# The url of the website we are searching
serviceurl  = 'https://www.gov.bw/parastatals'

#ignore SSL certificate errors 
ctx = ssl.create_default_context()
ctx.check_hostname = False 
ctx.verify_mode = ssl.CERT_NONE

print('Retrieving', serviceurl)
html = urlopen(serviceurl, context = ctx).read()
soup = BeautifulSoup(html, "html.parser")
#print(soup.prettify)
tags = soup('a')
# Dictionary for parastatals and their web addresses 
parastatals = {}
links = []
names = []
data = soup.find_all(class_ = 'servicesmi')
for tag in data:
    link = tag.get('href', None)
    links.append(link)
    name = tag.text
    names.append(name)
    parastatals[name] = link

# Navigate to the next page and find more parastatals and their links.
#pager = soup.findall(class_ = 'pager')
print(parastatals)



