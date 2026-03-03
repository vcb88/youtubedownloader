# YouTube Downloader: Comprehensive User Guide

This guide provides everything you need to know about using the YouTube Downloader efficiently. The tool uses `yt-dlp` under the hood for maximum reliability and speed.

## 🚀 Quick Start

If you have the environment set up, run:
```bash
python3 download.py "https://www.youtube.com/watch?v=XXXXXX"
```
By default, this downloads the **best combined resolution (usually 720p)** to the current directory.

---

## 🛠 Features

- **High Reliability:** Powered by `yt-dlp` to bypass common YouTube restrictions.
- **Custom Resolution:** Choose exactly what quality you want (720p, 1080p, 4k, etc.).
- **Automatic Organization:** Automatically creates directories if they don't exist.
- **Docker Support:** Run in an isolated container without installing Python locally.

---

## 📖 Command Line Options

| Flag | Long Flag | Description | Default |
| :--- | :--- | :--- | :--- |
| (None) | `url` | **Required.** The YouTube video URL. | N/A |
| `-p` | `--path` | Output directory path. | `./` |
| `-r` | `--resolution` | Desired height (e.g., `1080p`). | `best` (720p) |

### Advanced Resolution Examples
The `--resolution` flag is smart. If you ask for `1080p` and it's not available, it will fetch the next best thing.

- **Download 4K:**
  ```bash
  python3 download.py "URL" --resolution 2160p
  ```
- **Download 1080p:**
  ```bash
  python3 download.py "URL" --resolution 1080p
  ```

---

## 🐳 Docker Deployment

The cleanest way to run the downloader is using Docker. This avoids dependency conflicts on your host machine.

### 1. Build the Image
```bash
docker build -t yt-down .
```

### 2. Run the Container
To save files to your host machine, you **must mount a volume**.

**MacOS/Linux:**
```bash
docker run --rm -v "$(pwd)/test_downloads:/app/downloads" yt-down "URL" --path /app/downloads
```

---

## ❓ Troubleshooting

### Connection Errors (403 Forbidden)
YouTube occasionally blocks automated tools. Since we use `yt-dlp`, the best fix is usually ensuring your local `yt-dlp` is up to date:
```bash
pip install -U yt-dlp
```

### Missing FFmpeg
For resolutions higher than 720p (like 1080p or 4K), YouTube serves video and audio separately. `yt-dlp` needs `ffmpeg` to merge them.
- **Install on Mac:** `brew install ffmpeg`
- **Install on Ubuntu:** `sudo apt install ffmpeg`

### "Slow Downloads"
YouTube throttles download speeds for known bot signatures. `yt-dlp` handles most of this, but ensure you are not behind a heavily congested VPN or proxy.

---

## 📝 Best Practices

1.  **Use Quotes:** Always wrap the URL in double quotes (`" "`) to avoid shell errors with special characters like `&` or `?`.
2.  **Absolute Paths:** When using the `--path` flag, using absolute paths (e.g., `/Users/name/Downloads`) is safer than relative ones.
3.  **Check Available Formats:** If a specific resolution fails, the video might not support it. Use `yt-dlp -F URL` in your terminal to see exactly what YouTube offers for that specific video.
