import discord
import asyncio
import random
import openpyxl
from discord import Member
from discord.ext import commands
import youtube_dl
from urllib.request import urlopen, Request
import urllib
import urllib.request
import bs4
import os
import sys
import json
from selenium import webdriver
import time
import datetime
from parser import *
client = discord.Client()
import requests
from bs4 import BeautifulSoup
import pyowm
 
def get_html(url):
   _html = ""
   resp = requests.get(url)
   if resp.status_code == 200:
      _html = resp.text
   return _html

###################################



API_Key = '52a192d87186e871d8ad7c1300c3730d'
owm = pyowm.OWM(API_Key)
 
City_ID = 1835848
obs = owm.weather_at_id(City_ID)    
 
# get_location은 지역에 대한 정보를 가져 옵니다.
L = obs.get_location()
City_name = L.get_name()




 





##########################################################################################################







@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("히공봇은 열일할꺼에용!!!")
    await client.change_presence(status=discord.Status.online, activity=game)




@client.event
async def on_message(message):
    if message.content.startswith("/날씨"):
# get_weather는 기상정보에 대한 정보를 가져옵니다.
        W = obs.get_weather()
        Temp = W.get_temperature(unit='celsius')
        await message.channel.send(City_name + '의 최고기온은 ' + str(Temp['temp_max']) + ' 도 입니다.')
        await message.channel.send(City_name + '의 최저기온은 ' + str(Temp['temp_min']) + ' 도 입니다.')
        await message.channel.send(City_name + '의 현재기온은 ' + str(Temp['temp']) + ' 도 입니다.')
 
        Status = W.get_status()
        await message.channel.send(City_name + '의 현재날씨는 ' + Status + ' 입니다.')

            







    


client.run('NjcyMTAwNzk5ODc0MjAzNjgw.XjGl1g.6dPJQLIDaSiG5CUvsLo0HhEof1g')