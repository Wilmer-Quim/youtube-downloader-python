
# prueva fallida por errores de importacion de moviepy
# en la linea 6 por .editor import *

from pytube import YouTube
from moviepy.editor import *
import os

def descargar_mp3(link):
    try:
        # Descarga el video
        yt = YouTube(link)
        print(f"Descargando: {yt.title}...")

        # Carpeta donde se guardará el audio
        carpeta_salida = "descargas_mp3"
        os.makedirs(carpeta_salida, exist_ok=True)

        # Descarga el archivo de video en la mejor calidad de audio disponible
        stream = yt.streams.filter(only_audio=True).first()
        archivo_video = stream.download(output_path=carpeta_salida)

        # Convierte el archivo a MP3
        archivo_mp3 = os.path.splitext(archivo_video)[0] + ".mp3"
        videoclip = AudioFileClip(archivo_video)
        videoclip.write_audiofile(archivo_mp3)
        videoclip.close()

        # Elimina el archivo original de video
        os.remove(archivo_video)

        print(f"✅ Descarga completada: {archivo_mp3}")

    except Exception as e:
        print(f"❌ Error: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    link = input("Ingresa el link de YouTube: ")
    descargar_mp3(link)
