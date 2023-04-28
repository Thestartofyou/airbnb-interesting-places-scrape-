import requests
from bs4 import BeautifulSoup

# Define the URL for the Airbnb search results page for New York City
url = "https://www.airbnb.com/s/New-York--NY--United-States/homes"

# Send an HTTP request to the URL and get the HTML response
response = requests.get(url)

# Parse the HTML response with BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the property listings on the page
listings = soup.find_all("div", class_="_8s3ctt")

# Loop through each listing and extract the name and price
for listing in listings:
    name = listing.find("div", class_="_bzh5lkq").get_text().strip()
    price = listing.find("span", class_="_krjbj").get_text().strip()
    print(name + " - " + price)

