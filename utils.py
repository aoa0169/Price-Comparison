def match_products(products, search_term):
    return [p for p in products if search_term.lower() in p['title'].lower()]

def sort_by_price(products):
    return sorted(products, key=lambda x: x['price'])

def display_results(products):
    if not products:
        print("❌ No products found.")
        return

    print("\n💸 Top Deals:")
    for product in products[:5]:  # Show top 5 results
        print(f"{product['title']} - ${product['price']}")
        print(f"🔗 Link: {product['link']}\n")
