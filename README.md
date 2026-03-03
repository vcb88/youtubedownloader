# YouTube Downloader

A simple, yet powerful command-line utility to download YouTube videos, now powered by `yt-dlp` for superior reliability and performance.

### 📚 Detailed Documentation
For a full guide on advanced usage, custom resolutions (1080p, 4K), and common troubleshooting, see the **[USER_GUIDE.md](USER_GUIDE.md)**.

---

## 🚀 Quick Help

### 1. Installation
```bash
git clone https://github.com/vcb88/youtubedownloader.git
cd youtubedownloader
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### 2. Basic Usage (720p Default)
```bash
python3 download.py "URL"
```

### 3. High Resolution (1080p/4K)
*Requires `ffmpeg` installed on your system.*
```bash
python3 download.py "URL" --resolution 1080p
python3 download.py "URL" --resolution 2160p
```

---

## 🐳 Docker Support

If you don't want to install dependencies locally:
1.  **Build:** `docker build -t yt-down .`
2.  **Run:** `docker run --rm -v $(pwd)/downloads:/app/downloads yt-down "URL" --path /app/downloads`

---

## 🛠 Features
- **Reliable:** Migrated from `pytube` to `yt-dlp`.
- **Flexible:** Custom output paths and resolutions.
- **Robust:** Automatic directory creation and error handling.
- **Dockerized:** Ready for containerized environments.
