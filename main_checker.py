import time

import aioschedule as schedule
from pyrogram import Client, filters, types
from pyrogram.errors import FloodWait
import asyncio
import tgcrypto
from config import *
from helper_checker import *
from scrapper import reader

deal_link = ""

app = Client("my_friend", api_id=api_id_b, api_hash=api_hash_b)
counter = True


# def checked():
#     if checker():
#         return True
#     else:
#         return False

# TODO


def send_update():
    global deal_link, counter
    app.start()
    print(2)
    while counter:
        print(3)
        if not checker():
            chat_id = types.Chat = app.get_chat("Kuna Code Bot")
            deal = reader("last_results.json")[-1]["link"]
            deal_link = deal
            app.send_message(chat_id.id, deal)
            counter = False
            print(1)
            app.stop()


send_update()


#
@app.on_message(filters.bot)
async def get_info_about_deal(_, message: types.Message):
    global deal_link, counter
    if "you are going to accept order " in str(message.text):
        chat_id = types.Chat = await app.get_chat("Kuna Code Bot")
        chat_id = chat_id.id
        await app.send_message(chat_id, "📥 Pay")
    elif message.text.startswith("We`re in a deal creation."):
        pass
    elif len(message.text) == 16:
        info = reader("last_results.json")
        info1 = reader("result.json")
        if info[-1]["link"] == deal_link:

            info[-1]["card"] = message.text
            info[-1]["payed"] = False
            add_in_json("head_db.json", [info[-1]])
            msg = f"""Order: {info[-1]["#"]}\n
                      Prise: {info[-1]["min"]} | {info[-1]["max"]}\n
                      Percents: {info[-1]["percent"]}%\n
                      User: {info[-1]["user"]}\n
                      Bank: {info[-1]["bank"]}\n
                      Link: {info[-1]["link"]}\n
                      Card: <code>{info[-1]["card"]}<code>\n
                      Amount to pay: {info[-1]["max"]}"""
            await app.send_message(789402487, msg)
        else:
            for i in info1:
                if i["link"] == deal_link:
                    i["card"] = message.text
                    i["payed"] = False
                    add_in_json("head_db.json", [i])
                    msg = f"""Order: {i["#"]}\n
                              Prise: {i["min"]} | {info[-1]["max"]}\n
                              Percents: {i["percent"]}%\n
                              User: {i["user"]}\n
                              Bank: {i["bank"]}\n
                              Link: {i["link"]}\n
                              Card: <code>{i["card"]}</code>\n
                              Amount to pay: {i["max"]}"""
                    await app.send_message(789402487, msg)
        counter = 0
        while counter != 90:
            if check_json():
                print("payed")
                await message.click("🤝 I have paid")
                break
            else:
                counter += 1
                time.sleep(10)
                print("whait")
    elif "The seller did not respond to your deal" in str(message.text):
        counter = True
        send_update()
    else:
        await message.forward(789402487)
        counter = True
        send_update()


if __name__ == '__main__':
    app.run()
    # schedule.every().second.do(send_update, app)
    # while True:
    #     schedule.run_pending()
