from pytube import YouTube, Playlist, Channel
from pytube.cli import on_progress


def titulo(msg=''):
    print('-' * len(msg))
    print(f'{msg:^25}')
    print('-' * len(msg) )


def baixar_video():
    url = input("Insira a url do video que deseja baixar -> ")
    yt = YouTube(url, on_progress_callback=on_progress)
    print("Titulo = ", yt.title)
    print("Baixando...")
    video = yt.streams.get_highest_resolution()
    video.download()


def baixar_audio():
    url = input('Insira a url do video que deseja baixar o audio -> ')
    yt = YouTube(url, on_progress_callback=on_progress)
    print("Titulo = ", yt.title, ".mp3")
    print("Baixando...")
    audio = yt.streams.filter(only_audio=True)[0]
    audio.download()
    print("Completo!")


def baixar_playlist():
    url = input('Insira a url da Playlist que deseja baixar -> ')
    playlist = Playlist(url)
    for url in playlist:
        video = YouTube(url, on_progress_callback=on_progress)
        print("Titulo = ", video.title)
        print("Baixando...")
        video_playl = video.streams.get_highest_resolution()
        video_playl.download(output_path='Playlist')
        print("Completo!")


def baixar_channel():
    url = input('Insira a url do Canal que deseja baixar -> ')
    chanel = Channel(url)
    for url in chanel:
        video = YouTube(url, on_progress_callback=on_progress)
        print("Titulo = ", video.title)
        print("Baixando...")
        video_chan = video.streams.get_highest_resolution()
        video_chan.download(output_path='Canal')
        print("Completo!")
