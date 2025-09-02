import os
from typing import Dict

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3/"

HEADERS = {"accept": "application/json", "Authorization": f"Bearer {API_KEY}"}


def fetch_movies(
    category: str, language: str = "en-US", page: int = 1
) -> Dict[str, str]:
    url = f"{BASE_URL}/movie/{category}?language={language}&page={page}"
    response = requests.get(url=url, headers=HEADERS)
    response.raise_for_status()
    return response.json()
