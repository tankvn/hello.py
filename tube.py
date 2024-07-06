from pytube.cli import on_progress # this displays download progress in the console
from pytube import YouTube

# this is the handler/function for downloading the video
# the function takes the video url as an argument
def video_downloader(video_url):
    # passing the video url and progress_callback to the YouTube object
    my_video = YouTube(video_url, on_progress_callback=on_progress)
    # downloading the video in high resolution
    my_video.streams.get_highest_resolution().download()
    # return the video title
    return my_video.title

"""
    Running the code inside the try/except block
"""
try:
    # getting the url from the user
    # youtube_link = input('Enter the YouTube link:')
    youtube_link = input('https://www.youtube.com/watch?v=Xf7c3vHkNOM')
    print(f'Downloading your Video, please wait.......')
    # passing the url to the function
    video = video_downloader(youtube_link)
    # printing the video title
    print(f'"{video}" downloaded successfully!!')

except:
    print(f'Failed to download video')
