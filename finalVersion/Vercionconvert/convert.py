#me hacen falta librerias
#falta la libreria ffmpeg instalada en el sistema

import subprocess
import os

def convertir_webm_a_mp3(archivo_webm, archivo_mp3):
    if not os.path.exists(archivo_webm):
        print(f"Error: El archivo {archivo_webm} no existe.")
        return
    
    comando = [
        'ffmpeg',
        '-i', archivo_webm,  # Archivo de entrada
        '-vn',  # Sin video (solo audio)
        '-acodec', 'mp3',  # Codec de salida
        '-ab', '192k',  # Bitrate (opcional)
        archivo_mp3  # Archivo de salida
    ]
    
    try:
        subprocess.run(comando, check=True)
        print(f"Conversión completada: {archivo_webm} -> {archivo_mp3}")
    except subprocess.CalledProcessError as e:
        print(f"Error durante la conversión: {e}")

# Ejemplo de uso
convertir_webm_a_mp3("video.webm", "output.mp3")
