from pytube import YouTube
import os
def Download(link,choice):
    yt = YouTube(link)
    match choice:
        case 1:
            yt = yt.streams.filter(file_extension='mp4')
            yt = yt.first()
            try:
                print("Downloading file as video......")
                yt.download()
            except:
                print("Some error occured. Video couldn't be downloaded")
            print("Video downloaded successfully")
        case 2:
            try:
                print("Downloading file as audio.....")
                audio = yt.streams.filter(only_audio=True).first()
                audio = audio.download()
                base , ext = os.path.splitext(audio)
                new_file = base + '.mp3'
                os.rename(audio,new_file)
                print("Download successful")
            except:
                print("Mp3 file couldn't be downloaded")

link = input("Enter the link of the video : ")
print("Which format do you want to download - ")
print("1. mp4")
choice=int(input("2. mp3 : "))
Download(link,choice)

