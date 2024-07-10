#!/usr/bin/env python3

import sys
import os

from germansentiment import SentimentModel
from transformers import pipeline


model_ckpt = "papluca/xlm-roberta-base-language-detection"
pipe = pipeline("text-classification", model=model_ckpt)



germanModel = SentimentModel()
models = {}
models['de'] = germanModel

files = os.listdir("./descriptions")
for file in files:
    with open('./descriptions/'+file, 'r') as f:
        content = f.read()
        #print(content)
        lan=pipe(content, top_k=1, truncation=True)
        result,score = model[lan['label']].predict_sentiment([content], output_probabilities=True)
        print(file, lan, result,score)

