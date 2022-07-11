import youtube_dl

input_url = input("Ingrese la URL del video que desea convertir: ")

video_info = youtube_dl.YoutubeDL().extract_info(url=input_url, download=False)
video_title = video_info['title']

opciones = {
    'format': 'bestaudio/best',
    'outtmpl': f"C:/Users/Administrador/Desktop/musica-programa/%(title)s.%(ext)s",
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with youtube_dl.YoutubeDL(opciones) as ydl:
    ydl.download([input_url])