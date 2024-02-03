# [Report Notifier](https://github.com/smarts-uz/python-report-notifier)

This program parses data using [Xtrime TelegramAPIserver, TelegramRSS](https://github.com/xtrime-ru/TelegramApiServer) and saves the information on PostgreSQL database. Plus, it sends the corresponding information on specific groups using Telegram Bot.

<b> ⚠️ Make sure you have running instances of both Xtrime and RSS!</b>

## 💥 Features

- <i>Finds messages with a keyword, opens a topic in the name of that keyword in a separate group, and sends/forwards the found messages.</i>
- <i>Collects messages from specific groups with IDs. Bot sends replies to a specified message to a special group.</i>

## ⚙️ Installation

### 1. Create virtual environment
```py -m venv venv```

### 2. Install requirements
```pip install -r requirements.txt```

### 3. Create .env file using .env.example.
Fill the gaps with credentials you have:
```
TOKEN = ""
CHAT_ID = ""
PASSWORD = ""
HOST = ""
IP = ""
PORT = "9503"
PORT_RSS = "9504"
CHAT_ID_2 = ""
USER_NAME_LEN = 0
MESSAGE_LEN = 50
```
Now, you should be ready to run the program.

### 4. Run the main file of the project:
```
cd python-report-notifier
py main.py --help
```

This command shows the following instructions:
```
Usage: main.py [OPTIONS] COMMAND [ARGS]...
                                          
Options:                                  
  --help  Show this message and exit.     
                                          
Commands:                                 
  add-keyword                             
  add-report                              
  check-keyword                           
  check-report                            
  collect-msg-channel
  collect-msg-group
  get-dialogs
  get-rating
  run-searching
  show-keywords
```

Now, you can run any command you want. To read further, follow this list of contents:

- `add-keyword` - adds a new keyword
- `add-report` - adds a new report
- `check-keyword` - iterates through Keyword table and identifies for which keywords there are not any topics created
- `check-report` - iterates through Report table and identifies for which reports there are not any topics created
- `collect-msg-channel` - Collects messages in a channel with a given ID by iteration
- `collect-msg-group` - Collects messages in a group with a given ID by iteration
- `get-dialogs` - Filters all dialogs which are present on the main window of Telegram
- `get-rating` - Collects all messages that have at least one reply
- `run-searching` - alternative to writing "<your_search_query>" on Telegram's basic search bar
- `show-keywords` - Shows all keywords list