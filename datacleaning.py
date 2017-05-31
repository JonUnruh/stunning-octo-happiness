"""
Created on Tue May 30 14:38:49 2017

@author: Olaf
"""
import pandas as pd
df = pd.read_csv('american-election-tweets.csv', sep=';', encoding = 'iso8859-1')
print (df.shape)
df2 = df.drop(["source_url"], axis = 1)
print(df2.shape)
df3 = df2[df2.truncated != True]
df3 = df3.drop(["truncated"], axis=1)
print(df3)
df3.to_csv('amelec-filtered.csv', sep=';', encoding = 'iso8859-1')