# 🚀 Instrucciones de Uso

Este documento proporciona las instrucciones necesarias para configurar y comenzar a trabajar con tu entorno en Visual Studio Code utilizando Docker y Label Studio. Sigue los pasos detallados a continuación:

## 🐳 Configuración de Docker

1. **Abrir el entorno de trabajo en Visual Studio Code:**
  -> Abrir primeramente el Docker Desktop y posteriormente en terminal escribir: **docker-compose up**
  -> Abre la terminal y ejecuta el siguiente comando en la carpeta de trabajo para iniciar Label Studio con Docker:
  docker run -it -p 8080:8080 -v pwd/mydata:/label-studio/data heartexlabs/label-studio:latest

  Este comando inicia Label Studio en el puerto `8080` y monta tu carpeta actual (`pwd`) bajo `/mydata` en el contenedor, permitiendo la persistencia de los datos.

## 🔑 Iniciar Sesión en Label Studio

- **Credenciales:**
Una vez que Label Studio esté corriendo, puedes acceder mediante tu navegador e iniciar sesión utilizando las credenciales guardadas previamente.

## 📁 Configuración de `docker-compose.yml`

1. **Crear un archivo `docker-compose.yml`:**
En la carpeta de trabajo, crea un archivo `docker-compose.yml` con el siguiente contenido para definir y configurar el servicio de Label Studio:

```yaml
version: '3'
services:
  label-studio:
    image: heartexlabs/label-studio:latest
    ports:
      - "8080:8080"
    volumes:
      - ./mydata:/label-studio/data

## 🌐 Acceso a Plesk

**URL:** [https://go-capricornio.com:8443](https://go-capricornio.com:8443)

- **Usuario:** go-capricornio
- **Contraseña:** Zi%hp8E*1uojxY9q

## 📂 Acceso FTP

- **Usuario:** go-capricornio.com_ahorgfjr5
- **Contraseña:** Z46TiL$p4w

## 💾 Base de Datos

- **Base de Datos:** cerambyx_maria_db
- **Usuario:** cerambyx_user
- **Contraseña:** Uco.2024

##  Análisis manual de imágenes
- Se separa en 3 tipos de acontecimientos encontrados en el árbol, con nomeclatura en inglés, clasificándose en: serrín, agujeros y cortes