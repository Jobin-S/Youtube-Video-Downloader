from pytube import YouTube


def download_video(link, save_path):
    yt = YouTube(link)
    stream = yt.streams.first()
    stream.download(save_path)
