# 📊 YouTube Sentiment Analysis: Unveiling Political Rhetoric & Cyber Operations

A data journalism pipeline built with Python to extract, process, and analyze public discourse from YouTube comments. This project specifically examines the audience's cognitive map and political polarization in response to the "Antek Asing" (Foreign Agent) political rhetoric discussed in a political podcast. 

Beyond standard sentiment analysis, this project acts as a digital forensic tool that successfully identifies organized cyber operations (buzzers) utilizing **text obfuscation** tactics to manipulate public opinion and bypass algorithmic spam filters.

## 🗂️ Data Pipeline Architecture

This repository contains the end-to-end data extraction and natural language processing (NLP) workflow, divided into 6 sequential Python scripts:

* **`01_scrapping_yt_comments.py`**
  Automated data acquisition script utilizing the `yt-dlp` API to scrape raw comments, including metadata such as author IDs, timestamps, text, and like counts from the target YouTube video.
* **`02_cleaner_machine.py`**
  Data pre-processing engine using `pandas` and `datetime`. It handles mojibake character cleaning, UNIX timestamp conversion to local time zones, and duplicate data filtering.
* **`03_wordcount_machine.py`**
  Calculates the frequency of specific vocabulary to measure the penetration of political rhetoric at the grassroots level.
* **`04_unigram_bigram.py`**
  Extracts N-Grams (unigrams and bigrams) using `re` and `Counter` to map the dominant narratives framing the audience's discourse.
* **`05_wordcloud_machine.py`**
  Generates static visual representations of the most prominent terms and cognitive focus of the audience using `matplotlib` and `wordcloud`.
* **`06_sentiment_analysis_machine.py`**
  A sentiment labeling machine utilizing a custom political slang lexicon to accurately score and categorize the sentiment of each comment in the context of Indonesian political discourse.

## 💡 Key Investigative Findings

1. **The Echo Chamber Effect:** Discovered a highly concentrated narrative where approximately 1% of the most active participants monopolized 11% of the total discourse volume.
2. **Text Obfuscation Tactics:** Uncovered coordinated attempts by anomalous accounts (buzzers) to bypass YouTube's duplicate content filters by subtly mutating text characters, deliberately injecting anti-media narratives (e.g., MDIF, George Soros).
3. **Engagement Anomalies:** Statistical analysis (R² = 0.0018) revealed that extreme sentiment scores do not correlate with high social validation (likes). The "silent majority" tends to validate structured, ironic criticism rather than blind rage.

## 🛠️ Tech Stack & Requirements

* **Language:** Python 3.x
* **Libraries:** `pandas`, `matplotlib`, `wordcloud`, `yt-dlp`

To run the scripts in this repository locally, install the required dependencies:

```bash
pip install -r requirements.txt
