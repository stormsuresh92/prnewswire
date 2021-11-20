from requests_html import HTMLSession
import pandas as pd
from alive_progress import alive_bar
from time import sleep


data = []
def page(x):
    s = HTMLSession()
    url = f'https://www.prnewswire.com/news-releases/news-releases-list/?page={x}&pagesize=100'
    r = s.get(url)
    content = r.html.find('div.row.arabiclistingcards')
    with alive_bar(len(content), title=f'Getting page {x}', bar='classic2', spinner='classic') as bar:
        for item in content:
            try:
                date_time = item.find('h3', first=True).text.split('ET')[-2]
            except:
                date_time = ''
            try:
                title = item.find('h3', first=True).text.split('ET')[-1]
            except:
                title = ''
            try:
                url = 'https://www.prnewswire.com' + item.find('a.newsreleaseconsolidatelink', first=True).attrs['href']
            except:
                url = ''
            dic = {
                'Date_Time':date_time,
                'Title':title,
                'Urls':url
            }
            data.append(dic)
            sleep(0.2)
            bar()

endpage = int(input('Enter end page:'))
for x in range(1, endpage):
    page(x)
    
df = pd.DataFrame(data)
df.to_csv('Outputfile.csv', index=False)
print('\n')
print('file downloaded') 
input()
