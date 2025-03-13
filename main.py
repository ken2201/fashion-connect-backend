from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scraping import scrape_hm

app = FastAPI()

# Autoriser toutes les origines pour l'accès API (frontend et backend peuvent communiquer)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # À restreindre en production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/search")
def search(query: str):
    results = scrape_hm(query)
    return {"results": results}
