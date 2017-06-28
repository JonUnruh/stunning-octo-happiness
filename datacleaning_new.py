"""
Created on Tue May 30 14:38:49 2017

@author: Olaf
"""
import pandas as pd
df = pd.read_csv('american-election-tweets.csv', sep=';', encoding = 'latin-1')
df2 = df.drop(["source_url"], axis = 1)
df3 = df2[df2.truncated != True]
df3 = df3.drop(["truncated"], axis=1)
df3.to_csv('amelec-filtered.csv', sep=';', encoding = 'latin-1')
p = df2.loc[: , "text"]
pf = pd.DataFrame({'Inhalt' : []})
gf = pd.DataFrame({'Tweet-ID' : [], 'Vorkommen' : [], 'HashtagID' : []})
k = p.shape[0]
for x in range(0, k):
    tags = p.get_value(x, 'text').lower()
    hashtags = {tag.strip("#") for tag in tags.split() if tag.startswith("#")}
    for y in hashtags:
        if (y in pf.values):
            zu = (pf['Inhalt'] == y).argmax()
            rf = pd.DataFrame({'Tweet-ID': [x], 'Vorkommen' : [df2.get_value(x,'time')], 'HashtagID' : [zu]})
            framex = [gf, rf]
            gf = pd.concat(framex, ignore_index=True)
        else:
            ef = pd.DataFrame({'Inhalt': [y]})
            frames = [pf, ef]
            pf = pd.concat(frames, ignore_index=True)
            rf = pd.DataFrame({'Tweet-ID': [x], 'Vorkommen' : [df2.get_value(x,'time')], 'HashtagID' : [pf.shape[0] - 1]})
            framex = [gf, rf]
            gf = pd.concat(framex, ignore_index=True)
pf = pf.drop([325])
gf = gf.drop([1117])
pf.to_csv('amelec-hashtag.csv', sep=';', encoding = 'latin-1')
gf.to_csv('amelec-vorkommen.csv', sep=';', encoding = 'latin-1')