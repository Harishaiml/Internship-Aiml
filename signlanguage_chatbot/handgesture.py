import pickle
import cv2
import mediapipe as mp
import numpy as np

# Load trained model
def load_model():
    model_dict = pickle.load(open('"D:/internship/27-03-2025/MyProjects/MyProjects/model.p"', 'rb'))
    return model_dict['model']

# Initialize hand tracking
def initialize_hand_tracking():
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.3)
    return hands, mp_hands, mp_drawing, mp_drawing_styles

# ASL Labels Dictionary
labels_dict = {0: 'A', 1: 'B', 2: 'C',3: 'D',4: 'E',5: 'F',6: 'G',7: 'H',8: 'I',9: 'J',10:'K',11:'L',12: "M",
               13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'T',21:'U',22:'V',23:'W',24:'X',25:'Y',26:'Z'}

# Extract hand landmarks and recognize gestures
def recognize_gesture(frame, hands, model):
    H, W, _ = frame.shape
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if not results.multi_hand_landmarks:
        return None, frame  # No hand detected

    x_, y_, data_aux = [], [], []
    for hand_landmarks in results.multi_hand_landmarks:
        for landmark in hand_landmarks.landmark:
            x_.append(landmark.x)
            y_.append(landmark.y)

        for landmark in hand_landmarks.landmark:
            data_aux.append(landmark.x - min(x_))
            data_aux.append(landmark.y - min(y_))

 
    if len(data_aux) < 84:  
       data_aux.extend([0] * (84 - len(data_aux)) ) # Ensure correct shape

    data_aux = np.asarray(data_aux).reshape(1, -1)


    # Predict the character
    try:
        prediction = model.predict(data_aux)
        predicted_character = labels_dict[int(prediction[0])]
        return predicted_character, frame
    except Exception as e:
        print(f"Prediction error: {e}")
        return None, frame
