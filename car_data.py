import requests
from bs4 import BeautifulSoup
import re
import random
from concurrent.futures import ThreadPoolExecutor

def fetch_car_image(car_link):
    try:
        page = requests.get(car_link)
        soup = BeautifulSoup(page.text, "html.parser")
        img_tag = soup.find("table", class_="infobox").find("img")
        return "https:" + img_tag['src'] if img_tag else None
    except:
        return None

def scrape_expensive_cars_with_images(limit=5):
    url = "https://en.wikipedia.org/wiki/List_of_most_expensive_cars_sold_at_auction"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    table = soup.find("table", {"class": "wikitable sortable"})

    entries = []
    seen_titles = set()

    for row in table.find_all("tr")[1:]:
        cols = row.find_all("td")
        if len(cols) < 8:
            continue

        date_sold = cols[0].get_text(strip=True)
        model_year = cols[1].get_text(strip=True)
        car_tag = cols[2].find("a")
        if not car_tag:
            continue

        car_name = car_tag.get_text(strip=True)
        if car_name in seen_titles:
            continue

        price_raw = cols[6].get_text(strip=True)
        match = re.search(r"\$([\d,]+)", price_raw)
        if not match:
            continue

        seen_titles.add(car_name)
        entries.append({
            "car": car_name,
            "date": date_sold,
            "model_year": model_year,
            "price": int(match.group(1).replace(",", "")),
            "link": "https://en.wikipedia.org" + car_tag['href']
        })

    selected = random.sample(entries, k=min(limit, len(entries)))

    with ThreadPoolExecutor() as executor:
        images = list(executor.map(lambda x: fetch_car_image(x["link"]), selected))

    for i in range(len(selected)):
        selected[i]["image_url"] = images[i]

    return [entry for entry in selected if entry["image_url"]]
