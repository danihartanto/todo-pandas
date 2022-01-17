from google_play_scraper import app
import pandas as pd
import numpy as np

#US Market

from google_play_scraper import Sort, reviews_all


us_reviews = reviews_all(
    'id.co.sevima.edlink',
    sleep_milliseconds=0, # defaults to 0
    lang='id', # defaults to 'en'
    country='id', # defaults to 'us'
    sort=Sort.NEWEST, # defaults to Sort.MOST_RELEVANT
)
df_busu = pd.DataFrame(np.array(us_reviews),columns=['review'])
df_busu = df_busu.join(pd.DataFrame(df_busu.pop('review').tolist()))
#print(df_busu.head())
#print(df_busu['score'].value_counts())
df_review_content = pd.DataFrame(df_busu, columns=['content','score'])
def xyz(x):
    if x>3:
        return 'positive'
    else:
        return 'negative'
s=df_review_content['score']
d=list(map(xyz,s))
df_review_content['score']=d

print(df_review_content.head(20))
df_review_content.to_csv("dataset-google-review-sevima-apps-sentimen.csv",index=False)
