#!/usr/bin/env python
# coding: utf-8

# In[17]:


import bs4,requests,csv
url="https://gamewith.tw/monsterstrike/article/show/85531"
response =requests.get(url)
soup=bs4.BeautifulSoup(response.text,"lxml")
bag=soup.find('table',class_='sorttable')
tag=bag.find_all('tr')
po=[]
for data in tag:
    dd=[]
    for ct in data:
        dd.append(ct.text)
    po.append(dd[0:5:2])
with open('output_new.csv','w', newline='',encoding='UTF-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(po)


# In[18]:


df = pd.read_csv('output_new.csv')
select_df = pd.DataFrame(df)
df[df['評分'] == 10.0]


# In[20]:


df = pd.read_csv('output_new.csv')
select_df = pd.DataFrame(df)
s=df[df['撃種']=='反射']
s


# In[25]:


s.sort_values(by = '評分',ascending = False)


# In[ ]:




