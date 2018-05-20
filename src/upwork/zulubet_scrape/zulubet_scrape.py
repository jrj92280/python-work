import urllib.request

from bs4 import BeautifulSoup

page_url = 'http://de.zulubet.com/tipps-01-01-2016.html'

request = urllib.request.Request(page_url)
page = urllib.request.urlopen(request)

soup = BeautifulSoup(page)

content_table = soup.find('table', attrs={'class': 'content_table'})

game_data = []

for index, row in enumerate(content_table.contents):
    if index <= 1:
        continue

    for row_column, td in enumerate(row.contents):
        if row_column == 0:
            # 'mf_usertime(\\'01/01/2016, 05:15\\');01-01, 06:15'
            td_data = td.text.split("'")
            game_data.append(td_data[1])

        # print(str(row_column) + "_" + str(td))

    # print(str(index) + "_" + str(row))
print(game_data)
