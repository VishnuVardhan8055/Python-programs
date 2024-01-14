import requests
from bs4 import BeautifulSoup
req = requests.get("https://www.amazon.com/")
soup = BeautifulSoup(req.content,"html.parser")
print(soup.get_text())
print(soup.prettify())



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
