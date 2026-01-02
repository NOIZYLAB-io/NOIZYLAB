"""
Gesture Volume Control Prototype
Uses MediaPipe for hand/finger tracking via webcam.
Maps hand position to volume level (0-100).
"""
import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

print("[ERNEST] Starting gesture volume control. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)
    h, w, _ = frame.shape
    volume = None
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            # Use index finger tip (landmark 8) for volume control
            x = int(hand_landmarks.landmark[8].x * w)
            y = int(hand_landmarks.landmark[8].y * h)
            # Map y position to volume (top=100, bottom=0)
            volume = int(np.interp(y, [0, h], [100, 0]))
            cv2.putText(frame, f'Volume: {volume}', (x, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    cv2.imshow('Gesture Volume Control', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("[ERNEST] Gesture volume control ended.")
