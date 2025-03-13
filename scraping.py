from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


def scrape_hm(query: str):
    # Configuration du navigateur headless
    options = Options()
    options.add_argument("--headless")  # Mode sans interface graphique
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Remplace le chemin ci-dessous par celui de ton chromedriver si nécessaire
    driver = webdriver.Chrome(options=options)

    # URL de recherche H&M
    url = f"https://www2.hm.com/fr_fr/search-results.html?q={query}"
    driver.get(url)
    time.sleep(3)  # Laisse le temps à la page de charger

    results = []
    # Classe des produits sur la page
    products = driver.find_elements(By.CLASS_NAME, "product-item")

    for product in products[:10]:  # Limite aux 10 premiers résultats
        try:
            title = product.find_element(By.CLASS_NAME, "item-heading").text
            link = product.find_element(By.TAG_NAME, "a").get_attribute("href")
            image = product.find_element(
                By.TAG_NAME, "img").get_attribute("src")

            results.append({
                "title": title,
                "link": link,
                "image": image
            })
        except:
            continue  # Ignore les erreurs individuelles sur un produit

    driver.quit()  # Ferme le navigateur automatisé
    return results
