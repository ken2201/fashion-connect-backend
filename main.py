from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# --------------------- CORS ---------------------- #
app.add_middleware(
    CORSMiddleware,
    # Remplacer "*" par l'URL de ton frontend en production
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------- CONFIGURATION RAPIDAPI ---------------------- #
RAPIDAPI_KEY = "a7d11ac285mshe549df68303cba5p1d2d93jsn92e2c47865c5"
RAPIDAPI_HOST = "aliexpress-datahub.p.rapidapi.com"

# --------------------- ROUTE SEARCH ---------------------- #


@app.get("/search")
def search_products(query: str):
    url = "https://aliexpress-datahub.p.rapidapi.com/item_search"
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": RAPIDAPI_HOST
    }
    params = {
        "q": query,
        "page": "1",  # Tu peux ajouter "sort": "SALE_PRICE_ASC" pour trier par prix
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code, detail="API Error")

    api_data = response.json()

    # --------------------- Adaptation des données ---------------------- #
    results = []
    for item in api_data.get("result", {}).get("resultList", []):
        results.append({
            "title": item.get("productTitle"),
            "price": item.get("salePrice"),
            "image": item.get("productMainImageUrl"),
            "link": item.get("productDetailUrl"),
        })

    return results
