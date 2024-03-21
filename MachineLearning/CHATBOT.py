# # import nltk
# # from nltk.chat.util import Chat, reflections
# # import requests
# # from bs4 import BeautifulSoup
# #
# # # Initialize NLTK chat
# # nltk.download('punkt')
# # nltk.download('averaged_perceptron_tagger')
# # nltk.download('wordnet')
# #
# #
# # # Define responses for stock-related queries
# # stock_responses = {
# #     'what is the current price of (.*)': [f'I am fetching the current price of {0}...', f'The current price of {0} is $XX.XX.'],  # Example pattern
# #     # Add more patterns and responses as needed
# # }
# #
# # # Define a function to search the web for stock-related queries not in the dataset
# # def search_web(query):
# #     search_url = f'https://www.example.com/search?q={query}'
# #     response = requests.get(search_url)
# #     if response.status_code == 200:
# #         soup = BeautifulSoup(response.content, 'html.parser')
# #         # Extract relevant information from the search results
# #         # Update this part based on the structure of the search results page
# #         # For example, you might look for specific HTML tags or classes containing the information you need
# #         # Then return the relevant information as a string
# #         return 'I found the information you were looking for on the web.'
# #     else:
# #         return 'Sorry, I couldn\'t find any information on the web.'
# #
# # # Define a function to respond to user queries
# # def respond(query):
# #     for pattern, responses in stock_responses.items():
# #         match = nltk.chat.util.find_match(pattern, query)
# #         if match:
# #             # For simplicity, just return the first response
# #             return responses[0].format(*match.groups())
# #     # If the query does not match any pattern, search the web
# #     return search_web(query)
# #
# # # Initialize the chatbot
# # stock_chatbot = Chat(stock_responses, reflections)
# #
# # # Main loop to interact with the chatbot
# # print("Welcome to the Stock Market Chatbot!")
# # while True:
# #     user_input = input("You: ")
# #     if user_input.lower() == 'exit':
# #         print("Stock Market Chatbot: Goodbye!")
# #         break
# #     else:
# #         print("Stock Market Chatbot:", respond(user_input))
#
# # import nltk
# # import random
# # from nltk.chat.util import Chat, reflections
#
# # # Define responses for stock-related queries
# # stock_responses = {
# #     'what is the current price of (.*)': [f'I am fetching the current price of {0}...', f'The current price of {0} is $XX.XX.'],  # Example pattern
# #     # Add more patterns and responses as needed
# # }
#
# # # Define responses for greetings
# # greeting_responses = ['Hello!', 'Hi there!', 'Greetings!', 'Hey! How can I help you today?']
#
# # # Combine all responses
# # responses = {**stock_responses}
#
# # # Initialize NLTK chat
# # nltk.download('punkt')
# # nltk.download('averaged_perceptron_tagger')
# # nltk.download('wordnet')
# # chatbot = Chat(responses, reflections)
#
# # # Function to handle user queries
# # def respond_to_user_query(query):
# #     response = chatbot.respond(query)
# #     if not response:
# #         return "I'm sorry, I couldn't understand your query. Can you please rephrase?"
# #     return response
#
# # # Main function
# # def main():
# #     print("Stock Market Chatbot: " + random.choice(greeting_responses))
# #     while True:
# #         user_input = input("You: ")
# #         if user_input.lower() == 'exit':
# #             print("Stock Market Chatbot: Goodbye!")
# #             break
# #         else:
# #             print("Stock Market Chatbot:", respond_to_user_query(user_input))
#
# # if __name__ == "__main__":
# #     main()
#
# import requests
# from bs4 import BeautifulSoup
#
# def search_on_internet(query):
#     search_url = f"https://www.duckduckgo.com/html/?q={query}"
#     response = requests.get(search_url)
#     if response.status_code >= 200:
#         soup = BeautifulSoup(response.content, 'html.parser')
#         search_results = soup.find_all('a', {'class': 'result__a'})
#         print("Search Results:")
#         for index, result in enumerate(search_results, start=1):
#             title = result.text.strip()
#             link = result['href']
#             print(f"{index}. {title}")
#             print(f"   {link}")
#             print()
#     else:
#         print("Error: Failed to fetch search results.")
#
# def main():
#     query = input("Enter your search query: ")
#     search_on_internet(query)
#
# if __name__ == "__main__":
#     main()
