import csv
from yt_dlp import YoutubeDL

video_url = "https://www.youtube.com/watch?v=2rBf7I8nK1g"

opts = {
    "getcomments": True,
    "skip_download": True,
    "quiet": True,
    "no_warnings": True,
    "ignore_no_formats_error": True,
    "format": "best",
    "extractor_args": {
        "youtube": {
            "max_comments": ["all"],
            "player_client": ["web"],
        }
    }
}

with YoutubeDL(opts) as yt:
    info = yt.extract_info(video_url, download=False)

thread_count = info.get("comment_count") or info.get("n_comment") or 0
comments = info.get("comments") or info.get("comment_entries") or []

rows = []
for c in comments:
    rows.append({
        "id": c.get("id"),
        "author": c.get("author"),
        "author_id": c.get("author_id"),
        "text": c.get("text"),
        "timestamp": c.get("timestamp"),
        "like_count": c.get("like_count")
    })

with open("youtube_comments.csv","w",newline="",encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["id","author","author_id","text","timestamp","like_count"])
    writer.writeheader()
    writer.writerows(rows)

print(f"number of top-level comments reported: {thread_count}")
print(f"Saved {len(rows)} comments to youtube_comments.csv")