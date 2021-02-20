import json
import time
import datetime
import discord
import requests
from discord.ext import commands
from discord.utils import get
import os
import re

token = os.environ["token"]

print('Puffy.')

nitro_sniper = True




Puffy = discord.Client()
Puffy = commands.Bot(description='Puffy Selfbot', command_prefix="*", self_bot=True)



@Puffy.event
async def on_message(message):



    def NitroData(elapsed, code):
        print(

            f" - AUTHOR: {message.author}"
            f"\n - SERVER: {message.guild}"
            f"\n - CHANNEL: {message.channel}"
            f"\n - ELAPSED: {elapsed}"
            f"\n - CODE: {code}")


    time = datetime.datetime.now().strftime("%H:%M %p")
    if message.guild is None:
        dm = f"https://discord.com/channels/@me/{message.channel.id}/{message.id}"
    else:
        dm = f'https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id}'
    if 'discord.gift/' in message.content:
        if nitro_sniper:
            start = datetime.datetime.now()
            code = re.search("discord.gift/(.*)", message.content).group(1)

            headers = {'Authorization': token}

            r = requests.post(
                f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem',
                headers=headers,
            ).text

            elapsed = datetime.datetime.now() - start
            elapsed = f'{elapsed.seconds}.{elapsed.microseconds}'

            if 'This gift has been redeemed already.' in r:
                print(""
                      f"\n[{time} - Nitro Already Redeemed]")
                NitroData(elapsed, code)
                requests.post(os.environ["nitrohook"] ,json={
                    'embeds': [{
                        'title': 'Nitro already Redeemed',
                        'description': f'**Author:** `{message.author}`\n**Server:** `{message.guild}`\n**Channel:** `{message.channel}`\n**Elapsed:** `{elapsed}`\n**Code:** `{code}`',
                        "fields": [
                        {
                            "name": "Message Link",
                            "value": f"[Click to jump to the message!]({dm})"
                        }],
                        'color': '16711680',
                        "footer": {
                            'text': 'Snipe time'
                        },
                        'timestamp': f'{message.created_at}'
                    }]
                })


            elif 'subscription_plan' in r:
                print(""
                      f"\n[{time} - Nitro Success]")
                NitroData(elapsed, code)
                requests.post(os.environ["nitrohook"] ,json={
                    'embeds': [{
                        'title': 'Nitro Claimed Successfully!',
                        'description': f'**Author:** `{message.author}`\n**Server:** `{message.guild}`\n**Channel:** `{message.channel}`\n**Elapsed:** `{elapsed}`\n**Code:** `{code}`',
                        "fields": [
                        {
                            "name": "Message Link",
                            "value": f"[Click to jump to the message!]({dm})"
                        }],
                        'color': '65280',
                        "footer": {
                            'text': 'Snipe time'
                        },
                        'timestamp': f'{message.created_at}'
                    }]
                })

            elif 'Unknown Gift Code' in r:
                print(""
                      f"\n[{time} - Nitro Unknown Gift Code]")
                NitroData(elapsed, code)
                try:
                    requests.post(os.environ["nitrohook"] ,json={
                        'embeds': [{
                            'title': 'Unknown Gift Code',
                            'description': f'**Author:** `{message.author}`\n**Server:** `{message.guild}`\n**Channel:** `{message.channel}`\n**Elapsed:** `{elapsed}`\n**Code:** `{code}`',
                            "fields": [
                            {
                                "name": "Message Link",
                                "value": f"[Click to jump to the message!]({dm})",
                            }],
                            'color': '16711680',
                            "footer": {
                                'text': 'Snipe time'
                            },
                            'timestamp': f'{message.created_at}'
                        }]
                    })
                except:
                    pass
        else:
            return

@Puffy.event
async def on_message_delete(message):
    if message.guild == None:
        dm = f"https://discord.com/channels/@me/{message.channel.id}/{message.id}"
    else:
        dm = f"https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id}"
    name = "<@!778226094754103306>"
    if name in message.content:
        requests.post(os.environ["ghosthook"], json={
            'embeds': [{
                'title': 'Ghost Ping detected!',
                'description': f'**Author:** `{message.author}`\n**Server:** `{message.guild}`\n**Channel:** `{message.channel}`\n**Message:**\n{message.content}\n ',
                "fields": [
                {
                    "name": "Message Link",
                    "value": f"[Click to jump to the message!]({dm})",
                }],
                'color': '00000000',
                "footer": {
                    'text': 'Snipe time'
                },
                'timestamp': f'{message.created_at}'
            }]
        })


                             


Puffy.run(os.environ["token"], bot=False)
