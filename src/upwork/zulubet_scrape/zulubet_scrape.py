import urllib.request

from bs4 import BeautifulSoup

page_url = 'http://de.zulubet.com/tipps-01-01-2016.html'

request = urllib.request.Request(page_url)
page = urllib.request.urlopen(request)

soup = BeautifulSoup(page)

content_table = soup.find('table', attrs={'class': 'content_table'})

print(content_table)
