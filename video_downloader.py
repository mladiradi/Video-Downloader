
import yt_dlp

# Ask user to type in the link
link = input("Enter the link of the YouTube video: ")

# Define the download options
ydl_opts = {
    'format': 'bestvideo+bestaudio/best',  # Get the highest resolution video
    'outtmpl': 'Downloads/python_mp4/%(title)s.%(ext)s',  # Specify download location
    'merge_output_format': 'mp4'  # Merge video and audio into an mp4 file
}

# Show the message until downloading
print("Downloading...")

# Create the downloader object and download the video
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])

# Show the message when download is completed
print("Download completed!!")
