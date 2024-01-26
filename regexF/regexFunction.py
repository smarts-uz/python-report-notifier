import re
import time


# error :
# str = "Flood control exceeded. Retry in 44.0 seconds"
str1 = "telebot.apihelper.ApiTelegramException: A request to the Telegram API was unsuccessful. Error code: 429. Description: Too Many Requests: retry after 38"


def retry_after(str):
    result = re.search("retry after", str)
    if result:
        # matching = re.findall(r'\b\d+\.\d+\b', str) for float
        matching = re.findall(r'\b\d+\b', str)   #for integer

        num = int(matching[1].split('.')[0])





        for i in range(1,num+1):
            time.sleep(1)
            print(f"retry after : {i}")
        # print('success')
        time.sleep(1)


