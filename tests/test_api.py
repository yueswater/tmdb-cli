from unittest.mock import patch

import pytest

from tmdb_cli.api import fetch_movies


@patch("tmdb_cli.api.requests.get")
def test_fetch_movies_success(mock_get):
    fake_response = {
        "page": 1,
        "results": [
            {"title": "Fake Movie", "release_date": "2025-09-01", "vote_average": 7.8}
        ],
    }

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = fake_response

    result = fetch_movies("now_playing")

    assert "results" in result
    assert result["results"][0]["title"] == "Fake Movie"


@patch("tmdb_cli.api.requests.get")
def test_fetch_movie_failure(mock_get):
    mock_get.return_value.status_code = 403
    mock_get.return_value.raise_for_status.side_effect = Exception("403 Forbidden")

    with pytest.raises(Exception):
        fetch_movies("now_playing")
