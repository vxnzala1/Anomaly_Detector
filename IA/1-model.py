import os
import shutil
import random
import yaml
from sklearn.model_selection import KFold
from ultralytics import YOLO
import numpy as np

def main():
    ROOT_PATH = r"D:\Documentos\Estudios\UNIVERSIDAD\Otros\TFG\Anomaly_Detector\IA\Export\YOLO\project-4-at-2024-08-05-09-17-df97b2c7"

    # Define paths
    image_dir = os.path.join(ROOT_PATH, 'images')
    label_dir = os.path.join(ROOT_PATH, 'labels')
    output_dir = os.path.join(ROOT_PATH, 'output')

    # Asegúrate de que el directorio de salida existe
    os.makedirs(output_dir, exist_ok=True)

    images = os.listdir(image_dir)
    labels = os.listdir(label_dir)

    # Emparejar imágenes y etiquetas
    dataset = list(zip(images, labels))
    random.shuffle(dataset)

    # Crear un objeto KFold
    kf = KFold(n_splits=5)

    def create_fold_dirs(base_dir, fold):
        os.makedirs(f"{base_dir}/fold_{fold}/train/images", exist_ok=True)
        os.makedirs(f"{base_dir}/fold_{fold}/train/labels", exist_ok=True)
        os.makedirs(f"{base_dir}/fold_{fold}/val/images", exist_ok=True)
        os.makedirs(f"{base_dir}/fold_{fold}/val/labels", exist_ok=True)

    def copy_files(files, base_dir, fold, split):
        for image, label in files:
            shutil.copy(os.path.join(image_dir, image), f"{base_dir}/fold_{fold}/{split}/images/{image}")
            shutil.copy(os.path.join(label_dir, label), f"{base_dir}/fold_{fold}/{split}/labels/{label}")

    def create_folds(create_folds_flag):
        if create_folds_flag:
            for fold, (train_idx, val_idx) in enumerate(kf.split(dataset)):
                train_files = [dataset[i] for i in train_idx]
                val_files = [dataset[i] for i in val_idx]
                
                create_fold_dirs(output_dir, fold)
                copy_files(train_files, output_dir, fold, "train")
                copy_files(val_files, output_dir, fold, "val")

    def create_data_yaml(train_path, val_path, output_dir, fold, class_names):
        data = {
            'train': os.path.join(train_path, 'images'),
            'val': os.path.join(val_path, 'images'),
            'nc': len(class_names),  # Número de clases
            'names': class_names  # Nombres de las clases
        }
        yaml_path = os.path.join(output_dir, f'data_fold_{fold}.yaml')
        with open(yaml_path, 'w') as outfile:
            yaml.dump(data, outfile, default_flow_style=False)
        return yaml_path

    def train_and_evaluate(fold, class_names):
        # Define paths for this fold
        train_path = f"{output_dir}/fold_{fold}/train"
        val_path = f"{output_dir}/fold_{fold}/val"
        
        # Create data.yaml file
        data_yaml_path = create_data_yaml(train_path, val_path, output_dir, fold, class_names)
        
        # Initialize YOLO model
        model = YOLO('yolov8n.yaml') # Cambiar esto si se necesita usar otro modelo
        
        # Train the model
        results = model.train(data=data_yaml_path, epochs=1000, imgsz=1024, batch=16)  #Modelo con casi 100% de precisión en YOLOv8n
        #results = model.train(data=data_yaml_path, epochs=100, imgsz=1280, batch=32, patience=10, augment=True)
        #results = model.train(data=data_yaml_path, epochs=500, imgsz=1024, batch=16)
        #results = model.train(data=data_yaml_path, epochs=1000, imgsz=1024, batch=16)
        #results = model.train(data=data_yaml_path, epochs=1000, imgsz=1024, batch=16)
        
        # Evaluate the model
        metrics = model.val(data=data_yaml_path)

        return metrics

    def calculate_average_metrics(all_metrics):
        # Asumiendo que all_metrics es una lista de diccionarios de métricas
        averaged_metrics = {}
        for key in all_metrics[0].keys():
            averaged_metrics[key] = np.mean([metrics[key] for metrics in all_metrics])
        return averaged_metrics

    # Control flag for creating folds
    create_folds_flag = False  # Cambia esto a True si necesitas crear los folds

    # Define your class names here
    class_names = ['Cut', 'Hole', 'Injure', 'Sawdust']  # Asegúrate de incluir todos los nombres de las clases

    create_folds(create_folds_flag)

    # Perform training and evaluation for each fold
    all_metrics = []
    for fold in range(1): #Modifcarlo para que haga 5 folds
        metrics = train_and_evaluate(fold, class_names)
        all_metrics.append(metrics)

    #average_metrics = calculate_average_metrics(all_metrics)
    #for key, value in average_metrics.items():
    #    print(f"{key}: {value}")

if __name__ == '__main__':
    import multiprocessing
    multiprocessing.freeze_support()
    main()