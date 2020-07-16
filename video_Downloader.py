from pytube import YouTube


def download_video(link, save_path):
    yt = YouTube(link)
    stream = yt.streams.first()
    print(yt.views)
    stream.download(save_path)
