"""
Example of a test for an HTTP request
"""
import requests


URL = "http://www.google.com"

QUERY = "http://www.google.com/search?q=python"


def test_request():
    result = requests.get(URL)
    assert result.status_code == 200
    assert "Google" in result.text


def test_request():
    result = requests.get(URL + "/search", params={"q": "python"})
    assert result.status_code == 200
    assert "Google" in result.text
