import requests
from bs4 import BeautifulSoup
query = input()
req = requests.get(f"https://www.{query}.com/")
soup = BeautifulSoup(req.content,"html.parser")
print(soup.get_text())
print(soup.prettify())
#


# from googlesearch import search
#
# def search_on_google(query):
#     print("Searching on Google...")
#     try:
#         # Perform Google search and fetch top 5 results
#         search_results = search(query,)# num=500, stop=5, pause=2)
#         print("Search Results:")
#         for index, result in enumerate(search_results, start=1):
#             print(f"{index}. {result}")
#     except Exception as e:
#         print("Error:", e)
#
# def main():
#     query = input("Enter your search query: ")
#     search_on_google(query)
#
# if __name__ == "__main__":
#     main()


# def scrape_website(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, "html.parser")
#     return soup
#
# def get_data(soup):
#     data = []
#     for article in soup.find_all("article"):
#         title = article.find("h2").text
#         content = article.find("p").text
#         data.append({"title": title, "content": content})
#     return data
#
# if __name__ == "__main__":
#     url = "https://www.geeksfogeeks.com"
#     soup = scrape_website(url)
#     data = get_data(soup)
#     print(data)
