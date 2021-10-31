import pytube

from aula01.down_from_yt import *
import PySimpleGUI as sg

tema = 'BrownBlue'

# Janela Inicial
def janela_um():
    sg.theme(tema)
    layout = [
        [sg.Text('Baixar videos do YouTube')],
        [sg.Text('Por favor, escolha uma opção: ')],
        [sg.Button('Vídeo'), sg.Button('Áudio'), sg.Button('Playlist')],
        [sg.Text('*VIDEO = baixa um video do YouTube, á partir de uma URL.')],
        [sg.Text('*AUDIO = baixa apenas o audio de um video, no formato .mp4')],
        [sg.Text('*PLAYLIST = baixa toda uma playlista. Obs. Digite o URL da playlist adequadamente.')],
        [sg.Button('Cancel')]
            ]
    return sg.Window('Baixar do YouTube', layout=layout, finalize=True)


# Janela para baixar videos:
def janela_videos():
    sg.theme(tema)
    layout = [
        [sg.Text('Insira a url do video: ')],
        [sg.Input(size=(40,1), key='video')],
        [sg.Text(size=(40, 1), key='output') ],
        [sg.Button('Baixar')],
        [sg.Button('Voltar')]
            ]
    return sg.Window('Baixar videos', layout=layout, finalize=True)


# Janela para baixar audio
def janela_audio():
    sg.theme(tema)
    layout = [
        [sg.Text('Insira a url do video: ')],
        [sg.Input(size=(40,1), key='audio')],
        [sg.Button('Baixar')],
        [sg.Button('Voltar')]
    ]
    return sg.Window('Baixar áudio', layout=layout, finalize=True)


# Janela para baixar Playlists
def janela_playlist():
    sg.theme(tema)
    layout = [
        [sg.Text('Insira a URL da Playlist: ')],
        [sg.Input(size=(40,1), key='playlist')],
        [sg.Button('Baixar')],
        [sg.Button('Voltar')]
            ]
    return sg.Window('Baixar Playlist', layout=layout, finalize=True)


# Cria Janelas iniciais
janela1, janela2, janela3, janela4 = janela_um(), None, None, None

# Loop de leitura
while True:
    window, event, values = sg.read_all_windows()
    # Para fechar o programa
    if window == janela1 and event == 'Cancel' or window == janela1 and event == sg.WINDOW_CLOSED:
        break
    if window == janela1 and event == 'Vídeo':
        janela2 = janela_videos()
        janela1.hide()
    elif window == janela1 and event == 'Áudio':
        janela3 = janela_audio()
        janela1.hide()
    elif window == janela1 and event == 'Playlist':
        janela4 = janela_playlist()
        janela1.hide()
    if window == janela2 and event == 'Voltar':
        janela1.un_hide()
    elif window == janela2 and event == 'Baixar':
        yt = pytube.YouTube(values['video'], on_progress_callback=on_progress).streams.get_highest_resolution()
        sg.popup('Baixando = ', yt.title)
        yt.download()
        sg.popup('Download concluido!')
    if window == janela3 and event == 'Voltar':
        janela1.un_hide()
    elif window == janela3 and event =='Baixar':
        YouTube(values['audio'], on_progress_callback=on_progress).streams.get_audio_only().download()
        sg.popup('Download Concluido.')
    if window == janela4 and event == 'Voltar':
        janela1.un_hide()
    elif window == janela4 and event == 'Baixar':
        play = Playlist(values['playlist'])
        for url in play:
            video = YouTube(url)

            video.streams.get_highest_resolution().download(output_path='playlist1')
            sg.popup(video.title, 'Download Concluido!')

window.close()
