import pandas as pd
import datetime

#Configurate Files Name
input_file = 'youtube_comments.csv'
output_file = 'youtube_comments_clean.csv'

print(f'Sedang membaca input file: {input_file}')

# 1. Read Csv File
try:
    df = pd.read_csv(input_file)
except FileNotFoundError:
    print("ERORR : File tidak ditemukan! pastikan nama file dan lokasinya benar.")
    exit()

# 2. Time Format Clean (TIMESTAMP)
print('Sedang memperbaiki format waktu.....')
# Converts (Unix) seconds to a readable Date
df['tanggal_baca'] = pd.to_datetime(df['timestamp'],unit='s')
# Convert to Western Indonesian Time Standard (+7 Hours)
df['tanggal_baca'] = df['tanggal_baca'] + pd.Timedelta(hours=7)

#3. Clean Text (Mojibake Fix)
print('Sedang memperbaiki karakter aneh(mojibake).....')

def text_fix(text):
    if not isinstance(text, str):
        return text
    try:
        return text.encode('cp1252').decode('utf-8')
    except:
        return text
    
# Apply fixes to 'text' and 'author' columns
df['clean_text'] = df['text'].apply(text_fix)
df['clean_author'] = df['author'].apply(text_fix)

# 4. Delete Duplicate
print("Sedang mengecek data ganda......")
jumlah_awal = len(df)
# Delete rows if comment id is similar
df = df.drop_duplicates(subset=['id'])
jumlah_hapus = jumlah_awal - len(df)

if jumlah_hapus > 0:
    print(f'Berhasil membuang {jumlah_hapus} data duplikar')
else:
    print('Data bebas dari duplikat')

#5. Save Output
final_column = ['tanggal_baca','clean_author','clean_text','like_count','id']
df_final = df[final_column]

# Save into new csv
df_final.to_csv(output_file,index=False,encoding='utf-8-sig')

print("\n" + "="*40)
print("PROSES SELESAI!")
print(f"File bersih tersimpan sebagai: {output_file}")
print(f"Total data siap analisis: {len(df_final)} baris")
print("="*40)


