import discord
import asyncio
import random
import secreto

client = discord.Client()

TOKEN = secreto.seu_token()

@client.event
async def on_ready():
    print('BOT ONLINE - Olá Mundo!')
    print(client.user.name)
    print(client.user.id)
    print('--------------Kay---------------')

@client.event
async def on_message(message):

    if message.channel.id == "400705396592869377":
        if message.author.bot:
            return
        else:
            return await client.send_message(message.channel, "Chamando @everyone os Heróis, um membro da nossa liga precisa de ajuda, cola junto!!!")


client.login(process.env.BOT_TOKEN);
