#!/usr/bin/env python3

import sys
import os

from transformers import pipeline

pipe = pipeline("text-classification", model="nlptown/bert-base-multilingual-uncased-sentiment")


files = os.listdir("./descriptions")
for file in files:
    with open('./descriptions/'+file, 'r') as f:
        text = f.read()
        result= pipe(text, top_k=1, truncation=True)
        print(file, result)
