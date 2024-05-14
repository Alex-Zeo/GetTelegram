# **README GetTelegram**
Data mine and track Telegram messages. These messages will be translated, stored, and categorized into SQL or SPARQL databases. Linguistic markers (idiolect), variance, quantitative analysis, and sentiment analysis will be performed on the data to identify patterns and insights.

**telegram.py**
This script is designed to extract messages from specified Telegram channels within a given date range using the Telethon library. The script collects a variety of message attributes, such as text content, sender information, media type, and metadata. It saves the extracted data into a CSV file for further analysis or archival purposes. The primary configuration parameters include the Telegram API credentials, the user's phone number, and the date range for message extraction.

![image](https://github.com/Alex-Zeo/GetTelegram/assets/6181715/c0f83f89-8624-48bb-bfab-30c84b567024)

The script establishes a connection to the Telegram API using the provided credentials. If the user is not authorized, it prompts for a login code sent to the phone number. Once connected, the script iterates through each channel, fetching messages within the specified date range. It handles rate limiting gracefully by pausing execution if a FloodWaitError occurs. The collected messages are then compiled into a pandas DataFrame and saved as a CSV file. The file is stored in the specified directory, and its name includes the start and end dates for easy identification. If no messages are found within the date range, the script will notify the user and skip the CSV creation.

**Telegram.xlsx**
Results include 106k+ telegram messages mined for April 2024
![image](https://github.com/Alex-Zeo/GetTelegram/assets/6181715/becd3ca7-214f-4754-9c2b-5ce7d2e9a0a5)

**translate.py**
Initial attempts to translate were unsuccessful
![image](https://github.com/Alex-Zeo/GetTelegram/assets/6181715/bd29e82b-76f7-462f-9099-1b0e5a3c1a87)
![image](https://github.com/Alex-Zeo/GetTelegram/assets/6181715/7afd1e8c-0161-47c7-8f2f-0a92f42ccf09)

A weekly instead of monthly chunking strategy was adopted.
