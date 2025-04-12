from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def scrape_prices(product_name):
    options = Options()
    options.add_argument("--headless")  # run in background
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # Setup ChromeDriver (requires chromedriver in PATH or use webdriver-manager)
    driver = webdriver.Chrome(options=options)
    
    search_query = product_name.replace(" ", "+")
    url = f"https://www.ebay.com/sch/i.html?_nkw={search_query}"
    driver.get(url)

    time.sleep(3)  # wait for JS to load

    results = []
    items = driver.find_elements(By.CSS_SELECTOR, ".s-item")

    print(f"Found {len(items)} product blocks")

    for item in items:
        try:
            title = item.find_element(By.CSS_SELECTOR, ".s-item__title").text
            price = item.find_element(By.CSS_SELECTOR, ".s-item__price").text
            link = item.find_element(By.CSS_SELECTOR, ".s-item__link").get_attribute("href")

            if title and price and link:
                results.append({
                    "title": title,
                    "price": extract_price(price),
                    "link": link
                })
        except Exception as e:
            continue

    driver.quit()
    return results

def extract_price(price_str):
    price = ''.join(filter(lambda x: x.isdigit() or x == '.', price_str))
    return float(price) if price else 0.0

