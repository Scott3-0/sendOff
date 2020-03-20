import requests
import lxml.html as lh
import pandas as pd

letter = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
url = 'http://www.univsearch.com/name-search.php?alpha='

for i in range(0,26):
    #Create a handle, page, to handle the contents of the website
    page = requests.get(url+letter[i])
    #Store the contents of the website under doc
    doc = lh.fromstring(page.content)

    #Parse data that are stored between <tr>..</tr> of HTML
    tr_elements = doc.xpath('//tr')

    #Create empty list
    col=[]

    #For each row, store each first element (header) and an empty list
    for t in tr_elements[0][0][1]:
        name=t[0].text_content()
        #print('%s'%(name)) #for debug
        col.append(name)

    df = pd.DataFrame(col)
    df.to_csv('out'+letter[i]+'.csv', index=False, header=True)
    print(df)
