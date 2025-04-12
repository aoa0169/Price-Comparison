from scrapers import scrape_prices

print("🛍️  Welcome to the E-commerce Price Comparison Tool!")
product = input("Enter a product to search: ")

print("\n🔎 Scraping prices, please wait...")
results = scrape_prices(product)

if results:
    print(f"\n✅ Found {len(results)} matching products:\n")
    for r in results[:5]:  # display only first 5 results
        print(f"🛒 {r['title']}\n💲 ${r['price']:.2f}\n🔗 {r['link']}\n")
else:
    print("❌ No products found.")
