import youtube_dl 
#Libreria de Youtube

#Pide el url
input_url = input("Ingrese la URL del video que desea convertir: ")

video_info = youtube_dl.YoutubeDL().extract_info(url=input_url, download=False)
video_title = video_info['title'] #Toma el titulo de la canción

opciones = {
    'format': 'bestaudio/best',
    'outtmpl': f"C:/Users/Administrador/Desktop/musica-programa/%(title)s.%(ext)s",
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3', #Descarga en mp3
        'preferredquality': '192',
    }],
}

with youtube_dl.YoutubeDL(opciones) as ydl:
    ydl.download([input_url])