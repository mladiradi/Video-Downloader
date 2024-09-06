import yt_dlp
import os


def get_video_link():
    return input("Enter the link of the YouTube video: ")


def get_desktop_path():
    return os.path.join(os.path.expanduser("~"), "Desktop")  # връща пътя до работния плот на потребителя


def download_video(link, download_path):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Взима най-доброто видео и аудио
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),  # Специфицира локацията на сваляне
        'merge_output_format': 'mp4'  # Обединява видео и аудио в mp4 файл
    }

    print("Downloading...")

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

    print("Download completed!!")


def main():
    link = get_video_link()
    desktop_path = get_desktop_path()
    download_video(link, desktop_path)


if __name__ == "__main__":
    main()
