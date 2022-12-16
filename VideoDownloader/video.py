from pytube import YouTube
link = input("URL:");
yt = YouTube(link);
yt.streams.first().download();
print('Dowloaded', link)