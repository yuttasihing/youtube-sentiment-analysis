import pandas as pd

# Read .csv data
file_name = 'youtube_comments_clean.csv'
df = pd.read_csv(file_name)

#Calculating Wordcount
df['word_count'] = df['clean_text'].apply(lambda x: len(str(x).split()))

#Saved Data
file_output = 'youtube_comments_with_wordcount.csv'
df.to_csv(file_output, index=False)

print(f"--- PROSES BERHASIL ---")
print(f"Total Baris Diproses: {len(df)}")
print(f"Rata-rata Kata per Komentar: {df['word_count'].mean():.2f} kata")
print(f"File Output: {file_output}")
      
