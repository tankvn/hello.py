from pytube import YouTube

url = "https://www.youtube.com/watch?v=Xf7c3vHkNOM"
YouTube(url).streams.get_highest_resolution().download()