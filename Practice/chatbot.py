import nltk
from nltk.tokenize import word_tokenize
import re
import random

responses = [
    "Hello! How are you doing today?",
    "That's great to hear!",
    "Oh, I'm sorry to hear that.",
    "I see. Can I help you with anything else?",
    "Thank you for chatting with me. Goodbye!"
]

def generate_response(user_input):
    tokens = word_tokenize(user_input)
    # Simple pattern matching to handle greetings
    if re.search("hello", user_input) or re.search("hi", user_input):
        return "Hello there! How can I help you today?"
    elif re.search("how are you", user_input):
        return random.choice(responses)
    elif re.search("exit|quit", user_input):
        return "Thank you for chatting with me. Goodbye!"
    else:
        # Default response if no pattern matches
        return "Sorry, I didn't quite understand that. Can you rephrase your question?"

def main():
    print("Welcome to the Chat Bot!")
    while True:
        user_input = input("You: ")
        response = generate_response(user_input)
        print("Chat Bot: ", response)
        if response == "Thank you for chatting with me. Goodbye!":
            break

if __name__ == "__main__":
    main()