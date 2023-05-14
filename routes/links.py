from fastapi import APIRouter
from typing import List
import threading
import asyncio
from repo.links import LinkRepo
from models.links import  HTMLModel
from helpers.get_html_by_links import get_html_by_link
from helpers.convert_link import convert_link
from helpers.async_wrapper import async_wrapper

link_router = APIRouter()

async def insert_noncached(link: str, target: List) -> None:
    html = get_html_by_link(link)
    if html:
        document = await LinkRepo.insert_html(link, html)
        target.append(document)
    else:
        target.append({"link": link, "html": "No content. Please, check if url is correct"})


@link_router.post("/parse")
async def get_html(links: List[str]) -> List[HTMLModel]:
    if len(links) > 50:
        links = links[:51]

    html = []

    for link in links:
        link = convert_link(link)
        try:
            if document := await LinkRepo.get_html(link):
                html.append(document)
            else:
                thr = threading.Thread(target=async_wrapper, args=(insert_noncached, link, html))
                thr.start()
                thr.join()
                # await insert_noncached(link, html)
        except:
            html.append({"link": link, "html": "Error was occurred"})
    return html
