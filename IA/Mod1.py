from ultralytics import YOLO

def main():
    # Cargar el modelo YOLO preentrenado
    model = YOLO('yolov8n.pt')  # Puedes cambiar a 'yolov5m.pt' o 'yolov5l.pt' para versiones más grandes

# Cargar el modelo YOLO preentrenado
# Entrenar el modelo
    model.train(data=r'D:\Documentos\Estudios\UNIVERSIDAD\Otros\TFG\Anomaly_Detector\IA\data.yaml', epochs=10) # Varía los epochs según la cantidad de datos y la potencia de tu GPU
    model.save('Train_1.pt')
if __name__ == '__main__':
    import multiprocessing
    multiprocessing.freeze_support()
    main()
#image_dir = 'D:\Documentos\Estudios\UNIVERSIDAD\Otros\TFG\Anomaly_Detector\IA\Export\YOLO\project-4-at-2024-08-05-09-17-df97b2c7\images'
#label_dir = 'D:\Documentos\Estudios\UNIVERSIDAD\Otros\TFG\Anomaly_Detector\IA\Export\YOLO\project-4-at-2024-08-05-09-17-df97b2c7\labels'