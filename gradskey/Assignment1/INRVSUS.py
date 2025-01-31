import requests
from bs4 import BeautifulSoup
import csv

def fetch_currency_data():
    url = "https://example.com/inr-usd-data"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = []
    for row in soup.find_all("tr")[1:]:
        cols = row.find_all("td")
        data.append([cols[0].text, cols[1].text])
    with open("currency_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Year", "Exchange Rate"])
        writer.writerows(data)
fetch_currency_data()