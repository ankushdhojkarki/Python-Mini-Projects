import requests
query = input("What type of news are you interested to read today?\n")
api = "202502e5775a49c4bdd7468ff8c37eed"
url = f"https://newsapi.org/v2/everything?q={query}&from=2025-04-01&sortBy=publishedAt&apiKey={api}" 

print(url)

r = requests.get(url)
data = r.json()
articles = data["articles"]

for index, article in enumerate(articles):
    print (index + 1, article["title"], "\n", article["url"])
    print("\n******************************************************************************************************\n")
