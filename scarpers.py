import requests
from bs4 import BeautifulSoup

def scrape_prices(product_name):
    headers = {"User-Agent": "Mozilla/5.0"}
    search_query = product_name.replace(" ", "+")
    url = f"https://www.ebay.com/sch/i.html?_nkw={search_query}"

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    results = []
    items = soup.select(".s-item")

    for item in items:
        title = item.select_one(".s-item__title")
        price = item.select_one(".s-item__price")
        link = item.select_one(".s-item__link")

        if title and price and link:
            results.append({
                "title": title.text,
                "price": extract_price(price.text),
                "link": link['href']
            })
    return results

def extract_price(price_str):
    price = ''.join(filter(lambda x: x.isdigit() or x == '.', price_str))
    return float(price) if price else 0.0
