def load_knowledge(file_path):
    """Loads knowledge from a document and returns a dictionary."""
    knowledge = {}
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                if "|" in line:
                    question, answer = line.strip().split(" | ", 1)
                    knowledge[question.lower()] = answer  # Store questions in lowercase for case-insensitive matching
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    return knowledge

def get_answer(question, knowledge):
    """Returns an answer based on the question or a default response."""
    return knowledge.get(question.lower(), "I'm not sure about that. Please ask something else.")

if __name__ == "__main__":
    knowledge_file = "knowledge.txt"  # Path to the knowledge document
    knowledge_base = load_knowledge(knowledge_file)

    if not knowledge_base:
        print("No knowledge loaded. Exiting...")
    else:
        print("\nChatbot: Hello! Ask me a question. Type 'exit' to quit.\n")
        
        while True:
            user_input = input("You: ").strip()
            if user_input.lower() in ["exit", "quit"]:
                print("Chatbot: Goodbye!")
                break
            response = get_answer(user_input, knowledge_base)
            print(f"Chatbot: {response}\n")
