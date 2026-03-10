import pandas as pd
import re

#Load Data
lexicon_df = pd.read_csv('lexicon_camus_update2.csv',sep=';')
lexicon_dict = dict(zip(lexicon_df['Phrase(tokenization)'], lexicon_df['sentimen']))

#Read Comments Dataset
df = pd.read_csv('youtube_comments_with_wordcount.csv')

#2. Function Sentiment Calculated
def calculate_sentiment(text, lexicon):
    if pd.isna(text) : return 0
    # Normalize Text to match with lexicon
    text = str(text).lower()
    text = re.sub(r'[^a-z\s]','',text)
    tokens = text.split()

    #Calculated Total Score Based on Camus
    score = 0
    for token in tokens:
        if token in lexicon:
            score += lexicon[token]

    return score

#Label Execution
df['score'] = df['clean_text'].apply(lambda x : calculate_sentiment(x, lexicon_dict))

#Categorize
def categorize(score):
    if score > 0: return 'Positif'
    elif score < 0: return 'Negatif'
    else: return 'Netral'

df['sentiment'] = df['score'].apply(categorize)

#Output Saved
output_cols = ['tanggal_baca','id','clean_author','clean_text','score','sentiment']
df[output_cols].to_csv('sentiment_analysis_final.csv',index=False)
