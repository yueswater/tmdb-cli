# TMDB CLI App

A simple command-line interface (CLI) tool for fetching and displaying movie information from [The Movie Database (TMDB)](https://www.themoviedb.org/). This application allows users to browse movies by category (e.g. now playing, popular, top rated, and upcoming) directly from the terminal.

This project is built with Python, uses the TMDB v4 API with Bearer Token authentication, and formats the output into clean tables using the `tabulate` package.



## Features

- Fetches data from the official [TMDB API](https://developer.themoviedb.org/)
- Supports 4 types of movie categories:
  - `playing`: Currently playing movies
  - `popular`: Most popular movies
  - `top`: Top-rated movies
  - `upcoming`: Upcoming movie releases
- Outputs data in a formatted table
- Handles network and API errors gracefully
- Uses `.env` file to store your API key securely
- Written with clean code structure using the `src/` layout
- Fully tested using `pytest` and `unittest.mock`



## Demo

```bash
poetry run tmdb-app --type popular
````

Returns a table like:

```
╒═══════════════════════════════╤══════════════╤══════════╤════════════════════════════════════════════════════════╕
│ Title                         │ Release Date │ Rating   │ Overview                                               │
├───────────────────────────────┼──────────────┼──────────┼────────────────────────────────────────────────────────┤
│ War of the Worlds             │ 2025-07-29   │ 4.323    │ Will Radford is a top analyst for Homeland Security... │
│ F1                            │ 2025-06-25   │ 7.815    │ Racing legend Sonny Hayes is coaxed out of retirem...  │
╘═══════════════════════════════╧══════════════╧══════════╧════════════════════════════════════════════════════════╛
```



## Installation

This project uses [Poetry](https://python-poetry.org/) for dependency and environment management.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/tmdb-cli-app.git
cd tmdb-cli-app
```

### 2. Install Dependencies

```bash
poetry install
```

### 3. Add Your TMDB API Key

Go to your [TMDB account settings](https://www.themoviedb.org/settings/api), and copy your **v4 access token (Bearer Token)**.

Create a `.env` file in the project root:

```
TMDB_API_KEY=your_bearer_token_here
```

Make sure the token starts with `ey...`, not a legacy v3 key.



## Usage

Run the CLI using:

```bash
poetry run tmdb-app --type [playing|popular|top|upcoming]
```

Examples:

```bash
poetry run tmdb-app --type playing
poetry run tmdb-app --type top
```



## Project Structure

```
tmdb-cli/
├── pyproject.toml
├── Makefile
├── .env
├── README.md
├── src/
│   └── tmdb_cli/
│       ├── api.py         # Handles API requests to TMDB
│       ├── app.py         # CLI entrypoint (main function)
│       └── display.py     # Output formatting using tabulate
├── tests/
│   ├── test_api.py        # Unit tests for API fetching
│   └── __init__.py
└── notebook/
    └── main.ipynb         # (Optional) Exploration notebook
```



## Development

### Run the CLI

```bash
poetry run tmdb-app --type popular
```

### Run Tests

```bash
poetry run pytest
```



## Dependencies

* `requests`: For making HTTP requests
* `tabulate`: For rendering terminal tables
* `python-dotenv`: For reading `.env` API key
* `pytest`: For unit testing (in dev group)



## Makefile (Optional)

You can define shortcuts in a `Makefile`:

```makefile
popular:
	poetry run tmdb-app --type popular

top:
	poetry run tmdb-app --type top

test:
	poetry run pytest
```



## License

This project is open-source and available under the [MIT License](LICENSE).



## Acknowledgments

* [TMDB API](https://developer.themoviedb.org/)
* [Roadmap.sh Projects](https://roadmap.sh/projects/tmdb-cli)

```