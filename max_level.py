import json

# Guardar el nivel en un archivo JSON
def save_level(level):
    with open("save_file.json", "w") as file:
        json.dump({"level": level}, file)

# Cargar el nivel del archivo JSON
def load_level():
    try:
        with open("save_file.json", "r") as file:
            data = json.load(file)
            return data.get("level", 1)
    except FileNotFoundError:
        return 1  # Retorna 0 si no existe el archivo
