# Define a dictionary of responses
responses = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! How are you?",
    "how are you": "I'm just a program, so I don't have feelings, but thanks for asking!",
    "bye": "Goodbye! Have a great day!",
    "default": "I'm not sure how to respond to that. Can you please ask something else?"
}

# Function to get a response based on the user's input
def get_response(user_input):
    user_input = user_input.lower()
    return responses.get(user_input, responses["default"])

# Chatbot loop
print("Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye!")
        break
    response = get_response(user_input)
    print(f"Chatbot: {response}")

import nltk
from nltk.chat.util import Chat, reflections

# Pairs is a list of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"hi|hello",
        ["Hello", "Hi there",]
    ],
    [
        r"what is your name ?",
        ["I am a bot created by you. You can call me Chatbot.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about You?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "No problem",]
    ],
    [
        r"bye|quit",
        ["Bye! Take care.",]
    ],
]

# Create a chatbot using the Chat class from nltk
chatbot = Chat(pairs, reflections)

# Start the conversation
print("Hi, I'm your chatbot. Type something to start a conversation. Type 'bye' to exit.")
chatbot.converse()
