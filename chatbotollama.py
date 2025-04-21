import nltk
import ollama

# Ensure necessary resources are downloaded
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")

def extract_keywords(text):
    """Extracts relevant keywords using NLTK (nouns, verbs, adjectives)."""
    words = nltk.word_tokenize(text)  
    tagged_words = nltk.pos_tag(words)  

    # Extract nouns, verbs, and adjectives for richer context
    keywords = [word for word, tag in tagged_words if tag in ("NN", "NNS", "NNP", "NNPS", "VB", "VBP", "VBZ", "JJ", "JJR", "JJS")]

    return keywords if keywords else ["Unknown"]

def get_llama_response(text):
    """Generates a chatbot response using extracted keywords."""
    keywords = extract_keywords(text)
    prompt = f"Provide a concise, informative answer about: {' '.join(keywords)}"

    try:
        response = ollama.chat(
            model="llama3",  # Ensure model name is correct
            messages=[{"role": "user", "content": prompt}]
        )
        return response["message"]["content"].strip()
    except Exception as e:
        return f"Error generating response: {e}"
