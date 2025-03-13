from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Autoriser toutes les origines pour le frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Remplacer "*" par ton domaine en prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Route API vers AliExpress via RapidAPI


@app.get("/search")
def search_products(query: str):
    url = "https://aliexpress-datahub.p.rapidapi.com/item_search"
    headers = {
        "x-rapidapi-host": "aliexpress-datahub.p.rapidapi.com",
        "x-rapidapi-key": "a7d11ac285mshe549df68303cba5p1d2d93jsn92e2c47865c5",
    }
    params = {"q": query}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        # Adapter selon le format retourné par RapidAPI
        items = data.get("result", {}).get("items", [])
        results = [
            {
                "title": item.get("title"),
                "image": item.get("image"),
                "link": item.get("url"),
                "price": item.get("price"),
            }
            for item in items
        ]
        return results
    else:
        return {"error": "Failed to fetch products"}
