#prueva fallida por errores de importacion de moviepy
# en la linea 6 por .editor import *

from pytube import YouTube
from moviepy.editor import *
import os

def descargar_mp3(link):
    try:
        yt = YouTube(link)
        print(f"🎥 Descargando: {yt.title}")

        carpeta_salida = "descargas_mp3"
        os.makedirs(carpeta_salida, exist_ok=True)

        # Descargar solo el audio del video
        stream = yt.streams.filter(only_audio=True).first()
        archivo_video = stream.download(output_path=carpeta_salida)

        # Convertir el archivo descargado a mp3
        archivo_mp3 = os.path.splitext(archivo_video)[0] + ".mp3"
        clip = AudioFileClip(archivo_video)
        clip.write_audiofile(archivo_mp3)
        clip.close()

        # Eliminar el archivo original (mp4)
        os.remove(archivo_video)

        print(f"✅ Descarga completada: {archivo_mp3}")

    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    link = input("Ingresa el link de YouTube: ").strip()
    descargar_mp3(link)
