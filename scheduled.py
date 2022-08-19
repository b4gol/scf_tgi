from helper_checker import *
from scrapper import *
import schedule
import asyncio
# from main_checker import upper, app

schedule.every().second.do(checker)
schedule.every().second.do(check_json)
# schedule.every(2).second.do(upper, app)

while True:
    schedule.run_pending()
    asyncio.sleep(0.01)

