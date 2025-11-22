import argparse
from pytube import YouTube
from pytube.cli import on_progress

def download_video(url, output_path, resolution):
    """
    Downloads a YouTube video.

    Args:
        url (str): The URL of the YouTube video.
        output_path (str): The path to save the video.
        resolution (str): The desired resolution (e.g., "720p", "1080p").
                          If None, the highest resolution is chosen.
    """
    try:
        print(f"Connecting to YouTube...")
        yt = YouTube(url, on_progress_callback=on_progress)

        print(f"Fetching streams for '{yt.title}'...")
        if resolution:
            stream = yt.streams.filter(res=resolution, progressive=True).first()
            if not stream:
                print(f"Resolution {resolution} not available for this video.")
                print("Falling back to the highest available resolution.")
                stream = yt.streams.get_highest_resolution()
        else:
            stream = yt.streams.get_highest_resolution()

        if not stream:
            print("No suitable stream found for this video.")
            return

        print(f"Downloading: {yt.title}")
        print(f"Resolution: {stream.resolution}")
        print(f"File size: {stream.filesize / 1_000_000:.2f} MB")
        print(f"Saving to: {output_path}")

        stream.download(output_path=output_path)
        print("\nDownload completed successfully!")

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
        help="The desired video resolution (e.g., '720p', '1080p'). Defaults to the highest available.",
    )

    args = parser.parse_args()

    download_video(args.url, args.path, args.resolution)
