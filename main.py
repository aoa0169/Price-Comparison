from scrapers import scrape_prices
from utils import match_products, sort_by_price, display_results

def main():
    print("🛍️  Welcome to the E-commerce Price Comparison Tool!")
    user_input = input("Enter a product to search: ")
    
    print("\n🔎 Scraping prices, please wait...")
    raw_data = scrape_prices(user_input)
    
    matched = match_products(raw_data, user_input)
    sorted_results = sort_by_price(matched)
    
    display_results(sorted_results)

if __name__ == "__main__":
    main()
