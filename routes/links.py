from fastapi import APIRouter
from typing import List
import threading
from repo.links import LinkRepo
from models.links import  HTMLModel
from helpers.get_html_by_links import get_html_by_link
from helpers.convert_link import convert_link
from helpers.async_wrapper import async_wrapper

link_router = APIRouter()


async def parse_urls(html: List, link: str):
    link = convert_link(link)
    try:
        if document := await LinkRepo.get_html(link):
            html.append(document)
        else:
            html_text = get_html_by_link(link)
            if html_text:
                document = await LinkRepo.insert_html(link, html_text)
                html.append(document)
            else:
                html.append({"link": link, "html": "No content. Please, check if url is correct"})
    except:
        html.append({"link": link, "html": "Error was occurred"})


@link_router.post("/parse")
async def get_html(links: List[str]) -> List[HTMLModel]:
    if len(links) > 50:
        links = links[:50]

    html = []

    for link in links:
        thr = threading.Thread(target=async_wrapper, args=(parse_urls, html, link))
        thr.start()
        thr.join()
    return html
