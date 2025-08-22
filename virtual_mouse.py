import cv2
import mediapipe as mp
import pyautogui
import numpy as np

# Initialize
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)

screen_w, screen_h = pyautogui.size()
cap = cv2.VideoCapture(0)

# Smoothing
prev_x, prev_y = 0, 0
smooth_factor = 0.2  # smaller = smoother but slower

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip for natural movement
    frame = cv2.flip(frame, 1)
    frame_h, frame_w, _ = frame.shape

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Index finger tip
            x = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * frame_w)
            y = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * frame_h)

            # Convert to screen coordinates
            screen_x = np.interp(x, [0, frame_w], [0, screen_w])
            screen_y = np.interp(y, [0, frame_h], [0, screen_h])

            # Smooth movement
            curr_x = prev_x + (screen_x - prev_x) * smooth_factor
            curr_y = prev_y + (screen_y - prev_y) * smooth_factor
            prev_x, prev_y = curr_x, curr_y

            pyautogui.moveTo(screen_w - curr_x, curr_y)  # FIX: mirror x-axis

            # Click detection (thumb + index distance)
            thumb = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            dist = np.linalg.norm(
                np.array([thumb.x, thumb.y]) - np.array([hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x,
                                                         hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y])
            )

            if dist < 0.04:  # Adjust threshold
                pyautogui.click()
                pyautogui.sleep(0.3)  # Avoid multiple clicks

            # Draw landmarks
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Virtual Mouse", frame)
    if cv2.waitKey(1) == 27:  # Esc to exit
        break

cap.release()
cv2.destroyAllWindows()
