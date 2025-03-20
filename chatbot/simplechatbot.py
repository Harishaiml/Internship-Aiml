#main.py


from chatbot_module import SimpleChatbot

if __name__ == "__main__":
    chatbot = SimpleChatbot()
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = chatbot.get_response(user_input)
        print(f"Chatbot: {response}")



#chatbot_module.py


class SimpleChatbot:
    def __init__(self):
        self.responses = {
           "What is AI?": "AI, or Artificial Intelligence, is the simulation of human intelligence in machines to perform tasks that typically require human intelligence, such as learning, reasoning, and problem-solving.",
            "What are the types of AI?": "AI is categorized into three types: Narrow AI (Weak AI), General AI (Strong AI), and Super AI. Narrow AI is designed for specific tasks, General AI has human-like intelligence, and Super AI surpasses human intelligence.",
            "What is the difference between AI and Machine Learning?": "AI is a broader concept that involves creating intelligent machines, whereas Machine Learning is a subset of AI that enables machines to learn patterns from data without explicit programming.",
            "What are the applications of AI?": "AI is used in various fields, including healthcare (diagnosis), finance (fraud detection), autonomous vehicles, chatbots, recommendation systems, and robotics.",
            "What is Natural Language Processing (NLP)?": "NLP is a field of AI that enables computers to understand, interpret, and generate human language. Examples include speech recognition and chatbots.",
            "What is Machine Learning?": "Machine Learning (ML) is a subset of AI that allows machines to learn from data and improve performance over time without being explicitly programmed.",
            "What are the types of Machine Learning?": "The three main types of Machine Learning are Supervised Learning, Unsupervised Learning, and Reinforcement Learning.",
            "What is supervised learning?": "Supervised Learning is a type of ML where the model is trained on labeled data, meaning it learns from input-output pairs. Examples include email spam detection and image classification.",
            "What is unsupervised learning?": "Unsupervised Learning is a type of ML where the model learns patterns from unlabeled data. Examples include clustering and anomaly detection.",
            "What is deep learning?": "Deep Learning is a subset of ML that uses neural networks with multiple layers to learn complex patterns in large datasets. It is widely used in image recognition and speech processing.",
            "What is Python?": "Python is a high-level programming language known for its simplicity and versatility. It is widely used in AI, web development, automation, and data science.",
            "Why is Python popular for AI?": "Python is popular for AI because it has a simple syntax, extensive libraries (like TensorFlow, PyTorch, and Scikit-Learn), and strong community support.",
            "What are Python libraries used for AI?": "Some popular Python libraries for AI include TensorFlow, PyTorch, Scikit-Learn, Keras, Numpy, and Pandas.",
            "What is TensorFlow?": "TensorFlow is an open-source library developed by Google for building and training machine learning models, particularly deep learning models.",
            "What is PyTorch?": "PyTorch is an open-source deep learning framework developed by Facebook, known for its flexibility and ease of use in research and production.",
            "Who invented AI?": "The concept of AI was first introduced by Alan Turing, but John McCarthy coined the term 'Artificial Intelligence' in 1956.",
            "What is the Turing Test?": "The Turing Test, proposed by Alan Turing, is a method to determine whether a machine can exhibit human-like intelligence by engaging in a conversation with a human judge.",
            "What is an Artificial Neural Network (ANN)?": "An ANN is a computing system inspired by the human brain, consisting of layers of interconnected nodes (neurons) used for deep learning tasks.",
            "What is reinforcement learning?": "Reinforcement Learning is a type of ML where an agent learns by interacting with an environment and receiving rewards or penalties for actions.",
            "What is an AI model?": "An AI model is a mathematical representation of a system that processes input data and produces predictions or decisions based on learned patterns."        
        }

    def get_response(self, question):
        return self.responses.get(question, "Sorry, I don't understand that question.")
