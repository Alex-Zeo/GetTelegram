# **README GetTelegram**
Data mine and track Telegram messages. These messages will be translated, stored, and categorized into SQL or SPARQL databases. Linguistic markers (idiolect), variance, quantitative analysis, and sentiment analysis will be performed on the data to identify patterns and insights.


**Overview**
This script is designed to extract messages from specified Telegram channels within a given date range using the Telethon library. The script collects a variety of message attributes, such as text content, sender information, media type, and metadata. It saves the extracted data into a CSV file for further analysis or archival purposes. The primary configuration parameters include the Telegram API credentials, the user's phone number, and the date range for message extraction.

**Configuration and Setup**
To run this script, update the code with your own Telegram API credentials (`api_id, api_hash) and phone number. These are essential for connecting to the Telegram API and accessing the specified channels. The script is configured to extract messages from a comprehensive list of channels defined in the channels list. You can modify this list based on your requirements. Additionally, ensure that the date range (start_dateandend_date`) is set to the desired period for message extraction.

**Execution**
The script establishes a connection to the Telegram API using the provided credentials. If the user is not authorized, it prompts for a login code sent to the phone number. Once connected, the script iterates through each channel, fetching messages within the specified date range. It handles rate limiting gracefully by pausing execution if a FloodWaitError occurs. The collected messages are then compiled into a pandas DataFrame and saved as a CSV file. The file is stored in the specified directory, and its name includes the start and end dates for easy identification. If no messages are found within the date range, the script will notify the user and skip the CSV creation.
