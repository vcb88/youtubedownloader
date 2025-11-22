# YouTube Downloader

A simple, yet powerful command-line utility to download YouTube videos.

## Description

This script allows you to download videos from YouTube by providing a URL. You can specify the output path and the desired video resolution.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/vcb88/youtubedownloader.git
    cd youtubedownloader
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

The script is run from the command line. The only required argument is the YouTube video URL.

**Basic Usage:**
Downloads the video in the highest available resolution to the current directory.
```bash
python3 download.py "YOUTUBE_VIDEO_URL"
```

**Specify Output Path:**
Use the `--path` flag to save the video to a specific directory.
```bash
python3 download.py "YOUTUBE_VIDEO_URL" --path /path/to/your/videos/
```

**Specify Resolution:**
Use the `--resolution` flag to download the video in a specific resolution (e.g., `720p`, `1080p`). If the specified resolution is not available, the script will fall back to the highest available resolution.
```bash
python3 download.py "YOUTUBE_VIDEO_URL" --resolution 720p
```

## Docker Usage

You can also run this utility in a Docker container.

1.  **Build the Docker image:**
    ```bash
    docker build -t youtube-downloader .
    ```

2.  **Run the container:**
    To download a video, you need to mount a local directory to the container to store the downloaded file.

    ```bash
    docker run --rm -v $(pwd)/videos:/app/videos youtube-downloader "YOUTUBE_VIDEO_URL" --path /app/videos
    ```
    *   This command mounts a `videos` directory from your current working directory into the container.
    *   The `--rm` flag automatically removes the container when it exits.
    *   Make sure to create the `videos` directory first: `mkdir videos`.
