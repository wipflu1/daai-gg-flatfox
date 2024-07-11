import pandas as pd
from transformers import pipeline

print('exectuted py')

df=pd.read_csv('flatfox.csv')
df=df[['pk','description']]
df = df.replace('[^\w\s]','', regex=True)
df.head()

pipe = pipeline("text-classification", model="nlptown/bert-base-multilingual-uncased-sentiment")
results=[]

for index, row in df.iterrows():
    text = str(row['description'])

    try:
        result= pipe(text, top_k=1, truncation=True)
        results.append(result)
        print(index)
    except:
        print(text)
df['SentimentValue'] = results

df.to_csv("pk-description-sentimentValue.csv",index=False, quoting=csv.QUOTE_NONNUMERIC ,quotechar='"', lineterminator='!')
df=df[['pk','sentimentValue']]
df.to_csv("pk-sentimentValue.csv", index=False,)
