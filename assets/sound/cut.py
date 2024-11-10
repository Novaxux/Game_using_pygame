from pydub import AudioSegment

# Cargar el archivo de audio
audio = AudioSegment.from_file("./damage.mp3")

# Definir el inicio y el final del recorte en milisegundos
start_time = 500  # 10 segundos
end_time = 1000    # 30 segundos

# Recortar el audio
cropped_audio = audio[start_time:end_time]

# Guardar el audio recortado
cropped_audio.export("./health_down.mp3", format="mp3")
