import requests


def get_html_by_link(link: str) -> str | None:
    try:
        return requests.get(link).text
    except requests.exceptions.ConnectionError:
        return None
