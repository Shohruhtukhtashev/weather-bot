# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 14:49:06 2021

@author: Shohruh Tukhtashev
"""


import logging
import python_weather
import asyncio
from aiogram import Bot, Dispatcher, executor, types
import math 
    
    
API_TOKEN = '1850109354:AAEdYjjm0YOJFvAKJEhP_D0Kqfnt8RtkZ1g'
client = python_weather.Client(format=python_weather.IMPERIAL)

 # Configure logging
logging.basicConfig(level=logging.INFO)

    

 # Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply(f"Assalomu alaykum.\nOb-havo botiga xush kelibsiz!\n Shahringiz nomini kiriting! ")


@dp.message_handler()
async def sendweather(message: types.Message):
   try:
       weather= await client.find(message.text)
       weat=weather.current.temperature
       weath=(weat-32)/1.8
       we=round(weath,1)
       
       await message.answer(f"Hozir {message.text}da harorat {we}°C.")
   except:
       await message.answer("Bu joy haqida ma'lumot topilmadi")


if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)
   

