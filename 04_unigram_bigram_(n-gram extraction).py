import pandas as pd
import re
from collections import Counter

#1. Load Data
print('Reading Document.....')
df = pd.read_csv('youtube_comments_clean.csv')

#2. Filter Buzzer (Only add 1 comments from indicated buzzer)
buzzer_list = ['@Noor.M-mg8mo', '@ste4494', '@dimasseto7248']
buzzer_list_lower = [b.lower() for b in buzzer_list] 

# Seperate Non-buzzer data and buzzer data
df_non_buzzer = df[~df['clean_author'].str.lower().isin(buzzer_list_lower)]
df_buzzer = df[df['clean_author'].str.lower().isin(buzzer_list_lower)]

# Just adding 1 comment from indicated buzzer
df_buzzer_limited = df_buzzer.drop_duplicates(subset='clean_author',keep='first')

df_final = pd.concat([df_non_buzzer,df_buzzer_limited]).copy()
print(f'Total data processed after filter: {len(df_final)} baris')

# 3. Date Preprocessing
df_final['tanggal'] = pd.to_datetime(df_final['tanggal_baca']).dt.date

# 4. Stopwords list 
stopwords_indo = set([
    'yang', 'dan', 'di', 'itu', 'dengan', 'untuk', 'tidak', 'ini', 'dari', 
    'dalam', 'akan', 'pada', 'juga', 'saya', 'ke', 'karena', 'ada', 'bisa', 
    'apa', 'dia', 'kalau', 'atau', 'sudah', 'tapi', 'saja', 'adalah', 'kita',
    'mereka', 'kami', 'anda', 'kamu', 'aku', 'biar', 'lagi', 'mana', 'memang',
    'tentang', 'seperti', 'sangat', 'banyak', 'lebih', 'harus', 'oleh', 'saat',
    'masih', 'bukan', 'pun', 'jika', 'sebagai', 'maka', 'telah', 'kepada',
    'yg', 'gk', 'gak', 'ga', 'nggak', 'kalo', 'kl', 'klo', 'dr', 'sdh', 'udh', 'dah',
    'dg', 'dgn', 'sm', 'sama', 'tuh', 'nih', 'sih', 'kok', 'deh', 'dong', 'donk',
    'aja', 'aj', 'doang', 'bgt', 'banget', 'tu', 'utk', 'jd', 'jdi', 'jadi',
    'tp', 'tpi', 'gw', 'gue', 'lo', 'lu', 'elu', 'wkwk', 'wkwkwk', 'haha', 'hihi',
    'se', 'si', 'mas', 'mbak', 'pak', 'bu', 'kak', 'bang', 'bro', 'sis', 'min',
    'gan', 'om', 'tante', 'mah', 'kek', 'kayak', 'kyk', 'tau', 'tauk',
    'nya', 'ny', 'ya', 'y', 'o', 'oh', 'ah', 'ih', 'eh', 'hm', 'hmm', 
    's', 't', 'm', 'p', 'd', 'k', 'g', 'b', 'n', 
    'video', 'nonton', 'komen', 'komentar', 'channel', 'youtube', 'yt'
])

stopwords_indo.update([
    'dlm', 'segala', 'jgn', 'cuma', 'skrg', 'jg', 'krn', 'sering', 'sebenarnya', 
    'pasti', 'selama', 'perlu', 'agar', 'para', 'tak', 'pernah', 'udah', 'kali', 
    'hal', 'cara', 'hanya', 'tdk', 'kenapa', 'sebuah', 'makin', 'justru', 'demi', 
    'spt', 'bagi', 'kan', 'bikin', 'ternyata', 'a', 'emang', 'dapat', 'mungkin', 
    'sampe', 'benar', 'of', 'justru', 'mudah', 'lain', 'sekali', 'sering', 'siapa', 
    'apakah', 'yaa', 'nanti', 'bahwa', 'trus', 'membuat', 'punya', 'org', 'sedang', 
    'buat', 'bener', 'paling'
])

# Text Cleaner Function
def text_cleaner(text):
    text = str(text).lower()
    text = re.sub(r'[^a-z\s]', '', text)
    token = text.split()
    # Just Putting word is not in stopwords and have a >2 length
    return [w for w in token if w not in stopwords_indo and len(w) > 2]

# 6. Processing N-Gram by date
print('Processing N-Gram by date')
unigram_rows = []
bigram_rows = []

#Grouping by date
for date, group in df_final.groupby('tanggal'):
    all_tokens = []
    all_bigram = []

    for comment in group['clean_text']:
        clean_words = text_cleaner(comment)
        all_tokens.extend(clean_words)

        #Bigram
        bg = [" ".join(pair) for pair in zip(clean_words, clean_words[1:])]
        all_bigram.extend(bg)

    #Calculated 50 words most in evwey date
    uni_counts = Counter(all_tokens).most_common(50)
    bi_counts = Counter(all_bigram).most_common(50)

    #putting into output list
    for p, f in uni_counts: unigram_rows.append({'tanggal':date, 'phrase': p, 'frekuensi':f})
    for p, f in bi_counts: bigram_rows.append({'tanggal':date, 'phrase': p, 'frekuensi':f})

    # 7. SAVE OUTPUT
pd.DataFrame(unigram_rows).to_csv('unigram_per_date.csv', index=False)
pd.DataFrame(bigram_rows).to_csv('bigram_per_date.csv', index=False)

print('Finish')
    


     
