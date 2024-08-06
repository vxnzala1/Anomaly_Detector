import os

# Obtener la ruta absoluta del directorio que contiene el script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Definir las rutas de las carpetas 'images' y 'labels'
images_dir = os.path.join(script_dir, '..', 'project-4-at-2024-08-05-09-17-df97b2c7', 'images')
labels_dir = os.path.join(script_dir, '..', 'project-4-at-2024-08-05-09-17-df97b2c7', 'labels')

images_dir = os.path.normpath(images_dir)
labels_dir = os.path.normpath(labels_dir)

# Verificar si las carpetas existen, si no, crearlas
if not os.path.exists(images_dir):
    os.makedirs(images_dir)
if not os.path.exists(labels_dir):
    os.makedirs(labels_dir)

# Iterar sobre los archivos en la carpeta de labels
for label_file in os.listdir(labels_dir):
    label_path = os.path.join(labels_dir, label_file)

    # Verifica si el archivo de etiqueta está vacío
    if os.path.getsize(label_path) == 0:
        # Extrae el identificador (nombre de archivo sin extensión)
        identifier = os.path.splitext(label_file)[0]

        # Genera la ruta correspondiente a la imagen
        image_path = os.path.join(images_dir, identifier + ".jpg")  # Cambia ".jpg" a la extensión correcta de tus imágenes

        # Elimina el archivo de etiqueta vacío
        os.remove(label_path)
        print(f"Etiqueta vacía eliminada: {label_path}")

        # Verifica si la imagen correspondiente existe y elimínala
        if os.path.exists(image_path):
            os.remove(image_path)
            print(f"Imagen correspondiente eliminada: {image_path}")

print("Proceso completado.")
