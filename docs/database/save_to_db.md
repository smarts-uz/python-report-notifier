# Report Notifier - Database Functions

## Overview

Module contains functions to:

- Extract data from chats by parsing
- Save the data to DB
- Send or forward the data to a specific group

## Functions

### save_to_db()

- Gets information by searching a certain keyword
- Saves the information to Message table
- Bot gets this data and sends to groups

### save_db_rss_group()

- Gets all messages on a certain group filtering by date
- Saves the information to TgGroupMessage table
- Bot gets this data and sends to groups

### save_db_rss_channel()

- Gets all messages on a certain channel filtering by date
- Saves the information to TgChannelMessage table

### save_to_report()

- Gets private link of a message that is present on DB!
- Creates a topic on a certain group 