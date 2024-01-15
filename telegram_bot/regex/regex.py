import re
import time

# error :
str = "Flood control exceeded. Retry in 44.0 seconds"


def retry_after(str):
    result = re.search("Retry in", str)
    if result:
        matching = re.findall(r'\b\d+\.\d+\b', str)

        num = int(matching[0].split('.')[0])



        for i in range(num+1):
            time.sleep(1)
            print(f"retry after : {i+1}")

        # print('success')
        time.sleep(2)



