import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Variables para seguimiento de objetos
obj_pos = [300, 300]
obj_radius = 40
obj_selected = False

# Iniciar captura de video
cap = cv2.VideoCapture(0)

with mp_hands.Hands(
    min_detection_confidence=0.8,
    min_tracking_confidence=0.5) as hands:

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            continue
        
        frame = cv2.resize(frame, (1280, 720))
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        result = hands.process(rgb_frame)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                # Obtener posiciones de dedos
                h, w, _ = frame.shape
                index_finger_tip = hand_landmarks.landmark[8]
                thumb_tip = hand_landmarks.landmark[4]

                index_pos = (int(index_finger_tip.x * w), int(index_finger_tip.y * h))
                thumb_pos = (int(thumb_tip.x * w), int(thumb_tip.y * h))

                # Calcular distancia entre índice y pulgar
                distance = np.linalg.norm(np.array(index_pos) - np.array(thumb_pos))

                # Detectar gesto de agarre
                if distance < 40:
                    if not obj_selected:
                        # Verificar si la mano está sobre el objeto
                        if np.linalg.norm(np.array(index_pos) - np.array(obj_pos)) < obj_radius:
                            obj_selected = True

                else:
                    obj_selected = False

                # Mover objeto si está seleccionado
                if obj_selected:
                    obj_pos = index_pos

                # Dibujar mano
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Dibujar objeto
        cv2.circle(frame, tuple(obj_pos), obj_radius, (255, 0, 0), -1)

        cv2.imshow('Drag & Drop Virtual', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()