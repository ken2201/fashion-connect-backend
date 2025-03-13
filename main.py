from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Configuration CORS pour autoriser les requêtes de ton site
app.add_middleware(
    CORSMiddleware,
    # Remplace "*" par l'URL de ton frontend si besoin (ex: "https://fashion-connect.onrender.com")
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Clé API et Host pour AliExpress DataHub
API_KEY = "a7d11ac285mshe549df68303cba5p1d2d93jsn92e2c47865c5"
API_HOST = "aliexpress-datahub.p.rapidapi.com"
API_URL = "https://aliexpress-datahub.p.rapidapi.com/item_search"


# Route de recherche
@app.get("/search")
def search(query: str):
    headers = {
        "x-rapidapi-host": API_HOST,
        "x-rapidapi-key": API_KEY
    }
    params = {
        "query": query,
        "page": "1",
        "country": "FR"
    }

    try:
        response = requests.get(API_URL, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        # Retourner uniquement les éléments pertinents (produits)
        return data.get("result", {}).get("resultList", [])
    except requests.RequestException as e:
        return {"error": str(e)}
