import spacy

# Load English tokenizer, POS tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")

# Define intents and responses
intents = {
    "greeting": ["hello", "hi", "hey"],
    "goodbye": ["bye", "goodbye", "see you"],
    "name": ["what is your name", "who are you"],
    "feeling": ["how are you", "how do you feel"],
    "capabilities": ["what can you do", "what are your functions"]
}

responses = {
    "greeting": "Hello! How can I help you?",
    "goodbye": "Goodbye! Have a nice day.",
    "name": "I’m a chatbot built using spaCy NLP!",
    "feeling": "I’m just code, but I’m doing great!",
    "capabilities": "I can answer simple questions using natural language processing."
}

# Function to predict intent
def predict_intent(user_input):
    user_input = user_input.lower()
    for intent, patterns in intents.items():
        for pattern in patterns:
            if pattern in user_input:
                return intent
    return "unknown"

# Start chatbot
print("Chatbot: Hi! I’m your spaCy chatbot. Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Chatbot:", responses["goodbye"])
        break

    intent = predict_intent(user_input)
    if intent in responses:
        print("Chatbot:", responses[intent])
    else:
        print("Chatbot: Sorry, I didn't understand that.")