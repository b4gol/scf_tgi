from pyrogram import Client, filters, types
from pyrogram.errors import FloodWait
import asyncio
import tgcrypto
from time import sleep
import json
from config import *
from scrapper import *
from helper_checker import checker

app = Client("me", api_hash=api_hash_v, api_id=api_id_v)

chat_id1 = ""
deal_link = ""


@app.on_message(filters.command("scrap", prefixes=".") & filters.me)
async def scrap_command(_, message: types.Message):
    global chat_id1
    chat_id = message.chat.id
    await app.send_message(chat_id, "started")
    chat_id1 = types.Chat = await app.get_chat("Kuna Code Bot")
    chat_id1 = chat_id1.id
    await app.send_message(chat_id1, "🔎 Orderbook")
    sleep(1.5)


# .first scrapper without scrolling by pages
@app.on_message(filters.bot)
async def on_first_order_book_message(_, message: types.Message):
    global deal_link
    with open("checker_db.json", "r", encoding="utf-8") as file:
        info = json.load(file)
    checker()
    # check_json()
    text = str(message.text)
    chat_id = message.chat.id
    if text.startswith("#"):
        scrap(text, info["min"], info["percents"], info["max"])

        await message.click("Refresh")
        sleep(1.5)
        await app.send_message(chat_id, "🔎 Orderbook")
        sleep(1.5)
    else:
        await app.send_message(chat_id, "🔎 Orderbook")
        await message.forward(789402487)


@app.on_edited_message(filters.bot)
async def edited(_, message: types.Message):
    with open("checker_db.json", "r", encoding="utf-8") as file:
        info = json.load(file)
    text = str(message.text)
    # print(text)
    scrap(text, info["min"], info["percents"], info["max"])
    await asyncio.sleep(1.5)
    await message.click("Refresh")
    await asyncio.sleep(1.5)
    chat_id = types.Chat = await app.get_chat("Kuna Code Bot")
    chat_id = chat_id.id
    await app.send_message(chat_id, "🔎 Orderbook")
    sleep(1.5)


@app.on_message(filters.command("payed", prefixes=".") & filters.me)
async def payed(_, message: types.Message):
    info = reader("head_db.json")[-1]
    info["payed"] = True
    add_in_json("head_db.json", [info])
    await message.reply("Ok")
    chat_id = types.Chat = await app.get_chat("Kuna Code Bot")
    chat_id = chat_id.id
    await app.send_message(chat_id, "🔎 Orderbook")
    sleep(1.5)


@app.on_message(filters.command("min", prefixes=".") & filters.me)
async def minimum(_, message: types.Message):
    min_ = int(message.text.split(".min ", maxsplit=1)[1])
    with open("checker_db.json", "r", encoding="utf-8") as file:
        info = json.load(file)
    info["min"] = min_
    with open("checker_db.json", "w", encoding="utf-8") as file:
        json.dump(info, file, indent=3)


@app.on_message(filters.command("max", prefixes=".") & filters.me)
async def maximum(_, message: types.Message):
    max_ = int(message.text.split(".max ", maxsplit=1)[1])
    with open("checker_db.json", "r", encoding="utf-8") as file:
        info = json.load(file)
    info["max"] = max_
    with open("checker_db.json", "w", encoding="utf-8") as file:
        json.dump(info, file, indent=3)


@app.on_message(filters.command("percents", prefixes=".") & filters.me)
async def percent(_, message: types.Message):
    percents = float(message.text.split(".percents ", maxsplit=1)[1])
    with open("checker_db.json", "r", encoding="utf-8") as file:
        info = json.load(file)
    info["percents"] = percents
    with open("checker_db.json", "w", encoding="utf-8") as file:
        json.dump(info, file, indent=3)


if __name__ == '__main__':
    app.run()
