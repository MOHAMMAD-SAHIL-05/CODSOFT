import difflib
import random
from datetime import datetime

data = {
    "hi": ["Hi there! I'm a friendly chatbot here to assist you 😊", "Hello! How can I brighten your day?"],
    "hello": ["Hello! How can I help you today? 😊", "Hi! What's on your mind?"],
    "what is your name": ["I'm just a chatbot, but you can call me ChatBot.", "I don't have a name, but you can name me if you want!"],
    "where are you from": ["I'm from the digital world, always ready to chat!", "I live in cyberspace 🌐, close to your heart!"],
    "how are you": ["I'm just a chatbot, but I'm here to assist you.", "I'm great! Thanks for asking 😊"],
    "do you have any hobbies or interests?": ["I love chatting with amazing people like you!", "Helping users is my favorite hobby!"],
    "what did you eat today?": ["I don't eat, but I can recommend some great recipes for you!", "I run on data and love helping people!"],
    "what's your favorite color?": ["I love all colors equally!", "I don't have a preference, but what's yours?"],
    "do you enjoy listening to music?": ["I can't listen to music, but I can chat about it!", "Music sounds fascinating, tell me about your favorite songs!"],
    "tell me a joke": ["Why don’t skeletons fight each other? They don’t have the guts! 😂", "Why did the scarecrow win an award? Because he was outstanding in his field! 🌾"],
    "tell me a fact": ["Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old! 🍯", "Fun fact: A group of flamingos is called a 'flamboyance'! 🦩"],
    "what time is it?": [datetime.now().strftime("The current time is %H:%M:%S ⏰.")],
    "bye": ["Goodbye! Have a wonderful day! 😊", "See you soon! Take care!"]
}

def get_response(user_input):
    user_input = user_input.lower()
    for pattern, responses in data.items():
        # Use fuzzy matching to find similar patterns
        if difflib.SequenceMatcher(None, pattern, user_input).ratio() > 0.6:
            return random.choice(responses)
    return "I'm sorry, I didn't understand that. Can you please rephrase? 🤔"

print("Chatbot: Hi! I'm a friendly chatbot, here to assist you! 😊")

while True:
    user_input = input("Me: ").strip()
    if user_input.lower() == 'bye':
        confirm = input("Chatbot: Are you sure you want to exit? (yes/no): ").strip().lower()
        if confirm == 'yes':
            print("Chatbot: Goodbye! Have a great day! 😊")
            break
        else:
            print("Chatbot: Great! Let's keep chatting. 😊")
            continue
    response = get_response(user_input)
    print("Chatbot:", response)
