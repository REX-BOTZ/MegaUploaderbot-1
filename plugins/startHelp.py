#!/usr/bin/env python3


"""Importing"""
# Importing Common Files
from botModule.importCommon import *


"""Start Handler"""
@Client.on_message(filters.private & filters.command("start"))
async def start_handler(bot:Update, msg:Message):
    if await search_user_in_community(bot, msg):
        await msg.reply_text(BotMessage.start_msg, parse_mode = 'html')
    return


"""Help Handler"""
@Client.on_message(filters.private & filters.command("help"))
async def help_handler(bot:Update, msg:Message):
    if await search_user_in_community(bot, msg):
        await msg.reply_text(BotMessage.help_msg, parse_mode = 'html')
    return

