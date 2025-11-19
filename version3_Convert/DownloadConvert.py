import yt_dlp
import os

def descargar_mp3(url, carpeta='downloads'):
    try:
        # Crear la carpeta si no existe
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

        # Configuración de descarga
        opciones = {
            'format': 'bestaudio/best',
            'outtmpl': f'{carpeta}/%(title)s.%(ext)s',
            'postprocessors': [{  # Convierte el archivo a mp3 automáticamente
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'quiet': False,  # Muestra progreso
        }

        print(f"Iniciando descarga de: {url}")
        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([url])
        print("Descarga completada en formato MP3.")

    except Exception as e:
        print(f"Ocurrió un error durante la descarga: {e}")

if __name__ == "__main__":
    url = input("Ingrese la URL del video de YouTube: ")
    descargar_mp3(url)
