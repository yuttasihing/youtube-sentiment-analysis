import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Input File
input_file = 'youtube_comments_clean.csv'

# Daftar Akun Indikasi Buzzer
indikasi_buzzer = [
    '@Noor.M-mg8mo', 
    '@ste4494', 
    '@dimasseto7248'
]

# Penghilangan kata sambung 
stopwords_indo = set([
    # 1. KATA HUBUNG & GANTI (Standar)
    'yang', 'dan', 'di', 'itu', 'dengan', 'untuk', 'tidak', 'ini', 'dari', 
    'dalam', 'akan', 'pada', 'juga', 'saya', 'ke', 'karena', 'ada', 'bisa', 
    'apa', 'dia', 'kalau', 'atau', 'sudah', 'tapi', 'saja', 'adalah', 'kita',
    'mereka', 'kami', 'anda', 'kamu', 'aku', 'biar', 'lagi', 'mana', 'memang',
    'tentang', 'seperti', 'sangat', 'banyak', 'lebih', 'harus', 'oleh', 'saat',
    'masih', 'bukan', 'pun', 'jika', 'sebagai', 'maka', 'telah', 'kepada',
    
    # 2. BAHASA GAUL / SINGKATAN (Slang Netizen)
    'yg', 'gk', 'gak', 'ga', 'nggak', 'kalo', 'kl', 'klo', 'dr', 'sdh', 'udh', 'dah',
    'dg', 'dgn', 'sm', 'sama', 'tuh', 'nih', 'sih', 'kok', 'deh', 'dong', 'donk',
    'aja', 'aj', 'doang', 'bgt', 'banget', 'tu', 'utk', 'jd', 'jdi', 'jadi',
    'tp', 'tpi', 'gw', 'gue', 'lo', 'lu', 'elu', 'wkwk', 'wkwkwk', 'haha', 'hihi',
    'se', 'si', 'mas', 'mbak', 'pak', 'bu', 'kak', 'bang', 'bro', 'sis', 'min',
    'gan', 'om', 'tante', 'mah', 'kek', 'kayak', 'kyk', 'tau', 'tauk',
    
    # 3. KATA SAMPAH SPESIFIK HASIL OBSERVISASI (Noise)
    'nya', 'ny', 'ya', 'y', 'o', 'oh', 'ah', 'ih', 'eh', 'hm', 'hmm', 
    's', 't', 'm', 'p', 'd', 'k', 'g', 'b', 'n', 
    'video', 'nonton', 'komen', 'komentar', 'channel', 'youtube', 'yt'
])

stopwords_indo.update(['dlm', 'segala', 'jgn', 'cuma', 'skrg', 'jg', 'krn', 'sering', 'sebenarnya', 
                       'pasti', 'selama', 'perlu', 'agar', 'para', 'tak', 'pernah', 'udah', 'kali', 
                       'hal', 'cara', 'hanya', 'tdk', 'kenapa', 'sebuah', 'makin', 'justru', 'demi', 
                       'spt', 'bagi', 'kan', 'bikin', 'ternyata', 'a', 'emang', 'dapat', 'mungkin', 
                       'sampe', 'benar', 'of', 'justru', 'mudah', 'lain', 'sekali', 'sering', 'siapa', 
                       'dlm', 'ternyata', 'cara', 'hanya', 'apakah', 'bagi', 'yaa', 'dari', 'nanti', 'bahwa', 
                       'trus', 'membuat', 'sebenarnya', 'punya', 'agar', 'bikin', 'dapat', 'sebuah', 'org', 'krn', 
                       'sedang', 'buat', 'bener', 'contoh', 'udah', 'kali', 'paling', 'cuma', 'jg', 'selama', 'dari'
                       ])

print('membaca data.....')  
df = pd.read_csv(input_file)

# Wordcloud Function
def make_wordcloud(teks_list, judul, nama_file):
    # Gabungan komentar jadi 1
    teks_gabungan = ' '.join(str(t) for t in teks_list).lower()

    #Generated Wordcloud
    wc = WordCloud(
        width=800, height=400,
        background_color='black',
        stopwords=stopwords_indo,
        colormap='bone' if 'Buzzer' in judul else 'bone',
        min_font_size=10
    ).generate(teks_gabungan)

    # Plotting 
    plt.figure(figsize=(10,5))
    plt.imshow(wc,interpolation='bilinear')
    plt.axis('off')
    plt.title(judul, fontsize=15, pad=20)
    plt.savefig(nama_file)
    print(f'gambar disinmpan: {nama_file}')
    plt.close()

#Skenario 1 : Data Kotor 
print("\n[1/2] Membuat Wordcloud versi kotor (FULLBUZZER)")

#generated wordcloud kotor :
text_kotor = df['clean_text']
make_wordcloud(text_kotor,"Word Cloud Dominasi Narasi Buzzer","wordcloud_buzzer1.png")

# --- SKENARIO 2: DATA BERSIH (TANPA BUZZER & DUPLIKAT) ---
print("\n[2/2] Membuat Word Cloud Versi BERSIH (Suara Organik)...")

# Menghilangkan komen dari indikasi buzzer
filter_buzzer = ~df['clean_author'].str.lower().isin([b.lower() for b in indikasi_buzzer])
df_bersih = df[filter_buzzer]

df_bersih['text_norm'] = df_bersih['clean_author'].str.lower().str.strip()
df_bersih = df_bersih.drop_duplicates(subset=['text_norm'])

print(f'statistik pembersihaan dari {len(df)} -> {len(df_bersih)}')

#Wordcloud untuk data bersih dari indikasi buzzer

text_bersih = df_bersih['clean_text']
make_wordcloud(text_bersih,'Wordcloud : Narasi Publik', 'wordcloud_bersih1.png')

print("\nSELESAI! Silakan cek 2 gambar PNG yang muncul di folder Anda.")
