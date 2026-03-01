import argparse
import yt_dlp
import os

def download_video(url, output_path, resolution):
    """
    Downloads a YouTube video using yt-dlp.

    Args:
        url (str): The URL of the YouTube video.
        output_path (str): The path to save the video.
        resolution (str): The desired resolution (e.g., "720p", "1080p").
                          If None, the highest resolution is chosen.
    """
    try:
        print(f"Connecting to YouTube (via yt-dlp)...")
        
        # Mapping resolution to yt-dlp format
        # Best video + best audio if resolution not specified
        format_str = f"bestvideo[height<={resolution[:-1]}]+bestaudio/best[height<={resolution[:-1]}]" if resolution else "best"

        ydl_opts = {
            'format': format_str,
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'quiet': False,
            'no_warnings': False,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            print(f"\nDownload completed successfully: {filename}")

    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YouTube Video Downloader")
    parser.add_argument("url", help="The URL of the YouTube video to download.")
    parser.add_argument(
        "--path",
        default=".",
        help="The output path to save the video. Defaults to the current directory.",
    )
    parser.add_argument(
        "--resolution",
        default=None,
        help="The desired video resolution (e.g., '720p', '1080p'). Defaults to the best available.",
    )

    args = parser.parse_args()

    # Ensure output path exists
    if not os.path.exists(args.path):
        os.makedirs(args.path)

    download_video(args.url, args.path, args.resolution)
