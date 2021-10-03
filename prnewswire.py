from requests_html import HTMLSession
import pandas as pd


data = []
def page(x):
    s = HTMLSession()
    url = f'https://www.prnewswire.com/news-releases/news-releases-list/?page={x}&pagesize=100'
    r = s.get(url)
    content = r.html.find('div.row.arabiclistingcards')
    for item in content:
        date_time = item.find('h3', first=True).text.split('ET')[-2]
        title = item.find('h3', first=True).text.split('ET')[-1]
        url = 'https://www.prnewswire.com' + item.find('a.newsreleaseconsolidatelink', first=True).attrs['href']
        dic = {
            'Date_Time':date_time,
            'Title':title,
            'Url':url
        }
        data.append(dic)
    return data

for x in range(1, 4):
    page(x)
    
df = pd.DataFrame(data)
df.to_csv('output.csv', index=False)
print('file downloaded') 