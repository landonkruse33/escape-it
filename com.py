import requests
from bs4 import BeautifulSoup

class WikipediaSurfingModel:
    def __init__(self):
        self.base_url = "https://en.wikipedia.org/wiki/"

    def search(self, query):
        # Format the query to create the URL
        formatted_query = query.replace(" ", "_")
        url = self.base_url + formatted_query
        
        # Send a request to the Wikipedia page
        response = requests.get(url)
        
        if response.status_code == 200:
            return self.extract_summary(response.text)
        else:
            return "Sorry, I couldn't find any information on that topic."

    def extract_summary(self, html_content):
        # Parse the HTML content
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Find the first paragraph of the article
        paragraphs = soup.find_all('p')
        if paragraphs:
            return paragraphs[0].text
        else:
            return "No summary available."

# Example usage
if __name__ == "__main__":
    model = WikipediaSurfingModel()
    question = input("What topic would you like to know about? ")
    answer = model.search(question)
    print(answer)
