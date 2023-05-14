from config.db_con import database
import uuid
from models.links import HTMLModel

collection = database.get_collection("links")


class LinkRepo:

    @staticmethod
    async def get_html(link):
        data = await collection.find_one({"link": link})
        return data if data else None

    @staticmethod
    async def insert_html(link, html):
        data = {"link": link, "html": html}
        await collection.insert_one(data)
        return data
