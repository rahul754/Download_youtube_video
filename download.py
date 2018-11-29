#https://www.youtube.com/watch?v=kp1xseNLYAM  link to download video

from pytube import YouTube

#path, where do you install your video in system
SAVE_PATH = "/video"

#youtube link
link = "https://www.youtube.com/watch?v=MYPVmvui_dc"

#creating a object from pytube module
yt = YouTube(link)

#which stream do you select. here two option first() / all()
stream = yt.streams.first()

#print video title 
print(yt.title)

#set path, where your video will install
stream.download('video')

#show video download progress/ set file extension mp4
yt.streams.filter(progressive=True,adaptive=True,file_extension='mp4').first()

