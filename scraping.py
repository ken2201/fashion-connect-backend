import requests
from bs4 import BeautifulSoup


def scrape_hm(query):
    url = f"https://www2.hm.com/fr_fr/search-results.html?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.content, "html.parser")
    products = []

    for item in soup.select('.product-item'):
        try:
            title = item.select_one('.item-heading').get_text(strip=True)
            link = "https://www2.hm.com" + item.select_one('a')['href']
            image = item.select_one('img')['data-src']
            price = item.select_one('.price').get_text(strip=True)

            products.append({
                "title": title,
                "link": link,
                "image": image,
                "price": price
            })
        except Exception as e:
            print(f"Erreur produit : {e}")
            continue

    return products
