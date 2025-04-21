import cv2
import time
from handgesture import load_model, initialize_hand_tracking, recognize_gesture
from chatbotollama import get_llama_response
from difflib import get_close_matches

# Load trained model
model = load_model()
hands, mp_hands, mp_drawing, mp_drawing_styles = initialize_hand_tracking()

# Initialize camera
cap = cv2.VideoCapture(0)

# Common words dictionary for auto-correction
common_words = ["what", "name", "you", "hello", "how", "are", "thank", "please", "yes", "no"]

def autocorrect(word):
    matches = get_close_matches(word, common_words, n=1, cutoff=0.7)
    return matches[0] if matches else word

predicted_word = ""
corrected_word = ""
last_time = time.time()
display_time = 2.0  # Delay in seconds between predictions

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    character, frame = recognize_gesture(frame, hands, model)

    if character:
        current_time = time.time()
        if current_time - last_time > display_time:
            predicted_word += character
            corrected_word = autocorrect(predicted_word)
            print(f"Predicted Word: {corrected_word}")
            last_time = current_time

    cv2.putText(frame, corrected_word, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 3, cv2.LINE_AA)
    cv2.imshow("ASL Sign Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Get AI chatbot response based on predicted word
if corrected_word:
    chatbot_response = get_llama_response(corrected_word)
    print(f"\nChatbot Response: {chatbot_response}")
   