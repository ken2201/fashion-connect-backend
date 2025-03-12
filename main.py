from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scraping import scrape_hm

app = FastAPI()

# Autorisation CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # À remplacer par ton domaine en prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Route publique pour la recherche


@app.get("/search")
def search(query: str):
    results = scrape_hm(query)
    return {"results": results}
