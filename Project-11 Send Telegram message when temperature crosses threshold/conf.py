"""Configurations for telegram_alert.py"""
bolt_api_key = "876619b0-11e9-41e4-9206-c70652dcaac0"                 # This is your Bolt Cloud API Key
# This is the device ID and will be similar to BOLTXXXX where XXXX is some numbers
device_id = "BOLT1349843"
# This is the channel ID of the created Telegram channel. Paste after @ symbol.
telegram_chat_id = "@bolt_iot_temperature_monitor"
# This is the bot ID of the created Telegram Bot. Paste after bot text.
telegram_bot_id = "bot935754143:AAEePbgKjm3pjO07so34Klrf5xd_CcrLapQ"
threshold = 250                       # Threshold beyond which the alert should be sent