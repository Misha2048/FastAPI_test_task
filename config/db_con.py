import motor.motor_asyncio
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

user = os.environ.get("DB_USER")
password = os.environ.get("DB_PASSWORD")
host = os.environ.get("DB_HOST")

CON_STR = f"mongodb+srv://{user}:{password}@{host}/?retryWrites=true&w=majority"

client = motor.motor_asyncio.AsyncIOMotorClient(CON_STR)
client.get_io_loop = asyncio.get_event_loop

database = client.chatmasters
