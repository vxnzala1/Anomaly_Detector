from ultralytics import YOLO

# Cargar el modelo YOLO preentrenado
model = YOLO('yolov8n.pt')  # Puedes cambiar a 'yolov5m.pt' o 'yolov5l.pt' para versiones más grandes

# Entrenar el modelo
model.train(data=r'D:\Documentos\Estudios\UNIVERSIDAD\Otros\TFG\Anomaly_Detector\IA\data.yaml', epochs=1)