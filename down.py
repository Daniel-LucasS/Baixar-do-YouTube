from aula01.down_from_yt import *

resposta = True
while resposta:
    titulo('DOWNLOAD FROM YT')
    print('''
[1] Baixar vídeos
[2] Baixar audio
[3] Baixar Playlists
[4] Baixar Canais
[5] Finalizar
''')
    resp = input('Qual programa deseja inicializar? [Para sair, digite "5"] -> ')
    if resp.isnumeric():
        resp = int(resp)
        if resp == 5:
            resposta = False
        elif resp == 1:
            baixar_video()
        elif resp == 2:
            baixar_audio()
        elif resp == 3:
            baixar_playlist()
        elif resp == 4:
            baixar_channel()
        else:
            print("Por favor, digite apenas valores validos.")
    else:
        print("Por favor, digite apenas valores validos!")
titulo('Obrigado por utilizar o programa!')
