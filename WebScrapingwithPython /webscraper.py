import pandas as pd

scraper = pd.read_html("https://en.wikipedia.org/wiki/Bangladesh")

scraper
#for i , table in enumerate(scraper):
    #print("-----")
    #print(i)
    #print(table)

scraper[0]

df =scraper[0]
df.to_csv('premier_leangue.csv', index = False)
df_scraped_file = pd.read_csv('premier_langue.csv')
df_scraped_file