# VisorPython

# Drag & Drop Virtual con Detección de Manos

Este proyecto permite simular una funcionalidad de "arrastrar y soltar" (drag & drop) utilizando una cámara web y gestos con las manos. Utiliza la biblioteca **MediaPipe** para detectar las manos en tiempo real y mover un objeto virtual (círculo azul) en la pantalla al juntar el pulgar y el dedo índice.

## ¿Para qué sirve?

Este script es útil como demostración de interacción hombre-máquina sin contacto físico, ideal para proyectos de interfaces naturales (NUI), domótica, prototipos interactivos o sistemas de control basados en visión por computadora.

## ¿Cómo funciona?

1. Se inicia la cámara web y se captura el video en tiempo real.
2. Utiliza **MediaPipe Hands** para detectar los puntos clave de la mano.
3. Cuando el usuario junta el pulgar y el dedo índice cerca del objeto, se considera un "agarre".
4. Al mover la mano mientras se mantiene el gesto de agarre, el objeto se mueve junto con los dedos.
5. Cuando los dedos se separan, se "suelta" el objeto.
6. Se puede cerrar el programa presionando la tecla `q`.

## Requisitos

- Python 3.7 o superior
- Cámara web activa

## Librerías necesarias

Asegúrate de instalar las siguientes librerías antes de ejecutar el programa:

```bash
pip install opencv-python mediapipe numpy
