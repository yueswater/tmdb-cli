import argparse

from tmdb_cli.api import fetch_movies
from tmdb_cli.display import render_movie_table

type_map = {
    "playing": "now_playing",
    "popular": "popular",
    "top": "top_rated",
    "upcoming": "upcoming"
}

def main():
    parser = argparse.ArgumentParser(description="TMDB Movie CLI")

    # Search by type
    parser.add_argument(
        "--type",
        "-t",
        choices=["playing", "popular", "top", "upcoming"],
        required=True,
        help="Movie category (playing, popular, top, upcoming)",
    )

    args = parser.parse_args()
    category = type_map[args.type]
    data = fetch_movies(category=category)
    movies = data.get("results", [])

    print(render_movie_table(movies))