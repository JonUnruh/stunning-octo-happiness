 import pandas as pd
df = pd.read_csv('american-election-tweets.csv', sep=';', encoding = 'iso8859-1')
df2 = df.drop(["source_url"], axis = 1) #entfernt Spalte "source_url"
df3 = df2[df2.truncated != True]  #entfernt alle gekürzten Tweets
df3 = df3.drop(["truncated"], axis=1) #entfernt Spalte "truncated"
df3.to_csv('amelec-filtered.csv', sep=';', encoding = 'iso8859-1')
