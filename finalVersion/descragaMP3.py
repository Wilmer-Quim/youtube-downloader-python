# yt_dlp es una biblioteca de Python que permite descargar videos y audios de YouTube y otros sitios web.
# Se instala con: pip install yt-dlp
# Esta versión descarga el audio en su formato original (generalmente webm o m4a).

import yt_dlp
import os

def descargar_audio(url, carpeta='downloads'):
    try:
        # Crear la carpeta de descargas si no existe
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

        opciones = {
            'format': 'bestaudio/best',  # Mejor calidad de audio disponible
            'outtmpl': f'{carpeta}/%(title)s.%(ext)s',  # Nombre y extensión original
            'noplaylist': True  # Evitar descargar listas de reproducción
        }

        print(f"🎵 Iniciando descarga de: {url}")
        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([url])
        os.system('cls')
        print("✅ Descarga completada.")
        
    except Exception as e:
        os.system('cls')
        print(f"❌ Ocurrió un error durante la descarga: {e}")

if __name__ == "__main__":
    url = input("Ingrese la URL del video de YouTube: ").strip()
    if url:
        descargar_audio(url)
    else:
        print("No ingresaste un enlace válido.")

while True:
    repetir = input("¿Deseas descargar otro audio? (s/n): ").strip().lower()
    if repetir == 's':
        url = input("Ingrese la URL del video de YouTube: ").strip()
        if url:
            descargar_audio(url)
        else:
            print("No ingresaste un enlace válido.")
    elif repetir == 'n':
        print("¡Gracias por usar el descargador de MP3! ¡Hasta luego!")
        break
    else:
        print("Por favor, ingresa 's' para sí o 'n' para no.")

