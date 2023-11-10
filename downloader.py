
# YT Downloader Project # 

from pytube import YouTube

link = input("Enter a YouTube video URL: ") # Enter a YouTube video URL

try:
    
    yt = YouTube(link) # YouTube object

    print("Title:", yt.title) # YouTube title
    print("Description:", yt.description) # YouTube description
    print("Views:", yt.views) # YouTube views
    
    install = yt.streams.get_highest_resolution() # Get the highest resolution of video 

    download_path = r' ' # Input your own download path before using program, otherwise the program will not work properly 

    install.download(output_path=download_path) # Download the video

    print("Video downloaded successfully to:", download_path) # Video downloaded successfully to: (Path that you inputted)
except Exception as e:
    print("Error occurred:", str(e)) # Chances are that you made a mistake in the path that you inputted 

