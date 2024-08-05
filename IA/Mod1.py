from ultralytics import YOLO

# Cargar el modelo YOLO preentrenado
model = YOLO('yolov5s.pt')  # Puedes cambiar a 'yolov5m.pt' o 'yolov5l.pt' para versiones más grandes

# Entrenar el modelo
model.train(data='/path/to/data.yaml', epochs=100)
