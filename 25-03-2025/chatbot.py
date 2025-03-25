import ollama

class Chatbot:
    def __init__(self):
        self.conversation_history = [
            {"role": "system", "content": "You are an AI assistant that answers questions based on context."}
        ]

    def get_response(self, user_input):
        """Generate a response while maintaining context."""
        self.conversation_history.append({"role": "user", "content": user_input})

        response = ollama.chat(
            model="llama3.2:latest",  # Use exact model name
            messages=self.conversation_history
        )

        bot_reply = response['message']['content']
        self.conversation_history.append({"role": "assistant", "content": bot_reply})
        return bot_reply

def main():
    chatbot = Chatbot()
    print("Chatbot is ready! Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        
        response = chatbot.get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
