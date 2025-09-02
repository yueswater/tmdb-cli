from tabulate import tabulate
from typing import List, Dict

def render_movie_table(movies: List[Dict]) -> str:
    table_data = []

    for movie in movies:
        table_data.append([
            movie["title"],
            movie["release_date"],
            movie["vote_average"],
            movie["overview"][:60] + "..." if len(movie["overview"]) > 60 else movie["overview"]
        ])
        
    headers = ["Title", "Release Date", "Rating", "Overview"]
    return tabulate(
        tabular_data=table_data,
        headers=headers,
        tablefmt="fancy_grid"
    )